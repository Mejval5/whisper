# Campaign notes

Running memory of the campaign, updated after each session summary.

Campaign: **Abomination Vaults**, currently in the prelude **Menace Under Otari** (Beginner's Box).
GM: Dan. Full GM material (character lore, NPCs, canon, session log) lives in the `pathfinder`
skill: `D:\Projects\ai-plugins\plugins\second-brain\skills\pathfinder\references\`
(`postavy.md`, `sezeni.md`, `druzina.md`, `kanon_menace_under_otari.md`, one file per character).
That is the source of truth and contains spoilers; this file is only what the transcripts need.
Player profiles (how each player talks and behaves at the table) are in `campaign/players/`.

## Party

| Character | Player | Discord | Build |
| --- | --- | --- | --- |
| Trigwynn | Veru | vrnk3014 | Duskwalker Oracle (Bones), Pharasma. Poses as a wandering bard |
| Ezekiel Monstrans | Vojta | prkno | Skeleton Thaumaturge (Chalice). Undead, wears a mask; healing hurts him |
| Arnold | Makak | makak4376 | Android Gunslinger (Drifter), amnesiac. Talks like a machine ("toto rozhodnutí je nelogické"). He is a Schwarzenegger reference (revealed 29/09); Makak plans to drop the robot speech |
| Rikkit Klaw | Milan | mj696969 | Ratfolk Inventor (crossbow), from another world. Speaks broken Czech in third person |

**Verrick** (Robo, robo_cuties, Human Ranger) left the game for good after 29/09/2026.

Mic setup changes between sessions. `campaign/speakers.json` holds the current setup (one mic
each); older sessions keep their shared-mic mapping in `sessions/<session>/speakers.json`:
- until 29/09/2026: Veru and Vojta shared vrnk3014, Makak on makak4376.
- 11/10/2026: Veru, Vojta and Makak in person on one account, **prkno**.
- 13/10/2026: everyone on their own mic. vrnk3014 = Veru, prkno = Vojta, makak4376 = Makak.

On a shared track, tell them apart by voice and grammar: Ezekiel speaks in masculine forms and
formal, archaic Czech ("Vyražme", "avšak"), Trigwynn in feminine forms, Arnold in a male voice
(possibly still the machine speech; it may go).

## Where we are (after 2026-10-21)

- **A11 throne hall cleared**: four kobolds dead this session. The **Kobold Trapmaster fled down
  the spiral stairs** (to floor 2), holding Trigwynn's arrow he caught in mid-air. More kobolds
  came up from below, so floor 2 is warned. The party rested about an hour in the hall; next
  session they go down the stairs.
- **Rikkit (Milan) was absent**, unexplained in the story ("maybe he'll catch up").
- Ezekiel was downed; a healing potion just ran out through his skull. Trigwynn revived him with
  her curse ability -> her body began to decay (curse stage 1, eased by 10 min Refocus). Ezekiel
  now knows she has **Curse of Living Death** and that her life force revived him; he owes her
  his life.
- Ezekiel gave Arnold **one Oil of Unlife** ("only in direst need"); Ezekiel carries the
  Everlight Crystal on his belt; Arnold fights with a torch. They swap back once out.
- Arnold's old crossbow is not by the A11 door (only a burnt-out torch); kobold armour (+2,
  heavy) piled in the hall.
- XP: 428 before this session; A11 not awarded yet.
- Sessions on Tuesdays, Sundays as backup. Next date not said; maybe in person in Pelhřimov [?].

## Sessions

Numbering follows the GM's `sezeni.md`, which counts an unrecorded crypt-fight session as 2.

- **Sessions 1-2** (by 20/09/2026): cellar, rats, spider, barricade, empty sarcophagus, crypt
  fight (not recorded).
- **Session 3** (29/09/2026): crypt aftermath, Gozreh shrine, kobolds in the storeroom, falling
  ceiling trap, Abadar's coin riddle. -> `sessions/2026-09-29_session/summary.md`
  (that file still calls itself "Sezení 2").
- **Session 4** (11/10/2026): first without Verrick, three players in person. A10 gear machine,
  spear trap kills a kobold, Arnold downed at the A11 door, retreat, Tamily, night at the
  fishery. -> `sessions/2026-10-11_session/summary.md`
- **Session 5** (13/10/2026): first with separate mics. Shopping in Otari: Keeleno's werewolf
  job, Carman gives Rikkit the forge key for a flume brake, Trigwynn kills a beggar (Void Warp)
  and Ezekiel swears silence. Back down to the barricade. -> `sessions/2026-10-13_session/summary.md`
- **Session 6** (21/10/2026): Rikkit absent, an hour lost to Veru's PC. A11 fight: Arnold and
  Ezekiel downed, Trigwynn kills three kobolds and revives Ezekiel with her curse, trapmaster
  flees downstairs. Oil of Unlife to Arnold, Trigwynn's fake calluses, "ukaž boky", second
  question game. -> `sessions/2026-10-21_session/summary.md`

## Important NPCs

- **Tamily** -> harbor warden, runs the fishery. Hired the party to clear the cellar. Sense
  Motive says she is honest: the wall fell about a week ago, two barrels (almost a ton) of fish
  gone, she is afraid to go down. Ezekiel told her only about rats, a giant spider and "a gap
  behind the spider". She does not believe rats and a spider ate a ton of fish. Gave 2 healing
  potions, 5 gp advance and rooms; will ask the guards in the morning.
- **Keeleno Lathenar** (name not said at the table yet) -> runs Otari Market. Buys at half price,
  no haggling, "bought too much iron already". A werewolf, "a local druid", killed his wife years
  ago; the guard had no proof. Hired Verrick "yesterday evening" to visit the druid; Verrick has
  not returned. Offers the party 20 gp + the silver dagger he carries (refuses to give it in
  advance). Buys wolf pelts. Sells silversheen 6 gp (4 gp if they go). Will ask around town for
  a pistol for Arnold. Watches Rikkit, "maybe knows why you are here". Closed on the 5th of Gozran [?].
- **Carman Rajani** -> smith, Blades for Glades (north of town). Gave Rikkit the forge key, old
  artisan's tools and a sketch: build a brake that stops the **logging flume**, must look like a
  breakdown, fit it at night when the guard changes, deadline 3-4 days, "elections in a week".
  Offered Rikkit 5 sp/day work. Bought Trigwynn's scimitar for 8 sp.
- **Kurator Ilya** -> Ezekiel's acquaintance. Carman thinks he may be at **Crook's Nook** (tavern
  on the big bridge over the river) in the evenings.
- **The beggar** -> old sailor, 40 years at sea, daughters in Absalom. Killed by Trigwynn in an
  alley near Otari Market. Body left there [?].
- **Kobolds** -> built the barricade and salt / fish-bone warding symbols to keep the thing from
  the sarcophagus out. Three killed in A07, one fled upstairs. In A11 one was killed by the
  spear trap; the rest killed on 21/10. They wore good armour.
- **Kobold Trapmaster** (GM lore: female) -> survived A11, fled down the spiral stairs with
  Trigwynn's arrow. Floor 2 is warned.
- **The dead from the sarcophagus** -> left the crypt before the barricade went up. Whereabouts
  unknown.

## Places

- **Otari** -> the town. The fishery cellar leads down into Menace Under Otari.
- **Otari Market** (Keeleno), **Blades for Glades** (Carman, north), **Crook's Nook** (tavern on
  the bridge over the river).
- **Immenwood** -> north/east of town; woodcutters keep finding claw notches on trunks (the werewolf).
- **A05 crypt** -> cleared, barricaded again by Arnold with sarcophagi.
- **A06 shrine of Gozreh** -> silver bowl, once-a-day blessing water (Trigwynn got Ocean's Might,
  Ezekiel got sick).
- **A07 storeroom** -> cell looted (200 sp, gold ring, shortsword).
- **A09** -> Abadar statue and coin riddle, solved; 8 gp taken.
- **A10 Abadar's Vault** -> chest looted by Ezekiel (contents not in the recording), chest now
  on the barricade. Gear machine (bell wheel, spear wheel, safety latch) works the A11 trap;
  jammed after the bell rang. Wall slits look into A11.
- **A11 hall** -> cleared 21/10. Spiral stairs at the back lead down to floor 2 (trapmaster fled
  there). GM: the room with the stairs is "certainly special". A pile of kobold armour.

## Items

- **Everlight Crystal** -> Ezekiel's belt since 21/10, still in the fishing net (half range).
  Arnold says "the ball is mine" and wants it back once they are out.
- **Oil of Unlife** -> one jar given to Arnold 21/10 (direst need only), to be returned.
- Arnold: new hand crossbow, 2 healing potions, 5 gp from Tamily. Sold the gem shortsword and
  other spare weapons. His old crossbow and torch are still in A11.
- Rikkit: 100 bolts [?], Artisan's Tools and the forge key from Carman, the brake sketch,
  Sold his sling. Repaired Ezekiel's sickle.
- Trigwynn: armour now worn, no longer encumbered. Shortbow + 20 arrows from Ezekiel, battleaxe.
  Sold the scimitar.
- Ezekiel: folding sickle repaired by Rikkit. Healing potions and Treat Wounds do not work on
  him (needs Stitch Flesh); only the chalice, Oil of Unlife, Trigwynn's ability. Sold scimitars.

## Open threads

- **Arnold's flashbacks:** GM sent Flashback 2 (spiral stairs) and reposted Interlude A. Makak
  misread Interlude A (grooves on the woman's side, not the ball's) -> "show your hips". Agreed:
  Arnold had a glitch and will work out in play that the grooves are on the ball.
- **Question game 21/10:** Arnold has "visions"; says war drove him out, he was a "liquidator",
  "I am human". Trigwynn: war drove her out, never fought, came "from far away", her body has
  rotted "since forever" (Sense Motive: not lying). No war on this island now. Ezekiel died
  "by my own doing". Red flash in Arnold's eye: "adrenaline".
- Trigwynn faked calluses on her knuckles to throw Arnold off.
- **Keeleno's werewolf job** (accepted by Ezekiel): Immenwood, notches on trunks. Where is Verrick?
- **Carman's flume brake** (Rikkit): due in 3-4 days. Why does Carman want the flume stopped?
- **Trigwynn's hunger:** she harvested the beggar and feels human again; without deaths she weakens
  and will lose physical strength.
- **Ezekiel and Trigwynn:** mutual silence about "secrets tied to death". He offered help; she told
  him never to follow her again.
- **Arnold suspects Trigwynn** (hands, "hips", soft skin, found in the fishery without a job);
  trusts nobody yet.
- Keeleno watches Rikkit and may know where he comes from.
- Kurator Ilya, maybe at Crook's Nook in the evening.
- A pistol for Arnold (Keeleno asks around).
- Arnold's eye blinked red when Ezekiel grappled him.
- Arnold thinks Tamily sent them to die; what Tamily learned from the guards.
- How Verrick's absence is explained in the story (Keeleno's job is the first hook).
- The jammed A10 machine; the kobolds in A11 heard the bell.
- The dead from the sarcophagus.
- The kobold who fled upstairs.
- Ezekiel's borrowed memory of kobolds warding a mausoleum.
- Ezekiel's mask secret: the party promised to keep it.
- Whom Trigwynn wanted to meet in the cellar ("chtěla jsem se s ní potkat").
- The sounds from the lower corridor, heard twice.
- **Table vs GM lore** (see session 5 summary): Keeleno still has the dagger (lore: it lies by
  Verrick's body), reward 20 gp vs 50 gp, the beggar kill paid out (lore: killing now yields
  nothing), Carman named the brake price on day one, Ilya placed at Crook's Nook vs the museum.
