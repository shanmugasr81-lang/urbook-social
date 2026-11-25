# Parking reels – instructions for the social agents

Owner: Shan. Written 25 Nov 2026. Agents (social, learn-social) read this file at the start of every parking reel task.
If anything here clashes with the Wix `Guardrails` rows, the guardrails win.

## 1. What we sell (Heathrow airport parking)
| Product | One-line promise (only what the live site says) | Music bed | Voice |
|---|---|---|---|
| Meet & Greet | A driver meets you at the terminal and takes your car; it is waiting when you land | `audio/airport-calm.m4a` | bf_alice |
| Park & Ride | Park nearby, short transfer to the terminal | `audio/05-lofi-departures.m4a` | bf_alice |
| Self Park | Park it yourself, walk or shuttle to the terminal | `audio/soft-travel.m4a` | bm_daniel |
| Park, Sleep & Fly | Hotel night + parking for early flights | `audio/lounge-evening.m4a` | bf_emma |

Prices, terminals and inclusions: take them from www.urbooktravel.com on the day (results page for Heathrow). If you cannot check the live price, leave `{{price}}` and flag it – never guess.

## 2. Where things live
- `instagram/links.md`, `tiktok/links.md` – reference reels Shan likes (links only).
- `instagram/notes.md`, `tiktok/notes.md` – the formula of each reference (hook, format, pacing, text), written by Claude from Shan's links and phone screen recordings. **Use these.** Agents never open, scrape or download Instagram/TikTok themselves (Instagram blocks it and it risks the account).
- `../videos/meet-and-greet/`, `../videos/park-and-ride/`, `../videos/self-park/`, `../videos/park-sleep-fly/` – Shan's own clips for each product (he is adding them). Our own footage only.
- `../../reels/specs/` – one JSON spec per reel (`parking-<product>-<idea>.json`).
- Built reels: `tools/video/remotion/out/` (not committed) → queued in Metricool **for Shan's review**.

## 3. How to build a parking reel
1. Pick the moment from the calendar (section 5) and one product.
2. Read the newest `notes.md` formulas + `anthropic-skills:ig-reel` rules. Write 3 hooks, score them (`tools/ig-reel/hookscore.py`, ≥ 50), pick the best.
3. Write the spec (example below), 15–30 s, 5–8 scenes, one idea per scene, each scene with a short `say` line.
4. `bash tools/video/setup.sh` (first time in a session), then `python3 tools/video/make_reel.py reels/specs/<name>.json`.
   It adds the British voice, the music at 12% under the voice, the urbook logo, the offer chip and the end card "Book at urbooktravel.com", loudness −14 LUFS and a `.srt`.
5. Watch 4 frames (start, middle, offer, end card) before queueing. Text must stay inside the safe zone.
6. Caption: `tools/ig-reel/caption.py` with 2 search phrases (e.g. "Heathrow Meet and Greet parking", "Heathrow airport parking"), ≤ 5 hashtags incl. #heathrow, end with "📍 Heathrow, London". Then queue in Metricool **for review** – never publish.

```json
{"name": "parking-meet-greet-terminal", "voice": "bf_alice", "music": "audio/airport-calm.m4a", "offer": "first",
 "end": {"title": "Heathrow Meet & Greet", "line": "Your car meets you at the terminal", "cta": "Book at urbooktravel.com"},
 "scenes": [
  {"seconds": 2.0, "src": "parking/videos/meet-and-greet/<clip>.mp4", "hook": "Heathrow T5 · 06:10", "say": "Heathrow Terminal 5, ten past six."},
  {"seconds": 2.5, "src": "parking/videos/meet-and-greet/<clip>.mp4", "caption": "Hand over the keys at the terminal", "say": "You hand over the keys right at the terminal."}
 ]}
```

## 4. Formulas that suit parking (use with the notes.md formulas)
- **POV timeline**: "06:10 drop the keys · 06:14 at check-in" – real times from the product, no invented claims.
- **The cost of getting it wrong**: missed flight / long walk from a far car park → the product that avoids it (no named competitors).
- **Checklist**: "3 things to do before you drive to Heathrow" → last item = book parking.
- **Product explainer in 20 s**: what happens at drop-off, during your trip, at pick-up.
- **Returning traveller**: "Booked with us before? £5 off with URBACK5."
Loop: the last line echoes the hook (e.g. starts and ends at the terminal).

## 5. When to post (UK travellers book 2–6 weeks ahead for parking)
| Posting month | Push |
|---|---|
| Dec | Christmas getaway; February half-term |
| Jan | February half-term; Easter |
| Feb–Mar | Easter holidays; May bank holidays |
| Apr | May half-term |
| May–Jun | Summer holidays (book early) |
| Jul | August bank holiday |
| Aug | September + October half-term |
| Sep–Oct | October half-term; Christmas getaway |
| Nov | Christmas getaway Meet & Greet |
Early flights → Park, Sleep & Fly all year. Full holiday plan: `reels/SEASONAL-PLAN.md`.

## 6. Hard rules (always)
- **Offer**: first booking URFIRST10 (£10 off) or WELCOMEUR (10% off); returning URBACK5 (£5 off). One code per booking.
- **Never say**: "free cancellation", "24/7", "guaranteed", "best", "cheapest", "No.1", "leading". Cancellation (only if needed): with Cancellation Cover, cancel online up to 24 hours before drop-off for a full refund of the booking price.
- **Never name** a parking, transfer or hotel provider, their car park or their staff.
- **People**: no recognisable people on video without a signed consent form; no AI-made people. Any voice is allowed (Shan, 25 Nov 2026) – tick the platform's AI-generated label when the voice is synthetic.
- **Footage and sound**: urbook-owned or free-licence only; our own music beds in `audio/`. Never another account's video, audio or words – copy the formula only.
- **Facts**: only from the live site / package. No invented numbers, reviews or customers. No number plates, faces of customers or booking details on screen.
- **Never post** – Metricool review queue only; Shan approves.
