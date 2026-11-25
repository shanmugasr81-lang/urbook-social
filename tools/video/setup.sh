#!/usr/bin/env bash
# urbook video toolkit – install + verify (Remotion, HyperFrames, FFmpeg, Whisper, yt-dlp). Safe to re-run.
# Usage: bash tools/video/setup.sh        (≈1–2 min; prints a PASS/FAIL line per tool)
set -u
cd "$(dirname "$0")"
CH="$(python3 -c 'from playwright.sync_api import sync_playwright as s; p=s().start(); print(p.chromium.executable_path); p.stop()' 2>/dev/null || true)"
export URBOOK_CHROME="$CH" PUPPETEER_EXECUTABLE_PATH="$CH" CHROME_PATH="$CH"
pip install --break-system-packages -q faster-whisper yt-dlp >/dev/null 2>&1
(cd remotion && npm install --silent --no-audit --no-fund >/dev/null 2>&1)
ok(){ echo "PASS  $1"; }; bad(){ echo "FAIL  $1 – $2"; }
T=$(mktemp -d)
# 1 FFmpeg
ffmpeg -loglevel error -y -f lavfi -i testsrc2=s=1080x1920:r=30:d=1 -c:v libx264 -pix_fmt yuv420p "$T/ff.mp4" && ok "FFmpeg $(ffmpeg -version | head -1 | cut -d' ' -f3)" || bad FFmpeg "render failed"
# 2 Remotion
(cd remotion && timeout 240 npx remotion render src/index.jsx StoryReel "$T/rm.mp4" --props=sample-props.json --browser-executable="$CH" --frames=0-29 --log=error >/dev/null 2>&1) && [ -s "$T/rm.mp4" ] && ok "Remotion $(node -p "require('./remotion/node_modules/remotion/package.json').version")" || bad Remotion "render failed (Chrome: ${CH:-none})"
# 3 HyperFrames
(cd "$T" && npx -y hyperframes@0.9 init hf --example=blank --non-interactive --skip-transcribe >/dev/null 2>&1 && cd hf && timeout 240 npx -y hyperframes@0.9 render . -o "$T/hf.mp4" -q draft -w 1 >/dev/null 2>&1) && [ -s "$T/hf.mp4" ] && ok "HyperFrames 0.9" || bad HyperFrames "render failed"
# 4 Whisper (faster-whisper). Model must be local: models/whisper/<name>/ (Hugging Face is blocked in the cloud).
python3 -c "import faster_whisper" 2>/dev/null || bad Whisper "faster-whisper not installed"
M=$(ls -d ../../models/whisper/*/ 2>/dev/null | head -1)
if [ -n "$M" ]; then python3 -c "from faster_whisper import WhisperModel as W; W('$M',device='cpu',compute_type='int8')" >/dev/null 2>&1 && ok "Whisper (model ${M#../../})" || bad Whisper "model at $M did not load"
else echo "WAIT  Whisper – installed, but no model in models/whisper/ yet (see tools/video/README.md)"; fi
# 5 yt-dlp (installed only; own-content rule – see README)
yt-dlp --version >/dev/null 2>&1 && ok "yt-dlp $(yt-dlp --version) (urbook-owned content only)" || bad yt-dlp "not installed"
rm -rf "$T"
