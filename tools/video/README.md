# urbook video toolkit (set up 25 Nov 2026)

Run `bash tools/video/setup.sh` at the start of any reel job – it installs and verifies all five tools (≈1 min) and prints PASS / FAIL / WAIT.

| Tool | What urbook uses it for | Rule |
|---|---|---|
| **FFmpeg** | cut, trim silences, join clips, crop to 9:16 1080×1920, mix music (`audio/`), export H.264 | – |
| **Remotion** (`remotion/`) | the `StoryReel` template: real clips/photos as scenes, hook card in frame 1, captions inside the safe zone, music bed. Drive it with a props JSON (see `remotion/sample-props.json`) | uses the Playwright Chromium (`$URBOOK_CHROME`) |
| **HyperFrames** | animated title cards / motion graphics (HTML → MP4) layered into a reel | – |
| **Whisper** (faster-whisper) | burned-in subtitles from the voiceover (most people watch muted) | needs a local model, see below |
| **yt-dlp** | **urbook-owned content only** – back up or re-edit our own posted Instagram/TikTok/YouTube videos | never download other accounts' videos (Instagram/TikTok terms + copyright → account block risk) |

## Whisper model (done by Claude, 26 Nov 2026)
Hugging Face is blocked from Claude's cloud, so GitHub fetches it: the `whisper-model` workflow put
`Systran/faster-whisper-base.en` (MIT; `model.bin`, `config.json`, `tokenizer.json`, `vocabulary.txt`, ≈145 MB)
on the release `model-whisper-base.en` of this repo, and `setup.sh` downloads it into `models/whisper/base.en/`
(not committed – too big for git).

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

## Voice, logo, offer and end card (v2, 25 Nov 2026)
- `python3 tools/video/make_reel.py reels/specs/<name>.json` → voice per scene (Kokoro British voice), render, loudness -14 LUFS, `.srt` subtitles. Example spec: `reels/specs/holiday-nepal-ebc-day4.json`.
- Every reel gets the urbook logo (white badge), an offer chip on the last two scenes (`"offer": "first"` = URFIRST10, `"returning"` = URBACK5) and a 3 s end card: logo, package, offer, "Book at urbooktravel.com".
- Strong voice, mild music: the music bed drops to 12% under the voice.
- Voices: bf_alice, bf_emma, bf_isabella, bf_lily, bm_daniel, bm_fable, bm_george, bm_lewis. Region → voice + music: `reels/seasonal-plan.json`.
- Any voice is allowed (Shan, 25 Nov 2026). Tick the AI-generated label when the voice is synthetic. No people on video without signed consent.
- Checked and not used: Edge-TTS (Microsoft service, blocked here and not cleared for commercial use), F5-TTS (non-commercial weights), VoiceStudio / Voicebox (GPU desktop apps; Kokoro inside them is the same engine we use). Whisper is only needed for Shan's own recorded voice; with Kokoro we already know the words, so the `.srt` is made from the script.

## Shan's own reels – keep his voice and music (25 Nov 2026)
- Shan sends a reel (chat attachment or Google Drive folder "urbook reels") with one line: `reel · holiday|parking · place/product · what it shows · IG/TikTok/both`.
- Spec: `"keepSound": true` – the clip's own voice + music play exactly as recorded; no music bed, no Kokoro voice. Scenes use `start` / `seconds` to cut; captions = the words Shan says (he types them, or Whisper once its model is in models/whisper/).
- Still added: subtitles, urbook logo, offer chip, end card "Book at urbooktravel.com".
- Music already inside the video must be licensed for business use (our own, or royalty-free). For an Instagram/TikTok trending sound, export WITHOUT that music and add the sound in the app when posting – a copyrighted track baked into the file can be muted or blocked.
