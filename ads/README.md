# urbook ad images (Google Ads + future promotions)

Made 11 Nov 2026 at Shan's request.

- `holidays/branded/` – one image per live holiday package (Wix `Holidays`, active, hero photo), with the urbook logo badge, a short title and a subtitle. Sizes: `_landscape` 1200×628, `_square` 1200×1200.
- `holidays/clean/` – the same photos with no text or logo. **Use these for Google Ads image assets**: Google often disapproves or limits images with overlaid logos or text. Branded = social, email, WhatsApp, Display/Demand Gen tests.
- `holidays/index.tsv` – slug · Wix media id · title · subtitle.
- `parking/` – Heathrow / parking / airport photos (Pexels free licence, no faces or readable plates), landscape 1200×628, square 1200×1200, portrait 960×1200.
- Renderer: `tools/urbook_ad_images.py` (fonts Baloo 2 800 + DM Sans 700 from @fontsource, logo `tools/urbook-logo.png`). Add a row to index.tsv and rerun when a new package goes live.

Rules: no faces, no number plates, no prices, never "free cancellation" / "24/7".

## Social posts (Shan, 11 Nov 2026)
The social agent uses these too: **Thursday (holidays & flights)** – background photo from `backgrounds/holiday/packages/<slug>.jpg` (full-size originals, listed in `backgrounds/index.json` with region + package), and the matching `ads/holidays/branded/<slug>_square.jpg` as the closing card. **Saturday (parking / transfers)** – `ads/parking/` photos (same Pexels set as `backgrounds/parking|airport|transfer`). Usual rules: no photo reused within 28 days (SocialMediaLog), no prices, UK framing.
