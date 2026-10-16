"""urbook video-clip intro (16 Oct 2026, Shan: "use the videos too, they are clear now").
Puts a few seconds of one of Shan's own clips (holiday/videos/...) IN FRONT of a rendered post video, with the urbook
logo in the corner and a soft dark scrim, then crossfades into the normal slides. The clip's own sound is never used.
Usage: python3 urbook_clip.py <rendered.mp4> <clip.mp4> <logo.png> <out.mp4> [seconds]
- Output size = the rendered video's size (1080x1920 Reel / 1920x1080 YouTube); the clip is cover-cropped, never stretched.
- Default seconds: 3.5 for a vertical video, 5 for a landscape one. The clip starts 0.5 s in.
- Output is SILENT: add the sound bed afterwards with urbook_sound.py mux.
"""
import sys, json, subprocess

src, clip, logo, dst = sys.argv[1:5]
def probe(p):
    o = json.loads(subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height:format=duration",
                                   "-of", "json", p], capture_output=True, text=True, check=True).stdout)
    return o["streams"][0]["width"], o["streams"][0]["height"], float(o["format"]["duration"])
W, H, _ = probe(src)
cw, ch, cd = probe(clip)
secs = float(sys.argv[5]) if len(sys.argv) > 5 else (3.5 if H > W else 5.0)
secs = max(2.0, min(secs, cd - 0.6))
L = int(min(W, H) * 0.13)  # logo size
f = (f"[1:v]trim=start=0.5:duration={secs:.2f},setpts=PTS-STARTPTS,scale={W}:{H}:force_original_aspect_ratio=increase,"
     f"crop={W}:{H},fps=30,setsar=1,eq=brightness=-0.04:saturation=1.08,"
     f"drawbox=x=0:y=ih*0.72:w=iw:h=ih*0.28:color=black@0.28:t=fill[c];"
     f"[2:v]scale={L}:{L},format=rgba[lg];[c][lg]overlay={int(L*0.3)}:{int(L*0.3)},format=yuv420p[ci];"
     f"[0:v]fps=30,setsar=1,format=yuv420p[r];[ci][r]xfade=transition=fade:duration=0.6:offset={secs-0.6:.2f}[v]")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-i", clip, "-i", logo, "-filter_complex", f, "-map", "[v]",
                "-an", "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-movflags", "+faststart", dst], check=True)
print("done", dst, f"{W}x{H}", f"intro {secs:.1f}s")
