# urbook video toolkit (set up 25 Nov 2026)

Run `bash tools/video/setup.sh` at the start of any reel job – it installs and verifies all five tools (≈1 min) and prints PASS / FAIL / WAIT.

| Tool | What urbook uses it for | Rule |
|---|---|---|
| **FFmpeg** | cut, trim silences, join clips, crop to 9:16 1080×1920, mix music (`audio/`), export H.264 | – |
| **Remotion** (`remotion/`) | the `StoryReel` template: real clips/photos as scenes, hook card in frame 1, captions inside the safe zone, music bed. Drive it with a props JSON (see `remotion/sample-props.json`) | uses the Playwright Chromium (`$URBOOK_CHROME`) |
| **HyperFrames** | animated title cards / motion graphics (HTML → MP4) layered into a reel | – |
| **Whisper** (faster-whisper) | burned-in subtitles from the voiceover (most people watch muted) | needs a local model, see below |
| **yt-dlp** | **urbook-owned content only** – back up or re-edit our own posted Instagram/TikTok/YouTube videos | never download other accounts' videos (Instagram/TikTok terms + copyright → account block risk) |

## Whisper model (one-off, Shan)
Hugging Face is blocked from Claude's cloud, so the model must sit in this repo:
download `Systran/faster-whisper-base.en` (files `model.bin`, `config.json`, `tokenizer.json`, `vocabulary.txt`, ≈145 MB)
into `models/whisper/base.en/` – or give Claude a Mac folder with them and Claude commits them.

## Making a story reel (what the social agent does)
1. Brief from `/ig-reel` (hook scored ≥ 50, beat sheet 15–45 s) + the reference notes in `<product>/reels/<platform>/notes.md`.
2. Footage, best first: Shan's own clips (`holiday/videos`, `parking/videos`, `transfers/videos`) → Shan's photos → licence-free `backgrounds/` (Pexels). Story arc: **problem → journey → relief → offer**, a new shot every 2–3 s.
3. Voiceover (Shan's voice or vidIQ voiceover) → Whisper subtitles → `StoryReel` props → render → `tools/urbook_sound.py mux` for the music bed.
4. Caption via `/ig-reel` checks → Metricool **for review** – nothing is posted without Shan's OK.

## Meta / TikTok safety (always)
- Our own or licence-free footage, music and fonts only; no other account's video, audio or watermark.
- No AI-made people; real people only with a signed consent form; realistic AI imagery gets the platform "AI info" label.
- Comment-keyword DMs only through Meta's own automated responses / Meta-approved partners – never unofficial bots.
- No claims we can't prove (best, cheapest, guaranteed, 24/7, free cancellation); prices only if they match the live site.
