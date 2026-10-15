"""urbook TikTok maker (15 Oct 2026): landscape YouTube video -> vertical 1080x1920 TikTok video.
The landscape video sits in the middle; above and below it is a blurred, darkened copy of the post's
first background photo (no navy bars any more – Shan, 15 Oct 2026). Without a photo it falls back to black.
Usage: python3 urbook_tiktok.py <in-landscape.mp4> <out-vertical.mp4> [background-photo.jpg]
The output is silent; add the sound bed with urbook_sound.py mux afterwards.
"""
import sys, os, subprocess, tempfile
from PIL import Image, ImageFilter, ImageEnhance

src, dst = sys.argv[1], sys.argv[2]
photo = sys.argv[3] if len(sys.argv) > 3 and os.path.exists(sys.argv[3]) else None
pad = os.path.join(tempfile.mkdtemp(), "pad.jpg")
if photo:
    im = Image.open(photo).convert("RGB")
    w, h = im.size
    s = max(1080 / w, 1920 / h)
    im = im.resize((int(w * s) + 1, int(h * s) + 1))
    l, t = (im.width - 1080) // 2, (im.height - 1920) // 2
    im = im.crop((l, t, l + 1080, t + 1920)).filter(ImageFilter.GaussianBlur(28))
    im = ImageEnhance.Brightness(im).enhance(0.55)
else:
    im = Image.new("RGB", (1080, 1920), "black")
im.save(pad, quality=90)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", pad, "-i", src, "-filter_complex",
                "[1:v]scale=1080:-2[fg];[0:v][fg]overlay=0:(H-h)/2:shortest=1,format=yuv420p",
                "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-r", "30", "-an", "-movflags", "+faststart", dst], check=True)
print("done", dst)
