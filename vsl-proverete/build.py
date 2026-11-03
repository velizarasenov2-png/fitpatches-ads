#!/usr/bin/env python3
"""Assembles the FitPatches VSL from stock clips, product stills, the voiceover and music.

    python3 build.py <workdir> <voiceover-take> [--draft]

<workdir> holds: clips/ (s<N>.mp4 and optional s<N>_4k.mp4), replace/ + replacements.json
(clips standing in for blocked Pexels shots), gfx/ (from make_graphics.py), music/,
vo/<take>.mp3 and vo/<take>.json (faster-whisper word timings of that take).
Writes <workdir>/out/fitpatches_vsl.mp4 plus timing.json and captions.ass.
"""
import difflib
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.abspath(sys.argv[1])
TAKE = sys.argv[2]
DRAFT = "--draft" in sys.argv
CAPS_ONLY = "--captions-only" in sys.argv
FPS = 30
W, H = 1080, 1920
OUT = os.path.join(WORK, "out")
SEG = os.path.join(OUT, "seg")
os.makedirs(SEG, exist_ok=True)

shots = json.load(open(os.path.join(HERE, "shots.json"), encoding="utf-8"))
repl = {}
rp = os.path.join(WORK, "replacements.json")
if os.path.exists(rp):
    for r in json.load(open(rp, encoding="utf-8")):
        repl[str(r["n"])] = r


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        print(" ".join(cmd))
        print(r.stderr[-3000:])
        raise SystemExit(1)
    return r.stdout


def probe(path):
    out = run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
               "stream=width,height:format=duration", "-of", "json", path])
    j = json.loads(out)
    return j["streams"][0]["width"], j["streams"][0]["height"], float(j["format"]["duration"])


# ---------------------------------------------------------------- alignment
def norm(w):
    return re.sub(r"[^0-9a-zа-яѝ]", "", w.lower().replace("ё", "е"))


tokens = []  # (text, shot_index)
for i, s in enumerate(shots):
    for t in s["vo"].split():
        tokens.append([t, i])
# glue lone dashes/quotes to the previous token
glued = []
for t in tokens:
    if not norm(t[0]) and glued:
        glued[-1][0] += " " + t[0]
    else:
        glued.append(t)
tokens = glued

words = []
for seg in json.load(open(os.path.join(WORK, "vo", TAKE + ".json"), encoding="utf-8")):
    for w in seg["words"]:
        words.append((w["w"], w["s"], w["e"]))
a = [norm(t[0]) for t in tokens]
b = [norm(w[0]) for w in words]
times = [None] * len(tokens)
sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
matched = 0
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == "equal":
        for k in range(i2 - i1):
            times[i1 + k] = (words[j1 + k][1], words[j1 + k][2])
            matched += 1
    elif tag == "replace":
        # spread the recognised span over the script span (numbers, merged words)
        s0, e0 = words[j1][1], words[j2 - 1][2]
        n = i2 - i1
        for k in range(n):
            times[i1 + k] = (s0 + (e0 - s0) * k / n, s0 + (e0 - s0) * (k + 1) / n)
print(f"aligned {matched}/{len(tokens)} script words exactly")
# fill gaps by interpolation
for i in range(len(times)):
    if times[i] is None:
        j = i - 1
        while j >= 0 and times[j] is None:
            j -= 1
        k = i + 1
        while k < len(times) and times[k] is None:
            k += 1
        t0 = times[j][1] if j >= 0 else 0.0
        t1 = times[k][0] if k < len(times) else t0 + 0.5
        n = k - j
        times[i] = (t0 + (t1 - t0) * (i - j) / n - 0.01, t0 + (t1 - t0) * (i - j + 1) / n - 0.02)

audio_dur = float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                       os.path.join(WORK, "vo", TAKE + ".mp3")]).strip())
TAIL = 1.6
total = audio_dur + TAIL

first_tok = {}
for idx, (t, si) in enumerate(tokens):
    first_tok.setdefault(si, idx)
starts = []
for si in range(len(shots)):
    st = 0.0 if si == 0 else max(0.0, times[first_tok[si]][0] - 0.08)
    starts.append(st)
frames = [round(s * FPS) for s in starts] + [round(total * FPS)]
for si, s in enumerate(shots):
    s["t0"] = frames[si] / FPS
    s["frames"] = frames[si + 1] - frames[si]
    s["dur"] = s["frames"] / FPS
short = [(s["n"], round(s["dur"], 2)) for s in shots if s["dur"] < 0.6]
if short:
    print("very short shots:", short)


# ---------------------------------------------------------------- segments
def clip_path(key):
    p4 = os.path.join(WORK, "clips", key + "_4k.mp4")
    if os.path.exists(p4):
        return p4
    return os.path.join(WORK, "clips", key + ".mp4")


def resolve(s):
    """-> (kind, path, cx, start_frac)"""
    src = s["src"]
    if src.startswith("REPL"):
        n = src.split(":")[1] if ":" in src else s["n"]
        r = repl.get(str(n))
        if not r:
            return ("missing", None, 0.5, 0.2)
        cx = {"left": 0.35, "right": 0.65}.get(r.get("crop_hint", "center"), 0.5)
        if isinstance(r.get("crop_hint"), (int, float)):
            cx = r["crop_hint"]
        cx = s.get("cx", cx)
        path = r["local_file"] if os.path.isabs(r["local_file"]) else os.path.join(WORK, r["local_file"])
        if s["src"].startswith("REPL:"):  # a repeat: use a later part of the clip
            return ("clip", path, cx, None if r.get("best_start_sec") is None else -1)
        return ("clip", path, cx, ("abs", r.get("best_start_sec", 0)))
    if src.startswith("still_"):
        return ("still", os.path.join(WORK, "gfx", src + ".png"), s.get("cx", 0.5), 0)
    return ("clip", clip_path(src), s.get("cx", 0.5), s.get("start", 0.2))


ENC = ["-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-pix_fmt", "yuv420p",
       "-r", str(FPS), "-an"]
seg_files = []
for s in ([] if CAPS_ONLY else shots):
    kind, path, cx, st = resolve(s)
    out = os.path.join(SEG, f"seg_{s['n']}.mp4")
    seg_files.append(out)
    D = s["dur"]
    nfr = s["frames"]
    fx = s.get("fx", [])
    ov = s.get("overlay")
    cmd = ["ffmpeg", "-v", "error", "-y"]
    if kind == "missing":
        cmd += ["-f", "lavfi", "-i", f"color=c=0x333333:s={W}x{H}:r={FPS}:d={D}",
                "-vf", f"drawtext=text='{s['n']} MISSING':fontcolor=white:fontsize=60:x=(w-tw)/2:y=300"]
    elif kind == "still":
        zoom = "1.0+0.07*t/{0}".format(max(D, 0.1))
        if "focus" in fx:
            blur = os.path.join(WORK, "gfx", os.path.basename(path).replace(".png", "_blur.png"))
            cmd += ["-loop", "1", "-t", f"{D}", "-i", blur, "-loop", "1", "-t", f"{D}", "-i", path]
            fc = (f"[0:v]scale={W}:{H},format=yuv420p,setsar=1[a];[1:v]scale={W}:{H},format=yuv420p,setsar=1[b];"
                  f"[a][b]blend=all_expr='A*(1-min(1,T/0.9))+B*min(1,T/0.9)'[v]")
        else:
            cmd += ["-loop", "1", "-t", f"{D}", "-i", path]
            fc = (f"[0:v]scale=w='trunc({W}*({zoom})/2)*2':h=-2:eval=frame,"
                  f"crop={W}:{H}:x='(in_w-{W})*{cx}':y='(in_h-{H})/2',setsar=1[v]")
        cmd += ["-filter_complex", fc, "-map", "[v]"]
    else:
        w, h, cd = probe(path)
        if isinstance(st, tuple):
            t_in = float(st[1])
        elif st == -1:
            t_in = cd * 0.55
        else:
            t_in = cd * float(st)
        speed = 1.0
        if "slow" in fx:
            speed = 1.6
        need = D / speed
        if t_in + need > cd - 0.05:
            t_in = max(0.0, cd - 0.05 - need)
        if need > cd - 0.05:
            speed = D / max(cd - 0.1, 0.5)
            need = D / speed
            t_in = 0.0
        scale_up = W / H > w / h  # source narrower than 9:16? (never in practice)
        cover = (f"scale=w='if(gt(a,{W}/{H}),-2,{W})':h='if(gt(a,{W}/{H}),{H},-2)',"
                 f"crop={W}:{H}:x='max(0,min(in_w-{W},in_w*{cx}-{W}/2))':y='(in_h-{H})/2'")
        zoom = f"scale=w='trunc({W}*(1.0+0.05*t/{max(D, 0.1)})/2)*2':h=-2:eval=frame,crop={W}:{H}"
        chain = f"setpts=(PTS-STARTPTS)*{speed:.4f},fps={FPS},{cover},{zoom}"
        if "bw" in fx:
            chain += ",hue=s=0,eq=contrast=1.08"
        chain += ",setsar=1"
        cmd += ["-ss", f"{t_in:.3f}", "-t", f"{need + 0.2:.3f}", "-i", path, "-filter_complex", f"[0:v]{chain}[v]",
                "-map", "[v]"]
    cmd += ["-frames:v", str(nfr)] + ENC + [out]
    sig = json.dumps([cmd[4:], ov], ensure_ascii=False)
    sig_file = out + ".sig"
    if os.path.exists(out) and os.path.exists(sig_file) and open(sig_file).read() == sig:
        print(f"{s['n']:>5} {s['t0']:7.2f}s {D:5.2f}s reused", flush=True)
        continue
    run(cmd)
    if ov:
        tmp = out.replace(".mp4", "_ov.mp4")
        ovp = os.path.join(WORK, "gfx", ov + ".png")
        delay = 0.15
        run(["ffmpeg", "-v", "error", "-y", "-i", out, "-loop", "1", "-t", f"{D}", "-i", ovp, "-filter_complex",
             f"[1:v]format=rgba,fade=t=in:st={delay}:d=0.2:alpha=1[o];[0:v][o]overlay=0:0:shortest=1[v]",
             "-map", "[v]", "-frames:v", str(nfr)] + ENC + [tmp])
        os.replace(tmp, out)
    with open(sig_file, "w") as f:
        f.write(sig)
    print(f"{s['n']:>5} {s['t0']:7.2f}s {D:5.2f}s {kind:6} {os.path.basename(path or '-')}", flush=True)

lst = os.path.join(OUT, "concat.txt")
with open(lst, "w") as f:
    for p in seg_files:
        f.write(f"file '{p}'\n")
video = os.path.join(OUT, "video_noaudio.mp4")
if not CAPS_ONLY:
    run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", video])

# ---------------------------------------------------------------- captions (ASS)
DISPLAY = [  # spoken spelling -> on-screen spelling for plain captions
    (r"\bФитПачес\b", "FitPatches"), (r"ел-глутамин", "L-глутамин"), (r"група Б\b", "група B"),
    (r"\bтри минути\b", "3 минути"), (r"\bтри въпроса\b", "3 въпроса"), (r"\bнад четирийсет\b", "над 40"),
    (r"\bедно евро\b", "1 евро"), (r"\bтрийсет лепенки\b", "30 лепенки"), (r"\bдва избора\b", "2 избора"),
]


def display(text):
    for pat, rep in DISPLAY:
        text = re.sub(pat, rep, text)
    return text


def ass_time(t):
    t = max(0, t)
    h = int(t // 3600)
    m = int(t % 3600 // 60)
    s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def esc(t):
    return t.replace("{", "(").replace("}", ")")


def clean_end(t):
    t = t.strip()
    t = re.sub(r"\s*—$", "", t)
    t = re.sub(r"[.,;:]+$", "", t)
    return t.strip()


chunks = []  # [token indexes, gold?, gold display text, plain prefix token count]
for si, s in enumerate(shots):
    idxs = [i for i, (_, k) in enumerate(tokens) if k == si]
    kw_rng = None
    if s.get("kw"):
        kwn = [norm(x) for x in s["kw"].split() if norm(x)]
        toks = [norm(tokens[i][0]) for i in idxs]
        for p in range(len(toks) - len(kwn) + 1):
            if toks[p:p + len(kwn)] == kwn:
                kw_rng = (idxs[p], idxs[p + len(kwn) - 1])
                break
        if kw_rng is None:
            print("keyword not found in shot", s["n"], s["kw"])
    cur = []
    i = 0
    while i < len(idxs):
        ti = idxs[i]
        if kw_rng and ti == kw_rng[0]:
            prefix = []
            # a short lead-in ("за", "Не", "с") stays on the same line, in white, before the gold word
            if cur and len(cur) <= 2 and len(" ".join(tokens[j][0] for j in cur)) <= 12 \
                    and not re.search(r"[.?!:]$", tokens[cur[-1]][0]):
                prefix, cur = cur, []
            if cur:
                chunks.append([cur, False, None, 0])
                cur = []
            span = list(range(kw_rng[0], kw_rng[1] + 1))
            chunks.append([prefix + span, True, s.get("kw_display", s["kw"]), len(prefix)])
            i += len(span)
            continue
        cur.append(ti)
        txt = " ".join(tokens[j][0] for j in cur)
        nxt_tok = tokens[idxs[i + 1]][0] if i + 1 < len(idxs) else ""
        ends = bool(re.search(r"[.,?!:;—…]$|“$", tokens[ti][0]))
        full = len(cur) >= 4 or len(txt) >= 24
        # don't leave a lone last word ("нали?", "интернет.") on its own
        if full and not ends and nxt_tok and re.search(r"[.,?!:;—…]$", nxt_tok) \
                and len(txt + " " + nxt_tok) <= 32 and not (kw_rng and idxs[i + 1] == kw_rng[0]):
            full = False
        if ends or full:
            chunks.append([cur, False, None, 0])
            cur = []
        i += 1
    if cur:
        chunks.append([cur, False, None, 0])

# merge one-word plain leftovers into the previous plain chunk of the same sentence when they fit
merged = []
for c in chunks:
    if (not c[1] and len(c[0]) == 1 and merged and not merged[-1][1]
            and not re.search(r"[.?!:]$", tokens[merged[-1][0][-1]][0])
            and tokens[merged[-1][0][-1]][1] == tokens[c[0][0]][1]
            and len(" ".join(tokens[j][0] for j in merged[-1][0] + c[0])) <= 32):
        merged[-1][0] = merged[-1][0] + c[0]
    else:
        merged.append(c)
chunks = merged

events = []
for ci, (idx, gold, disp, npre) in enumerate(chunks):
    st = times[idx[0]][0] - 0.05
    nxt = times[chunks[ci + 1][0][0]][0] - 0.05 if ci + 1 < len(chunks) else audio_dur + 0.8
    en = min(nxt, times[idx[-1]][1] + 0.6)
    if ci + 1 == len(chunks):
        en = max(en, st + 0.45)
    if gold:
        pre = clean_end(display(" ".join(tokens[j][0] for j in idx[:npre])))
        gold_txt = re.sub(r"([0-9][0-9€+,=.]*|€)", r"{\\fnMontserrat\\b1\\fs120}\1{\\rGold}", esc(disp))
        text = (esc(pre) + " " if pre else "") + r"{\rGold}" + gold_txt
    else:
        text = esc(clean_end(display(" ".join(tokens[j][0] for j in idx))))
    if not text:
        continue
    events.append((st, en, text, gold and not npre))

ass = os.path.join(OUT, "captions_preview.ass" if CAPS_ONLY else "captions.ass")
with open(ass, "w", encoding="utf-8") as f:
    f.write(f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Montserrat,96,&H00FFFFFF,&H00FFFFFF,&H50000000,&H78000000,1,0,0,0,100,100,0,0,1,4,4,2,80,80,500,1
Style: Gold,Playfair Display,136,&H004FC2E8,&H004FC2E8,&H40102030,&H78000000,1,0,0,0,100,100,0,0,1,4,5,2,70,70,490,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
""")
    for st, en, text, gold in events:
        style = "Gold" if gold else "Cap"
        anim = r"{\fad(70,40)\fscx90\fscy90\t(0,140,\fscx100\fscy100)}"
        text = text.replace(r"{\rGold}", r"{\rGold\fscx90\fscy90\t(0,140,\fscx100\fscy100)}")
        f.write(f"Dialogue: 0,{ass_time(st)},{ass_time(en)},{style},,0,0,0,,{anim}{text}\n")

if CAPS_ONLY:
    print("captions written:", ass, len(events))
    raise SystemExit

# ---------------------------------------------------------------- audio + final encode
reveal = next(s["t0"] for s in shots if s["n"] == "63")
m1 = os.path.join(WORK, "music", "m168.mp3")
m2 = os.path.join(WORK, "music", "m601.mp3")
vo = os.path.join(WORK, "vo", TAKE + ".mp3")
final = os.path.join(OUT, "fitpatches_vsl_draft.mp4" if DRAFT else "fitpatches_vsl.mp4")
fade_out_at = total - 2.0
fc = (
    f"[1:a]loudnorm=I=-16:TP=-2:LRA=9,aresample=48000[vo];"
    f"[2:a]aloop=loop=-1:size=2000000000,atrim=0:{reveal + 1.5:.2f},loudnorm=I=-31:TP=-8,afade=t=in:d=1.5,"
    f"afade=t=out:st={reveal - 0.5:.2f}:d=2.0,aresample=48000[m1];"
    f"[3:a]aloop=loop=-1:size=2000000000,atrim=0:{total - reveal + 1:.2f},loudnorm=I=-30:TP=-8,afade=t=in:d=1.2,"
    f"afade=t=out:st={total - reveal - 2.2:.2f}:d=2.2,adelay={int((reveal - 0.5) * 1000)}|{int((reveal - 0.5) * 1000)},"
    f"aresample=48000[m2];"
    f"[vo][m1][m2]amix=inputs=3:normalize=0:duration=longest,apad=whole_dur={total:.2f},atrim=0:{total:.2f},"
    f"loudnorm=I=-14:TP=-1.5:LRA=11[a];"
    f"[0:v]ass='{ass}',format=yuv420p[v]"
)
run(["ffmpeg", "-v", "error", "-y", "-i", video, "-i", vo, "-i", m1, "-i", m2, "-filter_complex", fc,
     "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "ultrafast" if DRAFT else "medium",
     "-crf", "28" if DRAFT else "21", "-profile:v", "high", "-pix_fmt", "yuv420p", "-r", str(FPS),
     "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", "-t", f"{total:.2f}", final])

json.dump([{k: s[k] for k in ("n", "vo", "t0", "dur", "src") if k in s} for s in shots],
          open(os.path.join(OUT, "timing.json"), "w"), ensure_ascii=False, indent=1)
print("done:", final, f"{total:.1f}s", f"{len(shots)} shots")
