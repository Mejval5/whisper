# Pathfinder session transcripts

Czech-language Pathfinder sessions recorded with Craig (Discord bot), transcribed locally with faster-whisper (large-v3, RTX 4090).

## Layout
- `sessions/<YYYY-MM-DD_name>/` - one folder per session. The user drops the Craig zip (or extracted per-user tracks) here.
  - `transcripts/<discord_user>.json|.txt` - one transcript per person
  - `transcript.md` / `transcript.json` - merged, time-ordered transcript
  - `summary.md` - AI summary (written by Claude)
- `campaign/speakers.json` - Discord username -> display name ("Player (Character)")
  - `sessions/<session>/speakers.json` (optional) overrides it for one session, e.g. when players shared a mic
- `campaign/glossary.txt` - names/terms passed to Whisper as spelling hints
- `campaign/notes.md` - running campaign memory across sessions
- `prompts/summary.md` - summary structure

## Commands
- Transcribe all new sessions: `.venv\Scripts\python.exe transcribe.py`
- One session: `.venv\Scripts\python.exe transcribe.py <session-folder>`
- After editing speakers.json: `.venv\Scripts\python.exe transcribe.py --merge-only <session-folder>`

## Summarizing a session
1. Read `campaign/notes.md`, `campaign/speakers.json`, `campaign/glossary.txt`, then the session's `transcript.md`.
2. Write `sessions/<session>/summary.md` following `prompts/summary.md`.
3. Update `campaign/notes.md` with new NPCs, places and open threads.
4. Suggest new glossary terms for names Whisper got wrong.
5. Copy the session into the GM bot, repo `D:\Projects\ai-plugins` (follow its CLAUDE.md: fresh worktree from `origin/main`, version bump, PR):
   `plugins/second-brain/skills/pathfinder/sezeni/sezeni_NN/zapis.md` <- `summary.md` (only for a new session; an existing `zapis.md` was edited by the GM bot, never overwrite it),
   `.../sezeni_NN/prepis.md` <- `transcript.md` with a header saying it is a raw transcript for grep only.
   The bot reads `zapis.md` and only greps `prepis.md`. NN follows the GM's numbering: 2026-09-29 = 03, 2026-10-11 = 04, 2026-10-13 = 05, 2026-10-21 = 06.
