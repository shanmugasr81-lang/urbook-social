#!/usr/bin/env python3
"""urbook_sound.py v1 (29 Sep 2026) - original, royalty-free soft travel sound beds for urbook videos.

Everything here is synthesised from scratch (no samples, no third-party music), so it is safe to use
on Instagram, Facebook, TikTok and YouTube without licence or Content ID claims.

Usage:
  python3 urbook_sound.py beds <outdir>                 # writes the 4 beds as .m4a (70 s each)
  python3 urbook_sound.py mux <video.mp4> <bed.m4a> <out.mp4>   # adds a bed to a video (fades in/out)
Beds:
  soft-travel      warm pad + gentle plucks (parking / transfers, everyday)
  airport-calm     terminal ambience: soft pad, airport PA chime at the start, distant jet swell
  sunrise-journey  brighter pad + soft pulse (holidays: Nepal / Sri Lanka / South India)
  lounge-evening   mellow low pad + slow bells (Park, Sleep & Fly, early flights, polls)
"""
import sys, os, subprocess
import numpy as np
from scipy.signal import butter, sosfilt

SR = 44100
DUR = 70.0

def midi(n):
    return 440.0 * 2 ** ((n - 69) / 12)

def env_adsr(n, a, r):
    e = np.ones(n)
    na, nr = int(a * SR), int(r * SR)
    na = min(na, n // 2); nr = min(nr, n // 2)
    e[:na] = np.linspace(0, 1, na) ** 2
    e[-nr:] *= np.linspace(1, 0, nr) ** 2
    return e

def lp(x, fc, order=2):
    return sosfilt(butter(order, fc, 'low', fs=SR, output='sos'), x)

def hp(x, fc, order=2):
    return sosfilt(butter(order, fc, 'high', fs=SR, output='sos'), x)

def bp(x, lo, hi, order=2):
    return sosfilt(butter(order, [lo, hi], 'band', fs=SR, output='sos'), x)

def pad_voice(f, n, rng, detune=0.25):
    t = np.arange(n) / SR
    out = np.zeros(n)
    for d in (-detune, 0, detune):
        ph = rng.uniform(0, 2 * np.pi)
        ff = f * 2 ** (d / 12 / 4)
        # soft saw-ish: a few harmonics with 1/k^1.5 roll-off
        for k in range(1, 7):
            out += np.sin(2 * np.pi * ff * k * t + ph * k) / k ** 1.5
    return out / 3

def pad(chords, seg, rng, bright=1800, oct_shift=0):
    n_total = int(DUR * SR)
    out = np.zeros(n_total)
    nseg = int(seg * SR)
    xf = int(1.5 * SR)
    i = 0; start = 0
    while start < n_total:
        ch = chords[i % len(chords)]
        n = min(nseg + xf, n_total - start)
        s = np.zeros(n)
        for m in ch:
            s += pad_voice(midi(m + 12 * oct_shift), n, rng)
        s *= env_adsr(n, 1.8, 1.8) / len(ch)
        out[start:start + n] += s
        start += nseg; i += 1
    out = lp(out, bright, 2)
    # slow tremolo-free breathing filter feel via gentle amplitude LFO
    t = np.arange(n_total) / SR
    out *= 0.85 + 0.15 * np.sin(2 * np.pi * t / 9.0)
    return out

def pluck(f, dur, rng):
    n = int(dur * SR)
    t = np.arange(n) / SR
    s = (np.sin(2 * np.pi * f * t) + 0.35 * np.sin(2 * np.pi * 2 * f * t) + 0.12 * np.sin(2 * np.pi * 3 * f * t))
    return s * np.exp(-t * 4.0) * env_adsr(n, 0.004, 0.05)

def bell(f, dur):
    n = int(dur * SR)
    t = np.arange(n) / SR
    s = (np.sin(2 * np.pi * f * t) * np.exp(-t * 1.6)
         + 0.5 * np.sin(2 * np.pi * f * 2.76 * t) * np.exp(-t * 2.8)
         + 0.25 * np.sin(2 * np.pi * f * 5.4 * t) * np.exp(-t * 4.5))
    return s * env_adsr(n, 0.003, 0.2)

def place(buf, sig, at):
    i = int(at * SR)
    if i >= len(buf):
        return
    j = min(len(buf), i + len(sig))
    buf[i:j] += sig[:j - i]

def arp_line(chords, seg, notes_per_seg, rng, level, octave=12, start_at=2.0):
    n_total = int(DUR * SR)
    out = np.zeros(n_total)
    t = start_at; i = 0
    step = seg / notes_per_seg
    while t < DUR - 2:
        ch = chords[int(t // seg) % len(chords)]
        m = ch[i % len(ch)] + octave
        place(out, pluck(midi(m), 1.6, rng) * level * rng.uniform(0.7, 1.0), t)
        t += step; i += 1
    return lp(out, 3500)

def reverb(x, amt=0.35):
    # cheap feedback-delay reverb (multi-tap, decaying)
    out = x.copy()
    for d, g in ((0.031, .5), (0.047, .45), (0.071, .4), (0.113, .35), (0.167, .3), (0.241, .25), (0.353, .2), (0.509, .15)):
        k = int(d * SR)
        y = np.zeros_like(x); y[k:] = x[:-k] * g
        out += y * amt
    return lp(out, 6000)

def noise_swell(at, dur, rng, lo=120, hi=900, level=0.25):
    n = int(dur * SR)
    t = np.linspace(0, 1, n)
    s = bp(rng.standard_normal(n), lo, hi) * np.sin(np.pi * t) ** 2 * level
    return s

def pa_chime():
    # classic three-tone "announcement" chime, original synthesis (G5, E5, C5)
    s = np.zeros(int(3.0 * SR))
    for k, m in enumerate((79, 76, 72)):
        place(s, bell(midi(m), 2.2) * 0.35, k * 0.42)
    return s

def normalise(x, peak=0.5):
    x = x - np.mean(x)
    return x / (np.max(np.abs(x)) + 1e-9) * peak

def fade(x, fin=1.5, fout=3.0):
    n = len(x)
    a, b = int(fin * SR), int(fout * SR)
    x[:a] *= np.linspace(0, 1, a)
    x[-b:] *= np.linspace(1, 0, b)
    return x

def stereo(l, r):
    return np.stack([l, r], axis=1)

def bed(name):
    rng = np.random.default_rng(abs(hash(name)) % (2 ** 32) if False else sum(map(ord, name)))
    n = int(DUR * SR)
    if name == 'soft-travel':
        ch = [[60, 64, 67, 71], [57, 60, 64, 67], [53, 57, 60, 64], [55, 59, 62, 67]]  # Cmaj7 Am7 Fmaj7 G
        p = pad(ch, 4.0, rng, 1600)
        a = arp_line(ch, 4.0, 8, rng, 0.22)
        mix = p * 0.8 + a
    elif name == 'airport-calm':
        ch = [[57, 60, 64, 69], [53, 57, 60, 65], [60, 64, 67, 72], [55, 59, 62, 67]]  # Am F C G
        p = pad(ch, 5.0, rng, 1300)
        hum = lp(rng.standard_normal(n), 300) * 0.05
        amb = np.zeros(n)
        place(amb, pa_chime(), 0.6)
        place(amb, noise_swell(0, 9, rng, 90, 700, 0.18), 18)
        place(amb, noise_swell(0, 9, rng, 90, 700, 0.15), 44)
        a = arp_line(ch, 5.0, 4, rng, 0.14, 24, 4.0)
        mix = p * 0.8 + hum + amb + a
    elif name == 'sunrise-journey':
        ch = [[62, 66, 69, 74], [59, 62, 66, 71], [55, 59, 62, 67], [57, 61, 64, 69]]  # D Bm G A
        p = pad(ch, 4.0, rng, 2200)
        t = np.arange(n) / SR
        pulse = (0.5 + 0.5 * np.sin(2 * np.pi * 2.0 * t)) ** 3
        sub = np.zeros(n); seg = int(4 * SR)
        for i in range(0, n, seg):
            f = midi(ch[(i // seg) % 4][0] - 12)
            k = min(seg, n - i)
            sub[i:i + k] = np.sin(2 * np.pi * f * np.arange(k) / SR)
        a = arp_line(ch, 4.0, 8, rng, 0.2, 12)
        mix = p * 0.75 + sub * pulse * 0.12 + a
    elif name == 'lounge-evening':
        ch = [[50, 57, 60, 64], [48, 55, 59, 64], [45, 52, 55, 60], [47, 54, 57, 62]]  # Dm9-ish Cmaj7 Am Bm7
        p = pad(ch, 6.0, rng, 1100)
        b = np.zeros(n)
        tt = 3.0; i = 0
        while tt < DUR - 3:
            m = ch[int(tt // 6.0) % 4][(i * 2) % 4] + 24
            place(b, bell(midi(m), 3.0) * 0.12, tt); tt += 3.0; i += 1
        mix = p * 0.85 + b
    else:
        raise SystemExit('unknown bed ' + name)
    mix = reverb(hp(mix, 45), 0.4)
    mix = fade(normalise(mix, 0.5))
    # gentle stereo width via tiny delay
    d = int(0.012 * SR)
    r = np.concatenate([np.zeros(d), mix[:-d]])
    return stereo(mix, 0.85 * r + 0.15 * mix)

BEDS = ['soft-travel', 'airport-calm', 'sunrise-journey', 'lounge-evening']

def write_bed(name, outdir):
    import wave
    os.makedirs(outdir, exist_ok=True)
    x = bed(name)
    wav = os.path.join(outdir, name + '.wav')
    pcm = (np.clip(x, -1, 1) * 32767).astype('<i2')
    with wave.open(wav, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
    m4a = os.path.join(outdir, name + '.m4a')
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', wav, '-af', 'loudnorm=I=-20:TP=-2:LRA=7',
                    '-ar', '44100', '-c:a', 'aac', '-b:a', '160k', m4a], check=True)
    os.remove(wav)
    return m4a

def mux(video, bedfile, out):
    dur = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
                                         '-of', 'default=nw=1:nk=1', video]).decode().strip())
    fo = max(0.0, dur - 2.0)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', video, '-i', bedfile,
                    '-filter_complex', f'[1:a]atrim=0:{dur:.3f},afade=t=in:d=0.8,afade=t=out:st={fo:.3f}:d=2,volume=1.0[a]',
                    '-map', '0:v:0', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '160k',
                    '-movflags', '+faststart', '-shortest', out], check=True)

if __name__ == '__main__':
    if len(sys.argv) >= 3 and sys.argv[1] == 'beds':
        for b in BEDS:
            print(write_bed(b, sys.argv[2]))
    elif len(sys.argv) == 5 and sys.argv[1] == 'mux':
        mux(sys.argv[2], sys.argv[3], sys.argv[4]); print(sys.argv[4])
    else:
        print(__doc__)
