# urbook social reels – the process (Shan, 25 Nov 2026)

Agents (social, learn-social) and Claude follow this for every reel. Hard rules in `parking/reels/INSTRUCTIONS.md` and the `ig-reel` skill still apply.

## 1. Where things go
| What | Where | Used for |
|---|---|---|
| **Original videos + audio** (Shan's own filming, his voice, our music) | GitHub `urbook-social`: `holiday/videos/<place>/`, `parking/videos/<product>/`, music beds `audio/` | Posted as urbook reels |
| **Reference reels** (other creators, screen recordings) | Google Drive `Reels` → `Reference – learn only` (or Shan's chat message) | Formula only → `holiday|parking/reels/<platform>/notes.md`. Never their video, voice or music |
| Shan's own clips in Drive | Drive `Reels` → `Own – can post` | Claude copies them into GitHub, then builds the reel |
| Read files | Logged in the `Reels read log` sheet → Apps Script moves them to `Archive – read` nightly and bins them after 7 days | |

## 2. Voice and music
- Shan's own reels: `"keepSound": true` – his voice and music exactly as recorded.
- Built reels: a British voice (male `bm_daniel` / `bm_george`, female `bf_emma` / `bf_isabella`) and a music bed from `audio/` at 12% under the voice – region → voice + music in `reels/seasonal-plan.json`.
- Music inside a file must be ours or royalty-free. Trending app sounds are added in the app when posting, never baked into the file.

## 3. The natural look (like the Colmar TikTok Shan liked)
- Real footage or photos that move (slow zoom/pan), a new shot every **2–3 s**, 15–30 s total.
- TikTok-native captions: white heavy text, dark outline, centred, **one `*word*` highlighted in yellow** per line, one line per beat.
- Branding stays small: a small see-through logo during the reel; the offer chip only on the last scene; a short 2.5 s end card (logo, package, price only if it matches the live site, URFIRST10, "Book at urbooktravel.com").
- Every caption matches what is on screen and comes from the package's own facts.

## 4. Maximum hooks – so people watch, like, save, share and book
1. **Write 8 hooks, score them** (`tools/ig-reel/hookscore.py`), use the top one (must be ≥ 50; aim for 80+).
2. **Re-hook every 4–6 s**: each beat opens something new – a day number, a surprise ("…and a cable car is included"), a contrast ("most people need a week").
3. **Late reveal** – name the package or price near the end (keeps people to the end = higher watch time).
4. **Loop** – the last line echoes the hook so the replay feels seamless.
5. **Make it worth saving and sending by itself** – a day-by-day plan, a price, "what's included". Never ask for it: no "share this", "tag someone", "follow for more", "like if…" (Meta and TikTok demote engagement bait).
6. **One booking line** at the end (offer + urbooktravel.com) – the caption carries the search phrases and one CTA.

## 5. Every post, before Metricool
Subtitles (`.srt` from the script), urbook logo, offer, end card, loudness −14 LUFS – all done by `python3 tools/video/make_reel.py reels/specs/<name>.json`. Tick the AI-generated label when the voice is synthetic. Queue **for Shan's review** – never publish.

Examples: `reels/specs/holiday-uk-scotland-3day.json` (photos, 3-day tour), `reels/specs/holiday-nepal-ebc-natural.json` (video clips).
