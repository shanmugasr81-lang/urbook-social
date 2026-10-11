"""urbook YouTube renderer v2 (11 Oct 2026; regular landscape video, not a Short).
v2: "challenge": true -> the question + a small GBP 50 voucher line are on the title slide (8s) and the thumbnail.
spec.json -> urbook-<date>-youtube.mp4 (1920x1080, ~45-60s, silent) + urbook-<date>-thumb.png (1280x720).
Usage: python3 urbook_render_yt.py spec.json logo.png fontsdir outdir
Uses the SAME spec.json as urbook_render.py v3, plus optional fields:
  "headline": SEO headline shown on the title slide
  "details": [one short sentence per point, <= ~120 chars] shown on each point's own slide
  "question": the comment question shown on the last slide
  "news_source": e.g. "Source: heathrow.com, 27 Sep 2026"
Slides: title (5s) -> news (7s) -> overview (6s) -> one slide per point (6s each) -> outro (7s).
With 3-5 points the video is about 43-55 seconds.
"""
import json, sys, os, html, subprocess
from playwright.sync_api import sync_playwright

spec_p, logo_p, fonts, out = sys.argv[1:5]
S = json.load(open(spec_p))
os.makedirs(out, exist_ok=True)
E = lambda s: html.escape(s or "")
INK, INK2, SUN, SUN2, PALE = "#0E2A47", "#17395C", "#F5821F", "#FFB020", "#E8EEF5"
W, H = 1920, 1080
PTS = S["points"]; NP = len(PTS)
DET = S.get("details") or [""] * NP
DET = (DET + [""] * NP)[:NP]

def face(fam, f, w):
    return f"@font-face{{font-family:'{fam}';font-weight:{w};src:url('file://{fonts}/{f}') format('woff2')}}"
CSS = "".join([face("Baloo 2", f"baloo-2-latin-{w}-normal.woff2", w) for w in (600, 700, 800)] +
              [face("DM Sans", f"dm-sans-latin-{w}-normal.woff2", w) for w in (400, 500, 700)])
LOGO = f"file://{os.path.abspath(logo_p)}"
CHECK = f'<svg style="flex-shrink:0" width="54" height="54" viewBox="0 0 24 24" fill="none" stroke="{SUN2}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12.5 9.5 18 20 6"/></svg>'

def page(w, h, body):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}
*{{box-sizing:border-box}}body{{margin:0;width:{w}px;height:{h}px;background:{INK};color:#fff;font-family:'DM Sans';overflow:hidden}}
.b{{font-family:'Baloo 2'}} .pill{{background:{SUN};color:{INK};font-weight:700;font-size:26px;letter-spacing:.08em;padding:12px 26px;border-radius:999px}}
</style></head><body>{body}</body></html>"""

def header():
    return (f'<div style="display:flex;justify-content:space-between;align-items:flex-start">'
            f'<span class="pill">{E(S["tag"]).upper()}</span>'
            f'<img src="{LOGO}" style="width:132px;height:132px;border-radius:26px"></div>')

def footer(k, total):
    pct = int(100 * (k + 1) / total)
    return (f'<div style="display:flex;flex-direction:column;gap:18px">'
            f'<div style="display:flex;justify-content:space-between;align-items:center">'
            f'<span class="b" style="font-weight:700;font-size:38px">www.urbook.co.uk</span>'
            f'<span style="border:3px solid {SUN2};color:{SUN2};font-weight:700;font-size:28px;padding:8px 22px;border-radius:14px">URFIRST10 · £10 off</span></div>'
            f'<div style="height:8px;background:{INK2};border-radius:4px"><div style="height:8px;width:{pct}%;background:{SUN2};border-radius:4px"></div></div></div>')

def frame(inner, k, total):
    return (f'<div style="width:{W}px;height:{H}px;padding:64px 110px 56px;display:flex;flex-direction:column;gap:30px">'
            f'{header()}<div style="flex-grow:1;display:flex;flex-direction:column;justify-content:center;gap:34px">{inner}</div>{footer(k, total)}</div>')

slides = []  # (html_inner, seconds)
CH = bool(S.get("challenge")) and bool(S.get("question"))
PRIZE = "Comment your answer &middot; correct answers can win a &pound;50 urbook voucher &middot; T&amp;Cs in the description"
if CH:
    qs = 46 if len(S["question"]) <= 160 else 38
    title = (f'<span class="b" style="font-weight:800;font-size:104px;line-height:.95">{E(S["hook"])}</span>'
             f'<span class="b" style="font-weight:700;font-size:70px;line-height:1;color:{SUN2}">{E(S["hook2"])}</span>'
             f'<div style="background:{INK2};border-radius:26px;padding:28px 40px;border-left:10px solid {SUN};display:flex;flex-direction:column;gap:12px;max-width:1650px">'
             f'<span style="font-size:{qs}px;font-weight:500;line-height:1.3">{E(S["question"])}</span>'
             f'<span style="font-size:28px;font-weight:500;color:{SUN2}">{PRIZE}</span></div>')
    slides.append((title, 8))
else:
    title = (f'<span class="b" style="font-weight:800;font-size:132px;line-height:.95">{E(S["hook"])}</span>'
             f'<span class="b" style="font-weight:700;font-size:92px;line-height:1;color:{SUN2}">{E(S["hook2"])}</span>'
             + (f'<span style="font-size:40px;color:{PALE};max-width:1500px;line-height:1.3">{E(S.get("headline"))}</span>' if S.get("headline") else ""))
    slides.append((title, 5))
news = (f'<span class="b" style="font-weight:800;font-size:84px;line-height:1">What\'s new</span>'
        f'<div style="background:{INK2};border-radius:28px;padding:40px 48px;border-left:10px solid {SUN};display:flex;flex-direction:column;gap:14px;max-width:1600px">'
        f'<span style="font-size:24px;font-weight:700;letter-spacing:.12em;color:{SUN2}">{E(S.get("news_label","TRAVEL NEWS TODAY"))}</span>'
        f'<span style="font-size:46px;line-height:1.3">{E(S["news"])}</span>'
        + (f'<span style="font-size:24px;color:{PALE}">{E(S.get("news_source"))}</span>' if S.get("news_source") else "")
        + '</div>')
slides.append((news, 7))
fs = 50 if NP <= 3 else 42
ov = (f'<span class="b" style="font-weight:800;font-size:78px;line-height:1;color:{SUN2}">{E(S.get("points_title") or "In this video")}</span>'
      + "".join(f'<div style="display:flex;gap:26px;align-items:center">{CHECK}<span style="font-size:{fs}px;font-weight:500;line-height:1.2">{E(p)}</span></div>' for p in PTS))
slides.append((ov, 6))
for i, (p, d) in enumerate(zip(PTS, DET)):
    s = (f'<span class="b" style="font-weight:800;font-size:40px;color:{SUN2};letter-spacing:.04em">{i+1} / {NP}</span>'
         f'<span class="b" style="font-weight:800;font-size:104px;line-height:1.02;max-width:1650px">{E(p)}</span>'
         + (f'<span style="font-size:46px;line-height:1.35;color:{PALE};max-width:1550px">{E(d)}</span>' if d else ""))
    slides.append((s, 6))
q = S.get("question")
outro_inner = (f'<div style="width:{W}px;height:{H}px;display:flex;align-items:center;justify-content:center;gap:110px;padding:80px 120px">'
               f'<img src="{LOGO}" style="width:440px;height:440px;border-radius:72px">'
               f'<div style="display:flex;flex-direction:column;gap:28px">'
               f'<span class="b" style="font-weight:800;font-size:88px;line-height:1">www.urbook.co.uk</span>'
               f'<span style="font-size:40px;color:{PALE}">Parking · Transfers · Holidays — one booking place</span>'
               f'<div style="background:{SUN2};color:{INK};border-radius:28px;padding:30px 48px;display:flex;flex-direction:column;gap:6px;align-self:flex-start">'
               f'<span class="b" style="font-weight:800;font-size:96px;line-height:1">URFIRST10</span><span style="font-size:36px;font-weight:700">£10 off your first booking</span></div>'
               + (f'<span style="font-size:36px;line-height:1.3;max-width:900px">💬 {E(q)}</span>' if q else "")
               + '</div></div>')
TOTAL = len(slides) + 1
bodies = [frame(h_, k, TOTAL) for k, (h_, _) in enumerate(slides)] + [outro_inner]
durs = [d for _, d in slides] + [7]

TQ = ""
if CH:
    TQ = (f'<span style="font-size:{30 if len(S["question"])<=120 else 24}px;line-height:1.3;max-width:1150px;margin-top:14px">{E(S["question"])}</span>'
          f'<span style="font-size:22px;color:{SUN2}">Comment your answer &middot; win a &pound;50 urbook voucher</span>')
thumb = (f'<div style="width:1280px;height:720px;padding:52px 64px;display:flex;flex-direction:column;justify-content:space-between;background:{INK}">'
         f'<div style="display:flex;justify-content:space-between;align-items:flex-start"><span class="pill" style="font-size:24px">{E(S["tag"]).upper()}</span>'
         f'<img src="{LOGO}" style="width:120px;height:120px;border-radius:24px"></div>'
         f'<div style="display:flex;flex-direction:column;gap:10px"><span class="b" style="font-weight:800;font-size:{80 if CH else 112}px;line-height:.92">{E(S["hook"])}</span>'
         f'<span class="b" style="font-weight:800;font-size:{60 if CH else 84}px;line-height:1;color:{SUN2}">{E(S["hook2"])}</span>{TQ}</div>'
         f'<span class="b" style="font-weight:700;font-size:34px">www.urbook.co.uk</span></div>')

d = S["date"]
with sync_playwright() as p:
    b = p.chromium.launch()
    jobs = [(f"s{k}", W, H, body) for k, body in enumerate(bodies)] + [("thumb", 1280, 720, thumb)]
    for name, w, h, body in jobs:
        pg = b.new_page(viewport={"width": w, "height": h})
        hp = os.path.abspath(f"{out}/_{name}.html"); open(hp, "w").write(page(w, h, body))
        pg.goto("file://" + hp); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(500)
        pg.screenshot(path=f"{out}/_{name}.png"); pg.close(); os.remove(hp)
    b.close()
os.replace(f"{out}/_thumb.png", f"{out}/urbook-{d}-thumb.png")

X = 0.6  # crossfade seconds
inputs, filt = [], []
for k, dur in enumerate(durs):
    L = dur + X
    inputs += ["-loop", "1", "-t", f"{L}", "-i", f"{out}/_s{k}.png"]
    filt.append(f"[{k}:v]scale=2112:1188,zoompan=z='min(zoom+0.0004,1.05)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={int(L*30)}:s={W}x{H}:fps=30,setsar=1,format=yuv420p[c{k}]")
prev, T = "c0", durs[0] + X
for k in range(1, len(durs)):
    lab = "v" if k == len(durs) - 1 else f"x{k}"
    tr = "slideleft" if 3 <= k < 3 + NP else "fade"
    filt.append(f"[{prev}][c{k}]xfade=transition={tr}:duration={X}:offset={T - X:.2f}[{lab}]")
    prev, T = lab, T + durs[k]
n = len(durs)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *inputs, "-f", "lavfi", "-t", f"{T:.2f}", "-i", "anullsrc=r=44100:cl=stereo",
                "-filter_complex", ";".join(filt), "-map", "[v]", "-map", f"{n}:a", "-c:v", "libx264", "-preset", "medium", "-crf", "21",
                "-c:a", "aac", "-shortest", "-movflags", "+faststart", f"{out}/urbook-{d}-youtube.mp4"], check=True)
for k in range(n): os.remove(f"{out}/_s{k}.png")
print("done", sorted(os.listdir(out)), f"{T:.1f}s")
