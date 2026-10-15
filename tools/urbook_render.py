"""urbook daily post renderer v5 (15 Oct 2026) – v5: optional "bg" = photo path or list of photo paths; when set, EVERY slide
gets a full-bleed natural photo under a neutral dark scrim (no navy), cards become dark glass (Shan, 15 Oct 2026).
Without "bg" the output is exactly v4.
urbook daily post renderer v4 (11 Oct 2026): spec.json -> feed PNG (1080x1350), story PNG and vertical MP4 (1080x1920).
Usage: python3 urbook_render.py spec.json logo.png fontsdir outdir
spec: {"date","tag","hook","hook2","points":[3-5 strings],"news","news_label"(opt), "points_title"(opt, e.g. "3-day itinerary"),
       "challenge"(opt, true on challenge days), "question"(the challenge question)}
v4: on challenge days the QUESTION is printed on the cover (first slide / Reel cover / feed image) under the hook,
    with a small line about the GBP 50 voucher draw, so nobody has to scroll the caption to find it (Shan, 11 Oct 2026).
"""
import json, sys, os, html, subprocess
from playwright.sync_api import sync_playwright

spec_p, logo_p, fonts, out = sys.argv[1:5]
S = json.load(open(spec_p))
os.makedirs(out, exist_ok=True)
E = lambda s: html.escape(s)
INK, INK2, SUN, SUN2, PALE = "#0E2A47", "#17395C", "#F5821F", "#FFB020", "#E8EEF5"

def face(fam, f, w):
    return f"@font-face{{font-family:'{fam}';font-weight:{w};src:url('file://{fonts}/{f}') format('woff2')}}"
CSS = "".join([face("Baloo 2", f"baloo-2-latin-{w}-normal.woff2", w) for w in (600, 700, 800)] +
              [face("DM Sans", f"dm-sans-latin-{w}-normal.woff2", w) for w in (400, 500, 700)])
CHECK = f'<svg style="flex-shrink:0" width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="{SUN2}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12.5 9.5 18 20 6"/></svg>'
LOGO = f"file://{os.path.abspath(logo_p)}"

BG = S.get("bg") or []
if isinstance(BG, str): BG = [BG]
BG = [os.path.abspath(x) for x in BG if x and os.path.exists(x)]
PH = bool(BG)
CARD = "rgba(8,12,18,.58)" if PH else INK2
def bgcss(k):
    if not PH: return f"background:{INK}"
    u = BG[k % len(BG)]
    return (f"background:linear-gradient(180deg,rgba(0,0,0,.42) 0%,rgba(0,0,0,.28) 38%,rgba(0,0,0,.62) 78%,rgba(0,0,0,.82) 100%),"
            f"url('file://{u}') center/cover no-repeat #111")
def page(w, h, body, k=0):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}
*{{box-sizing:border-box}}body{{margin:0;width:{w}px;height:{h}px;{bgcss(k)};color:#fff;font-family:'DM Sans';overflow:hidden;{'text-shadow:0 2px 14px rgba(0,0,0,.55)' if PH else ''}}}
.card{{backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px)}}
.b{{font-family:'Baloo 2'}} .pill{{background:{SUN};color:{INK};font-weight:700;font-size:26px;letter-spacing:.08em;padding:12px 24px;border-radius:999px;align-self:flex-start}}
.logo{{width:160px;height:160px;border-radius:30px}}
</style></head><body>{body}</body></html>"""

def header():
    return f'<div style="display:flex;justify-content:space-between;align-items:flex-start"><span class="pill">{E(S["tag"]).upper()}</span><img class="logo" src="{LOGO}"></div>'

NP = len(S["points"])
PT = S.get("points_title")
def points(size):
    if NP > 3: size = int(size * 0.84)
    head = f'<span class="b" style="font-weight:800;font-size:{int(size*1.5)}px;line-height:1;color:{SUN2}">{E(PT)}</span>' if PT else ""
    return head + "".join(f'<div style="display:flex;gap:22px;align-items:center">{CHECK}<span style="font-size:{size}px;font-weight:500;line-height:1.25">{E(p)}</span></div>' for p in S["points"])

def footer():
    return (f'<div style="display:flex;justify-content:space-between;align-items:center;border-top:2px solid {'rgba(255,255,255,.28)' if PH else INK2};padding-top:28px">'
            f'<span class="b" style="font-weight:700;font-size:40px">www.urbook.co.uk</span>'
            f'<span style="border:3px solid {SUN2};color:{SUN2};font-weight:700;font-size:28px;padding:10px 22px;border-radius:14px;{'background:rgba(8,12,18,.55)' if PH else ''}">URFIRST10 · £10 off</span></div>')

def col(w, h, pad, inner, gap=40):
    return f'<div style="width:{w}px;height:{h}px;padding:{pad};display:flex;flex-direction:column;gap:{gap}px">{inner}</div>'

news_label = S.get("news_label", "TRAVEL NEWS TODAY")
news_card = (f'<div class="card" style="background:{CARD};border-radius:26px;padding:30px 34px;border-top:8px solid {SUN};display:flex;flex-direction:column;gap:10px">'
             f'<span style="font-size:22px;font-weight:700;letter-spacing:.12em;color:{SUN2}">{E(news_label)}</span>'
             f'<span style="font-size:30px;line-height:1.35">{E(S["news"])}</span></div>')
CH = bool(S.get("challenge")) and bool(S.get("question"))
QL = len(S.get("question") or "")
def qcard(size):
    if not CH: return ""
    if QL > 160: size = int(size * 0.82)
    if QL > 240: size = int(size * 0.85)
    return (f'<div class="card" style="background:{CARD};border-radius:26px;padding:30px 34px;border-left:10px solid {SUN};display:flex;flex-direction:column;gap:14px">'
            f'<span style="font-size:{int(size*0.5)}px;font-weight:700;letter-spacing:.12em;color:{SUN2}">TODAY\'S CHALLENGE</span>'
            f'<span style="font-size:{size}px;font-weight:500;line-height:1.3">{E(S["question"])}</span>'
            f'<span style="font-size:{int(size*0.6)}px;font-weight:500;color:{SUN2};line-height:1.3">Comment your answer &middot; correct answers can win a &pound;50 urbook voucher &middot; T&amp;Cs in caption</span></div>')
hook = (f'<div style="display:flex;flex-direction:column;gap:14px"><span class="b" style="font-weight:800;font-size:{{s}}px;line-height:.95">{E(S["hook"])}</span>'
        f'<span class="b" style="font-weight:700;font-size:{{s2}}px;line-height:1;color:{SUN2}">{E(S["hook2"])}</span></div>')

pages = {
 "feed": (1080, 1350, col(1080, 1350, "64px 72px", header() + hook.format(s=84, s2=54) +
          f'<div style="display:flex;flex-direction:column;flex-grow:1;justify-content:center">{qcard(38)}</div>' + footer(), 26)) if CH else
         (1080, 1350, col(1080, 1350, "64px 72px", header() + hook.format(s=104 if NP<=3 else 88, s2=64 if NP<=3 else 54) + news_card +
          f'<div style="display:flex;flex-direction:column;gap:22px;flex-grow:1;justify-content:center">{points(34 if NP<=3 else 32)}</div>' + footer(), 26 if NP>3 else 30)),
 "v1": (1080, 1920, col(1080, 1920, "120px 80px 160px", header() +
        f'<div style="flex-grow:1;display:flex;flex-direction:column;justify-content:center;gap:44px">{hook.format(s=120 if CH else 150, s2=80 if CH else 96)}{qcard(46)}</div>')),
 "v2": (1080, 1920, col(1080, 1920, "120px 80px 160px", header() +
        f'<div style="flex-grow:1;display:flex;flex-direction:column;justify-content:center;gap:30px"><span class="b" style="font-weight:800;font-size:84px;line-height:1">What\'s new</span>{news_card}</div>')),
 "v3": (1080, 1920, col(1080, 1920, "120px 80px 160px", header() +
        f'<div style="flex-grow:1;display:flex;flex-direction:column;justify-content:center;gap:40px">{points(46)}</div>')),
 "v4": (1080, 1920, f'<div style="width:1080px;height:1920px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:56px;text-align:center">'
        f'<img src="{LOGO}" style="width:380px;height:380px;border-radius:64px">'
        f'<span class="b" style="font-weight:800;font-size:76px">www.urbook.co.uk</span>'
        f'<span style="font-size:38px;color:{PALE}">Parking · Transfers · Holidays — one booking place</span>'
        f'<div style="background:{SUN2};color:{INK};border-radius:28px;padding:34px 56px;display:flex;flex-direction:column;gap:6px">'
        f'<span class="b" style="font-weight:800;font-size:92px;line-height:1">URFIRST10</span><span style="font-size:34px;font-weight:700">£10 off your first booking</span></div></div>'),
}

with sync_playwright() as p:
    b = p.chromium.launch()
    for k, (name, (w, h, body)) in enumerate(pages.items()):
        pg = b.new_page(viewport={"width": w, "height": h})
        hp=os.path.abspath(f"{out}/_{name}.html"); open(hp,"w").write(page(w, h, body, {"feed":0,"v1":0,"v2":1,"v3":2,"v4":3}[name])); pg.goto("file://"+hp); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(500); os.remove(hp) if False else None
        pg.screenshot(path=f"{out}/{name}.png"); pg.close(); os.remove(hp)
    b.close()

d = S["date"]
os.replace(f"{out}/feed.png", f"{out}/urbook-{d}-post.png")
os.replace(f"{out}/v1.png", f"{out}/urbook-{d}-story.png")
# vertical video: 4 slides x 4s with gentle zoom + crossfades, silent (add a trending sound in-app)
inputs, filt = [], []
F = 7 if CH else 4  # first slide seconds (challenge: time to read the question)
for i in range(4):
    img = f"{out}/urbook-{d}-story.png" if i == 0 else f"{out}/v{i+1}.png"
    L = (F if i == 0 else 4) + 0.5
    inputs += ["-loop", "1", "-t", f"{L}", "-i", img]
    filt.append(f"[{i}:v]scale=1188:2112,zoompan=z='min(zoom+0.0006,1.06)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={int(L*30)}:s=1080x1920:fps=30,setsar=1,format=yuv420p[s{i}]")
filt.append(f"[s0][s1]xfade=transition=fade:duration=0.5:offset={F}[a];[a][s2]xfade=transition=slideleft:duration=0.5:offset={F+4}[b2];[b2][s3]xfade=transition=fade:duration=0.5:offset={F+8}[v]")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *inputs, "-f", "lavfi", "-t", f"{F+12.5}", "-i", "anullsrc=r=44100:cl=stereo",
                "-filter_complex", ";".join(filt), "-map", "[v]", "-map", "4:a", "-c:v", "libx264", "-preset", "medium", "-crf", "20",
                "-c:a", "aac", "-shortest", "-movflags", "+faststart", f"{out}/urbook-{d}-video.mp4"], check=True)
for i in (2, 3, 4): os.remove(f"{out}/v{i}.png")
print("done", os.listdir(out))
