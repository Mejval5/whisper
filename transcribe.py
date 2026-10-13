"""Transcribe Craig (Discord) multi-track recordings into per-speaker and merged transcripts.

Usage:
    python transcribe.py                 # process every session folder that has no transcript yet
    python transcribe.py SESSION [...]   # process specific session folders (name or path)
    python transcribe.py --force SESSION # redo transcription even if outputs exist
    python transcribe.py --merge-only SESSION  # rebuild transcript.md from existing per-speaker files
"""

import argparse
import json
import os
import re
import sys
import time
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SESSIONS_DIR = ROOT / "sessions"
CAMPAIGN_DIR = ROOT / "campaign"
SPEAKERS_FILE = CAMPAIGN_DIR / "speakers.json"
GLOSSARY_FILE = CAMPAIGN_DIR / "glossary.txt"

AUDIO_EXTS = {".flac", ".ogg", ".opus", ".m4a", ".aac", ".wav", ".mp3"}

MODEL = "large-v3"
LANGUAGE = "cs"
# Consecutive lines from the same speaker closer than this (seconds) are joined in the merged transcript.
JOIN_GAP = 2.0
# Batched inference is several times faster on a big GPU; lower it if you run out of VRAM.
BATCH_SIZE = 16


def add_cuda_dlls():
    """Make the pip-installed cuBLAS/cuDNN DLLs visible to CTranslate2 on Windows."""
    if os.name != "nt":
        return
    import site

    for base in site.getsitepackages():
        for sub in ("nvidia/cublas/bin", "nvidia/cudnn/bin", "nvidia/cuda_nvrtc/bin"):
            d = Path(base) / sub
            if d.is_dir():
                os.add_dll_directory(str(d))
                os.environ["PATH"] = str(d) + os.pathsep + os.environ["PATH"]


def load_speakers():
    if SPEAKERS_FILE.exists():
        return json.loads(SPEAKERS_FILE.read_text(encoding="utf-8"))
    return {}


def load_glossary():
    """Names/terms that Whisper should spell correctly (one per line, # comments allowed)."""
    if not GLOSSARY_FILE.exists():
        return None
    terms = [
        line.strip()
        for line in GLOSSARY_FILE.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]
    return ", ".join(terms) or None


def speaker_id(audio_path: Path) -> str:
    # Craig names tracks like "1-username.flac"; drop the track number.
    return re.sub(r"^\d+-", "", audio_path.stem)


def find_tracks(session: Path) -> list[Path]:
    audio_dir = session / "audio"
    for z in session.glob("*.zip"):
        marker = audio_dir / f".extracted-{z.stem}"
        if not marker.exists():
            print(f"  extracting {z.name}")
            audio_dir.mkdir(exist_ok=True)
            with zipfile.ZipFile(z) as zf:
                zf.extractall(audio_dir)
            marker.touch()
    tracks = [
        p
        for p in session.rglob("*")
        if p.suffix.lower() in AUDIO_EXTS and "transcripts" not in p.parts and not p.name.startswith(".")
    ]
    return sorted(tracks)


def fmt_ts(seconds: float) -> str:
    s = int(seconds)
    return f"{s // 3600:02d}:{s % 3600 // 60:02d}:{s % 60:02d}"


def transcribe_track(model, track: Path, out_json: Path, hotwords):
    t0 = time.time()
    segments, info = model.transcribe(
        str(track),
        language=LANGUAGE,
        beam_size=5,
        batch_size=BATCH_SIZE,
        without_timestamps=False,  # batched mode defaults to one segment per ~30 s chunk; we need per-sentence times to merge speakers
        vad_filter=True,  # Craig tracks are mostly silence; VAD prevents hallucinated text in the gaps
        vad_parameters={"min_silence_duration_ms": 500},
        condition_on_previous_text=False,  # avoids repetition loops on long files
        hotwords=hotwords,
    )
    result = []
    for seg in segments:
        text = seg.text.strip()
        if text:
            result.append({"start": round(seg.start, 2), "end": round(seg.end, 2), "text": text})
            print(f"    [{fmt_ts(seg.start)}] {text}")
    out_json.write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
    out_json.with_suffix(".txt").write_text(
        "\n".join(f"[{fmt_ts(s['start'])}] {s['text']}" for s in result) + "\n", encoding="utf-8"
    )
    print(f"  done in {time.time() - t0:.0f}s ({info.duration / 60:.0f} min of audio)")


def merge(session: Path, speakers: dict):
    lines = []
    for f in sorted((session / "transcripts").glob("*.json")):
        name = speakers.get(f.stem, f.stem)
        for seg in json.loads(f.read_text(encoding="utf-8")):
            lines.append({"speaker": name, **seg})
    lines.sort(key=lambda s: s["start"])

    joined = []
    for seg in lines:
        prev = joined[-1] if joined else None
        if prev and prev["speaker"] == seg["speaker"] and seg["start"] - prev["end"] <= JOIN_GAP:
            prev["text"] += " " + seg["text"]
            prev["end"] = max(prev["end"], seg["end"])
        else:
            joined.append(dict(seg))

    (session / "transcript.json").write_text(json.dumps(joined, ensure_ascii=False, indent=1), encoding="utf-8")
    md = [f"# {session.name}", ""]
    md += [f"[{fmt_ts(s['start'])}] **{s['speaker']}:** {s['text']}" for s in joined]
    (session / "transcript.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"  merged {len(joined)} lines -> {session / 'transcript.md'}")


def resolve_sessions(names):
    if not names:
        return [p for p in sorted(SESSIONS_DIR.iterdir()) if p.is_dir() and not (p / "transcript.md").exists()]
    out = []
    for n in names:
        p = Path(n)
        p = p if p.is_dir() else SESSIONS_DIR / n
        if not p.is_dir():
            sys.exit(f"Session folder not found: {n}")
        out.append(p.resolve())
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("sessions", nargs="*")
    ap.add_argument("--force", action="store_true", help="re-transcribe tracks that already have output")
    ap.add_argument("--merge-only", action="store_true", help="only rebuild the merged transcript")
    args = ap.parse_args()
    # Redirected stdout on Windows defaults to cp1252, which can't print Czech.
    sys.stdout.reconfigure(encoding="utf-8", errors="replace", line_buffering=True)

    SESSIONS_DIR.mkdir(exist_ok=True)
    sessions = resolve_sessions(args.sessions)
    if not sessions:
        print("Nothing to do. Put a Craig recording into sessions/<session-name>/ first.")
        return

    speakers = load_speakers()
    hotwords = load_glossary()
    model = None

    for session in sessions:
        print(f"== {session.name}")
        out_dir = session / "transcripts"
        out_dir.mkdir(exist_ok=True)
        if not args.merge_only:
            tracks = find_tracks(session)
            if not tracks:
                print("  no audio found, skipping")
                continue
            for track in tracks:
                out_json = out_dir / f"{speaker_id(track)}.json"
                if out_json.exists() and not args.force:
                    print(f"  {track.name}: already transcribed")
                    continue
                if model is None:
                    add_cuda_dlls()
                    from faster_whisper import BatchedInferencePipeline, WhisperModel

                    print(f"  loading {MODEL} on GPU...")
                    model = BatchedInferencePipeline(WhisperModel(MODEL, device="cuda", compute_type="float16"))
                print(f"  {track.name}")
                transcribe_track(model, track, out_json, hotwords)
        merge(session, speakers)


if __name__ == "__main__":
    main()
