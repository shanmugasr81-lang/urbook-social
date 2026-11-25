#!/usr/bin/env python3
"""urbook story reel builder (25 Nov 2026).

  python3 tools/video/make_reel.py reels/specs/<name>.json            # voice + render + share copy + .srt
  python3 tools/video/make_reel.py reels/specs/<name>.json --no-render # voice + props only

Spec JSON = StoryReel props plus:
  "name": "ebc-day4",            output name
  "voice": "bm_george",          Kokoro British voice (bf_alice bf_emma bf_isabella bf_lily bm_daniel bm_fable bm_george bm_lewis)
  "speed": 1.0,
  "offer": "first" | "returning" | {chip, end}   (codes from the urbook offer rules)
  scene "say": the line spoken over that scene (scene is lengthened to fit it).
Media paths are relative to the repo root (copied into remotion/public/ for the render).
Voice is synthetic (Kokoro-82M, Apache-2.0) -> tick the platform's AI-generated label when posting.
"""
import json, os, re, shutil, subprocess, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
RM = os.path.join(ROOT, 'tools/video/remotion'); PUB = os.path.join(RM, 'public'); OUT = os.path.join(RM, 'out')
MODELS = os.path.join(ROOT, 'models/kokoro')
OFFERS = {
  'first': {'chip': '£10 off your first booking · URFIRST10', 'end': 'First booking? £10 off with URFIRST10'},
  'returning': {'chip': 'Welcome back · £5 off with URBACK5', 'end': 'Booked before? £5 off with URBACK5'},
}
CHROME = os.environ.get('URBOOK_CHROME') or next((p for p in [
  '/opt/pw-browsers/chromium-1243/chrome-linux64/chrome'] if os.path.exists(p)), None)

def pub(path):
    """copy a repo file into public/ and return its public-relative name"""
    if not path or path.startswith('http'): return path
    src = path if os.path.isabs(path) else os.path.join(ROOT, path)
    if not os.path.exists(src): src = os.path.join(PUB, path)
    if not os.path.exists(src): sys.exit(f'missing media: {path}')
    name = os.path.basename(src); dst = os.path.join(PUB, name)
    if os.path.abspath(src) != os.path.abspath(dst): shutil.copy2(src, dst)
    return name

def speak(scenes, name, voice, speed):
    import soundfile as sf
    from kokoro_onnx import Kokoro
    k = Kokoro(os.path.join(MODELS, 'kokoro-v1.0.onnx'), os.path.join(MODELS, 'voices-v1.0.bin'))
    os.makedirs(os.path.join(PUB, 'vo', name), exist_ok=True)
    for i, s in enumerate(scenes):
        if not s.get('say'): continue
        spoken = s.get('spoken', s['say'])  # spoken text can spell numbers out ("three thousand…")
        a, sr = k.create(spoken, voice=s.get('voice_name', voice), speed=speed, lang='en-gb')
        rel = f'vo/{name}/{i:02d}.wav'; sf.write(os.path.join(PUB, rel), a, sr)
        s['voice'] = rel; s['seconds'] = round(max(s.get('seconds', 0), len(a) / sr + 0.35), 2)

def srt(scenes, path):
    t, n, lines = 0.0, 1, []
    f = lambda x: f'{int(x//3600):02d}:{int(x%3600//60):02d}:{int(x%60):02d},{int(round(x%1*1000)):03d}'
    for s in scenes:
        txt = s.get('say') or s.get('caption') or s.get('hook')
        if txt: lines += [str(n), f'{f(t)} --> {f(t + s["seconds"] - 0.05)}', txt, '']; n += 1
        t += s['seconds']
    open(path, 'w').write('\n'.join(lines))

def main():
    spec = json.load(open(sys.argv[1])); name = spec.pop('name'); voice = spec.pop('voice', 'bm_george'); speed = spec.pop('speed', 1.0)
    for s in spec['scenes']: s['src'] = pub(s.get('src'))
    for k in ('music', 'logo'):
        if spec.get(k): spec[k] = pub(spec[k])
    spec.setdefault('logo', pub('brand/urbook-premium-logo-light.png'))
    if isinstance(spec.get('offer'), str): spec['offer'] = OFFERS[spec['offer']]
    if any(s.get('say') for s in spec['scenes']): speak(spec['scenes'], name, voice, speed)
    os.makedirs(OUT, exist_ok=True); props = os.path.join(OUT, f'{name}.json')
    json.dump(spec, open(props, 'w'), indent=1); srt(spec['scenes'], os.path.join(OUT, f'{name}.srt'))
    if '--no-render' in sys.argv: return print(props)
    raw = os.path.join(OUT, f'{name}-raw.mp4'); final = os.path.join(OUT, f'{name}.mp4')
    cmd = ['npx', 'remotion', 'render', 'src/index.jsx', 'StoryReel', raw, f'--props={props}', '--log=error']
    if CHROME: cmd.append(f'--browser-executable={CHROME}')
    subprocess.run(cmd, cwd=RM, check=True)
    # loudness to -14 LUFS (Instagram/TikTok), H.264 high, faststart
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', raw, '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11',
        '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '160k',
        '-movflags', '+faststart', final], check=True)
    os.remove(raw); print(final)

if __name__ == '__main__': main()
