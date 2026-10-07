"""Voice-locked cut of the fridge ad (Аз съм хладилникът на Ивайла).

- every shot sits on the sentence it illustrates (times from audio/transcript.json)
- subtitles use the script's own wording, timed by aligning it word-by-word to the transcript
- on-screen headlines from the script's "Надпис на екрана" column, upper third, with a soft pop-in
- music very quiet under the voice
Outputs: final_subs.mp4 / final_clean.mp4 (1080x1920) and deliver/ copies.
"""
import difflib
import json
import os
import re
import subprocess
import tempfile

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
CLIPS = os.path.join(ROOT, "clips")
VOICE = os.path.join(ROOT, "audio", "voice.mp3")  # ElevenLabs, Peter K, eleven_v3, one take
MUSIC = os.path.join(ROOT, "..", "video-ad-berberin", "audio", "piano_a.mp3")  # soft piano, reused
W, H, FPS = 720, 1280, 24
FONT_LIGHT = "/usr/share/fonts/opentype/inter/Inter-Light.otf"
MUSIC_DB = -34

# (clip, timeline start, timeline end, in-point, mode)   mode: cut | fit (stretch <= 25 %) | hold
EDL = []  # filled in edl.py after the clips are reviewed
END_CARD = None
END_T = 68.8  # start of the closing offer card

# Headlines from the script table: (start, end, text)
HEADLINES = []


def run(cmd):
    subprocess.run(cmd, check=True)


def clip_len(path):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                                 path], capture_output=True, text=True).stdout)


def segment(name, t0, t1, inp, mode, out):
    dur = round(t1 - t0, 3)
    scale = f"scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos,crop={W}:{H},setsar=1"
    src = os.path.join(CLIPS, f"{name}.mp4")
    avail = clip_len(src) - inp
    if mode == "fit" or (mode == "cut" and avail < dur - 0.02):
        factor = dur / avail
        assert factor <= 1.25, (name, factor)
        vf = f"setpts={factor:.5f}*PTS,fps={FPS},{scale}"
        src_t = avail
    elif mode == "hold":
        vf = f"fps={FPS},{scale},tpad=stop_mode=clone:stop_duration={max(0.0, dur - avail):.3f}"
        src_t = min(avail, dur)
    else:
        vf = f"fps={FPS},{scale}"
        src_t = dur
    run(["ffmpeg", "-v", "error", "-y", "-ss", f"{inp:.3f}", "-t", f"{src_t:.3f}", "-i", src,
         "-vf", vf + ",format=yuv420p", "-t", f"{dur:.3f}", "-an", "-c:v", "libx264", "-crf", "16", out])


BG = "f9e0e6"  # the photo's own pink, so the 9:16 padding is seamless


def end_card(dur, out, photo):
    """Last frame: the photo of the real patches with a slow push-in; the offer is drawn by the ASS layer."""
    src = os.path.join(ROOT, "refs", photo)
    n = int(dur * FPS) + 1
    run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-i", src, "-vf",
         f"scale={W*2}:{H*2},"
         f"zoompan=z='1+0.06*on/{n}':x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2':d={n}:s={W}x{H}:fps={FPS},"
         "fade=t=in:d=0.25,format=yuv420p", "-frames:v", str(n), "-an", "-c:v", "libx264", "-crf", "16", out])


# ---------- subtitles: script words timed by the transcript ----------

def norm(w):
    return re.sub(r"[^0-9a-zа-яѝ]", "", w.lower().replace("ъ", "ъ"))


def script_words():
    text = open(os.path.join(ROOT, "vo_script.txt")).read().replace("…", "… ").replace("ФитПачес", "Фит Пачес").replace("Три плюс две", "3 плюс 2")
    return [w for w in text.split() if norm(w)]


def timed_script_words():
    tr = json.load(open(os.path.join(ROOT, "audio", "transcript.json")))
    tw = [w for w in tr if norm(w["w"])]
    sw = script_words()
    a = [norm(w) for w in sw]
    b = [norm(w["w"]) for w in tw]
    times = [None] * len(sw)
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            for k in range(i2 - i1):
                times[i1 + k] = (tw[j1 + k]["s"], tw[j1 + k]["e"])
        elif op in ("replace", "delete") and j2 > j1:
            s0, e0 = tw[j1]["s"], tw[j2 - 1]["e"]
            n = i2 - i1
            for k in range(n):
                times[i1 + k] = (s0 + (e0 - s0) * k / n, s0 + (e0 - s0) * (k + 1) / n)
    # fill gaps (script words with no transcript counterpart) from neighbours
    for i, t in enumerate(times):
        if t is None:
            prev = next((times[j] for j in range(i - 1, -1, -1) if times[j]), (0, 0))
            times[i] = (prev[1], prev[1] + 0.2)
    return list(zip(sw, times))


def subtitle_chunks(max_chars=40):
    """One subtitle per sentence; long sentences split at commas, then at the middle word, never leaving
    a one-word tail."""
    words = timed_script_words()
    sentences, cur = [], []
    for w, t in words:
        cur.append((w, t))
        if w[-1] in ".?!…":
            sentences.append(cur)
            cur = []
    if cur:
        sentences.append(cur)

    def length(ws):
        return len(" ".join(x[0] for x in ws))

    def split_long(ws):
        if length(ws) <= max_chars or len(ws) < 4:
            return [ws]
        best = min(range(2, len(ws) - 1), key=lambda k: abs(length(ws[:k]) - length(ws[k:])))
        return split_long(ws[:best]) + split_long(ws[best:])

    chunks = []
    for sent in sentences:
        parts, cur = [], []
        for w, t in sent:
            cur.append((w, t))
            if w[-1] in ",:;":
                parts.append(cur)
                cur = []
        if cur:
            parts.append(cur)
        merged = []
        for part in parts:
            if merged and length(merged[-1] + part) <= max_chars:
                merged[-1] = merged[-1] + part
            else:
                merged.append(part)
        if len(merged) > 1 and length(merged[-1]) < 12:  # short tail joins the previous line
            tail = merged.pop()
            merged[-1] = merged[-1] + tail
        for m in merged:
            chunks.extend(split_long(m))
    out = []
    for c in chunks:
        text = " ".join(x[0] for x in c).strip().rstrip(",;:")
        out.append([c[0][1][0], c[-1][1][1], text])
    for i in range(len(out) - 1):  # keep each line until shortly before the next one
        out[i][1] = min(max(out[i][1] + 0.25, out[i][0] + 0.7), out[i + 1][0] - 0.03)
    return out


def ass_time(t):
    h, rem = divmod(max(0, t), 3600)
    m, s = divmod(rem, 60)
    return f"{int(h)}:{int(m):02d}:{s:05.2f}"


def srt_time(t):
    h, rem = divmod(max(0, t), 3600)
    m, s = divmod(rem, 60)
    return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int(round((s % 1) * 1000)):03d}"


def write_subs(tmp, with_subs=True):
    subs = subtitle_chunks()
    with open(os.path.join(ROOT, "subtitles.srt"), "w") as f:
        for i, (a, b, t) in enumerate(subs, 1):
            f.write(f"{i}\n{srt_time(a)} --> {srt_time(b)}\n{t}\n\n")
    ass = os.path.join(tmp, "subs_%d.ass" % with_subs)
    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Sub,Inter Bold,52,&H00FFFFFF,&H00FFFFFF,&H64000000,&H78000000,0,0,0,0,100,100,0,0,1,2,3,2,50,50,330,1
Style: Head,Inter ExtraBold,46,&H00FFFFFF,&H00FFFFFF,&H00874DD6,&H64000000,0,0,0,0,100,100,3,0,1,0,3,8,50,50,230,1
Style: Clock,Inter ExtraBold,110,&H00FFFFFF,&H00FFFFFF,&H00874DD6,&H64000000,0,0,0,0,100,100,2,0,1,0,4,8,50,50,200,1
Style: Offer,Inter ExtraBold,40,&H00FFFFFF,&H00FFFFFF,&H00874DD6,&H00874DD6,0,0,0,0,100,100,1,0,3,18,0,2,50,50,90,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    with open(ass, "w") as f:
        f.write(head)
        for a, b, text in HEADLINES:
            style = "Clock" if re.fullmatch(r"\d{1,2}:\d{2}", text) else "Head"
            if text.startswith("3+2"):
                style = "Offer"
            pop = r"{\fad(180,220)\fscx86\fscy86\t(0,220,\fscx100\fscy100)}"
            # a short pink bar under the headline
            f.write(f"Dialogue: 1,{ass_time(a)},{ass_time(b)},{style},,0,0,0,,{pop}{text}\n")
        if with_subs:
            for a, b, text in subs:
                if a >= END_T:  # the offer card carries its own text
                    continue
                f.write(f"Dialogue: 0,{ass_time(a)},{ass_time(b)},Sub,,0,0,0,,{text}\n")
    return ass


def main():
    from edl import EDL as edl, HEADLINES as heads, END_CARD as endc, TOTAL
    global HEADLINES
    HEADLINES = heads
    tmp = tempfile.mkdtemp()
    parts = []
    t_prev = 0.0
    for i, (name, t0, t1, inp, mode) in enumerate(edl):
        assert abs(t0 - t_prev) < 0.01, ("gap/overlap before", name, t_prev, t0)
        p = os.path.join(tmp, f"{i:03d}_{name}.mp4")
        segment(name, t0, t1, inp, mode, p)
        parts.append(p)
        t_prev = t1
    if endc:
        p = os.path.join(tmp, "999_end.mp4")
        end_card(TOTAL - t_prev, p, endc)
        parts.append(p)
    lst = os.path.join(tmp, "list.txt")
    with open(lst, "w") as f:
        f.writelines(f"file '{p}'\n" for p in parts)
    video = os.path.join(tmp, "video.mp4")
    run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", video])

    mix = os.path.join(tmp, "mix.wav")
    run(["ffmpeg", "-v", "error", "-y", "-i", VOICE, "-i", MUSIC, "-filter_complex",
         f"[0:a]aresample=48000,apad=whole_dur={TOTAL}[v];"
         f"[1:a]aresample=48000,atrim=0:{TOTAL:.2f},volume={MUSIC_DB}dB,afade=t=in:d=2,"
         f"afade=t=out:st={TOTAL - 4:.2f}:d=4[m];"
         "[v][m]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]",
         "-map", "[a]", "-ac", "2", mix])

    outs = {}
    for with_subs, name in ((True, "final_subs.mp4"), (False, "final_clean.mp4")):
        ass = write_subs(tmp, with_subs)
        out = os.path.join(ROOT, name)
        run(["ffmpeg", "-v", "error", "-y", "-i", video, "-i", mix, "-map", "0:v", "-map", "1:a",
             "-vf", f"ass={ass}", "-c:v", "libx264", "-crf", "18", "-preset", "veryfast", "-c:a", "aac",
             "-b:a", "192k", "-t", str(TOTAL), "-movflags", "+faststart", out])
        outs[with_subs] = out
    deliver = os.path.join(ROOT, "deliver")
    os.makedirs(deliver, exist_ok=True)
    for with_subs, base in ((True, "FitPatches_hladilnik_subtitri"), (False, "FitPatches_hladilnik_bez_subtitri")):
        run(["ffmpeg", "-v", "error", "-y", "-i", outs[with_subs], "-c:v", "libx264", "-preset", "veryfast",
             "-b:v", "1800k", "-maxrate", "2500k", "-bufsize", "5000k", "-c:a", "aac", "-b:a", "128k",
             "-movflags", "+faststart", os.path.join(deliver, base + "_720p.mp4")])
    print("wrote", outs, f"({TOTAL}s)")


if __name__ == "__main__":
    main()
