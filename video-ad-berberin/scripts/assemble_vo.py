"""Final cut locked to the voice-over (audio/voice.mp3).

Every cut sits on a word boundary from audio/transcript.json (faster-whisper, word timestamps):
the shot changes 0.1-0.2 s before the sentence it illustrates, and actions inside the clips
(the look in the mirror, the glance at the bus stop, the look into the camera) land on the
matching words. Clip audio is dropped; the piano pad enters with scene 7 as in the script.

Outputs (1080x1920, 24 fps):
  final_subs.mp4     voice + piano + burned-in subtitles
  final_clean.mp4    same without subtitles
  subtitles.srt      the subtitles as a separate file
"""
import os
import subprocess
import tempfile

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
CLIPS = os.path.join(ROOT, "clips")
VOICE = os.path.join(ROOT, "audio", "voice.mp3")
PIANO = os.path.join(ROOT, "audio", "piano_a.mp3")
W, H, FPS = 1080, 1920, 24
FONT_LIGHT = "/usr/share/fonts/opentype/inter/Inter-Light.otf"

# (clip, timeline start, timeline end, in-point in clip, mode)
# mode: "cut" plays at normal speed; "fit" time-stretches the clip to the slot (<= 15 %);
#       "hold" plays at normal speed and holds the last frame for the rest of the slot.
EDL = [
    ("S01L_b", 0.00, 8.45, 0.0, "cut"),    # "Никой няма да ти го каже…" / look in the mirror on "А как изглеждаш?"
    ("S02", 8.45, 15.60, 0.0, "cut"),      # young woman passes on "Виждаш го в погледите…"
    ("S03a", 15.60, 21.75, 0.0, "fit"),    # "След четиридесет… Захарта. Налягането. Умората."
    ("S03b", 21.75, 27.90, 0.0, "fit"),    # "Лекарят каза…" walks out, reads, folds the paper away
    ("S04b", 27.90, 28.80, 1.0, "cut"),    # "Диети,"
    ("S04c", 28.80, 29.65, 2.4, "cut"),    # "фитнес,"
    ("S04d", 29.65, 32.45, 0.2, "cut"),    # "хапчета, всичко работеше две седмици." pushes the box away
    ("S04a", 32.45, 36.05, 0.4, "cut"),    # "После тялото връщаше всичко, с лихвата." on the scale
    ("S05", 36.05, 47.55, 0.0, "fit"),     # "Една вечер попаднах на статия…" phone closer on "И че има лепенка"
    ("S06a", 47.55, 52.30, 0.0, "cut"),    # "Лепенка. Честно, изсмях се…" phone down, stands, walks off
    ("S06b", 52.30, 57.45, 0.8, "cut"),    # "Но прочетох как работи…" picks the phone up again
    ("S07b", 57.45, 63.75, 0.0, "fit"),    # "Берберинът помага… вместо да я складира като мазнина."
    ("S07a", 63.75, 68.30, 0.5, "cut"),    # "Лепенката го пуска бавно, през кожата…"
    ("S07c", 68.30, 74.00, 0.0, "hold"),   # "Не ти казва какво да ядеш. Променя…"
    ("S08", 74.00, 80.00, 0.0, "cut"),     # "Нямах какво да губя. Поръчах един пакет…"
    ("CARD", 80.00, 81.85, 0.0, "card"),   # "Един месец по-късно" in the silence
    ("S09a", 81.85, 85.45, 0.0, "cut"),    # "Един месец по-късно. Не е чудо. Блузата стои различно."
    ("S09b", 85.45, 89.75, 0.5, "cut"),    # "Сутрин не съм подута. Лекарят погледна захарта…"
    ("S09c", 89.75, 94.10, 0.0, "cut"),    # "За първи път от петнадесет години…" + pause
    ("S10", 94.10, 101.30, 0.0, "cut"), # hand opens the door; look into the camera on "Аз също не вярвах."
    ("END", 101.30, 103.60, 0.0, "end"),   # "Виж как работят →" on "…ако искаш да прочетеш как работи."
]
TOTAL = EDL[-1][2]
FADE = 0.35
# picture fades into and out of the two black cards; every other change is a straight cut
FADE_OUT = {"S08", "S10"}
FADE_IN = {"S09a"}
MUSIC_IN = 57.45
ANIM_START, ANIM_END = 57.45, 74.00

# Subtitles: what the voice actually says, spelled correctly, one sentence (or half of a long one) each.
SUBS = [
    (0.60, 2.40, "Никой няма да ти го каже в лицето."),
    (2.90, 4.62, "Но първото, което хората виждат,"),
    (4.95, 5.65, "не е кой си."),
    (7.40, 8.45, "А как изглеждаш."),
    (8.50, 9.20, "Аз го знаех."),
    (9.65, 10.95, "Никой не ми го е казвал."),
    (11.25, 12.60, "Виждаш го в погледите,"),
    (12.62, 14.75, "които траят половин секунда по-дълго."),
    (15.70, 16.62, "След четиридесет"),
    (16.64, 18.05, "вече не беше за външния вид."),
    (18.45, 21.45, "Захарта. Налягането. Умората."),
    (21.95, 24.15, "Лекарят каза: „Трябва да отслабнете.“"),
    (24.70, 27.05, "Сякаш не бях опитвала петнадесет години."),
    (28.00, 28.86, "Диети."),
    (28.88, 29.72, "Фитнес."),
    (29.74, 30.40, "Хапчета."),
    (30.65, 32.30, "Всичко работеше две седмици."),
    (32.60, 34.42, "После тялото връщаше всичко."),
    (34.45, 35.15, "С лихвата."),
    (36.65, 38.30, "Една вечер попаднах на статия."),
    (38.60, 40.10, "Казваше, че след четиридесет"),
    (40.12, 41.85, "проблемът не са калориите,"),
    (41.90, 43.85, "а как тялото обработва захарта."),
    (44.15, 45.45, "И че има лепенка,"),
    (45.47, 47.05, "която действа точно на това."),
    (47.70, 48.40, "Лепенка."),
    (48.80, 49.75, "Честно, изсмях се."),
    (50.10, 52.05, "След всичко, което бях пробвала."),
    (52.40, 53.60, "Но прочетох как работи."),
    (53.85, 55.50, "И нещо ми направи впечатление."),
    (57.60, 59.15, "Берберинът помага на тялото"),
    (59.17, 61.30, "да усвоява захарта от храната,"),
    (61.35, 63.30, "вместо да я складира като мазнина."),
    (63.95, 65.58, "Лепенката го пуска бавно,"),
    (65.60, 68.15, "през кожата, двадесет и четири часа."),
    (68.45, 69.95, "Не ти казва какво да ядеш."),
    (70.15, 72.30, "Променя какво тялото прави с яденето."),
    (74.10, 75.20, "Нямах какво да губя."),
    (75.65, 76.65, "Поръчах един пакет."),
    (77.10, 78.30, "Ако не стане,"),
    (78.32, 79.25, "няма да е първият път."),
    (81.90, 83.35, "Един месец по-късно."),
    (83.40, 84.15, "Не е чудо."),
    (84.25, 85.50, "Блузата стои различно."),
    (85.55, 86.65, "Сутрин не съм подута."),
    (87.15, 88.42, "Лекарят погледна захарта"),
    (88.44, 89.65, "и попита какво правя."),
    (89.85, 91.88, "За първи път от петнадесет години"),
    (91.90, 93.20, "имах какво да му отговоря."),
    (96.70, 97.95, "Не ти казвам да ми вярваш."),
    (98.20, 99.35, "Аз също не вярвах."),
    (99.40, 100.46, "Линкът е отдолу,"),
    (100.48, 102.25, "ако искаш да прочетеш как работи."),
]


def run(cmd):
    subprocess.run(cmd, check=True)


def clip_len(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                         capture_output=True, text=True).stdout
    return float(out)


def text_vf(text, size, dur):
    t = text.replace(":", r"\:").replace("'", r"\'")
    alpha = f"if(lt(t,{FADE}),t/{FADE},if(gt(t,{dur - FADE:.3f}),({dur:.3f}-t)/{FADE},1))"
    return (f"drawtext=fontfile={FONT_LIGHT}:text='{t}':fontcolor=white:fontsize={size}:"
            f"alpha='{alpha}':x=(w-text_w)/2:y=(h-text_h)/2")


def segment(name, t0, t1, inp, mode, out):
    dur = round(t1 - t0, 3)
    scale = f"scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos,crop={W}:{H},setsar=1"
    silent = ["-f", "lavfi", "-t", f"{dur:.3f}", "-i", "anullsrc=r=48000:cl=stereo"]
    enc = ["-c:v", "libx264", "-crf", "16", "-c:a", "pcm_s16le", "-t", f"{dur:.3f}"]
    if mode in ("card", "end"):
        text = "Един месец по-късно" if mode == "card" else "Виж как работят →"
        size = 56 if mode == "card" else 76
        run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", f"color=black:s={W}x{H}:r={FPS}:d={dur}"] + silent +
            ["-map", "0:v", "-map", "1:a", "-vf", text_vf(text, size, dur) + ",format=yuv420p"] + enc + [out])
        return
    src = os.path.join(CLIPS, f"{name}.mp4")
    avail = clip_len(src) - inp
    fades = []
    if name in FADE_IN:
        fades.append(f"fade=t=in:st=0:d={FADE}")
    if name in FADE_OUT:
        fades.append(f"fade=t=out:st={dur - FADE:.3f}:d={FADE}")
    afade = f"afade=t=in:d=0.08,afade=t=out:st={dur - 0.12:.3f}:d=0.12"
    if mode == "fit":
        factor = dur / avail
        assert factor <= 1.16, (name, factor)
        vf = f"setpts={factor:.5f}*PTS,fps={FPS},{scale}"
        af = f"atempo={1 / factor:.5f},"
        src_t = avail
    elif mode == "hold":
        vf = f"fps={FPS},{scale},tpad=stop_mode=clone:stop_duration={max(0.0, dur - avail):.3f}"
        af = None  # animation: no room sound, the piano carries it
        src_t = min(avail, dur)
    else:
        assert avail >= dur - 0.02, (name, avail, dur)
        vf = f"fps={FPS},{scale}"
        af = ""
        src_t = dur
    vf = ",".join([vf] + fades + ["format=yuv420p"])
    if af is None or name.startswith("S07"):
        cmd = ["ffmpeg", "-v", "error", "-y", "-ss", str(inp), "-t", f"{src_t:.3f}", "-i", src] + silent + \
              ["-map", "0:v", "-map", "1:a", "-vf", vf] + enc + [out]
    else:
        cmd = ["ffmpeg", "-v", "error", "-y", "-ss", str(inp), "-t", f"{src_t:.3f}", "-i", src,
               "-vf", vf, "-af", f"{af}aresample=48000,{afade},apad", "-ac", "2"] + enc + [out]
    run(cmd)


def srt_time(t):
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int(round((s % 1) * 1000)):03d}"


def ass_time(t):
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    return f"{int(h)}:{int(m):02d}:{s:05.2f}"


def write_subs(tmp):
    srt = os.path.join(ROOT, "subtitles.srt")
    with open(srt, "w") as f:
        for i, (a, b, text) in enumerate(SUBS, 1):
            f.write(f"{i}\n{srt_time(a)} --> {srt_time(b)}\n{text}\n\n")
    ass = os.path.join(tmp, "subs.ass")
    # White, no box; a soft shadow keeps it readable on the light hallway shots. Lower third.
    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Sub,Inter Bold,76,&H00FFFFFF,&H00FFFFFF,&H50000000,&H70000000,0,0,0,0,100,100,0,0,1,1.8,3,2,80,80,500,1
Style: SubDark,Inter Bold,76,&H00262A2E,&H00262A2E,&H00262A2E,&H00000000,0,0,0,0,100,100,0,0,1,0,0,2,80,80,150,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    with open(ass, "w") as f:
        f.write(head)
        for a, b, text in SUBS:
            # dark text on the cream illustration background of scene 7, white everywhere else
            style = "SubDark" if ANIM_START <= a < ANIM_END else "Sub"
            f.write(f"Dialogue: 0,{ass_time(a)},{ass_time(b)},{style},,0,0,0,,{text}\n")
    return srt, ass


def main():
    tmp = tempfile.mkdtemp()
    parts = []
    for i, (name, t0, t1, inp, mode) in enumerate(EDL):
        p = os.path.join(tmp, f"{i:02d}_{name}.mov")
        segment(name, t0, t1, inp, mode, p)
        parts.append(p)
    lst = os.path.join(tmp, "list.txt")
    with open(lst, "w") as f:
        f.writelines(f"file '{p}'\n" for p in parts)
    video = os.path.join(tmp, "video.mp4")
    run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", video + ".mov"])
    run(["ffmpeg", "-v", "error", "-y", "-i", video + ".mov", "-map", "0:v", "-c", "copy", video])
    amb = os.path.join(tmp, "ambience.wav")
    run(["ffmpeg", "-v", "error", "-y", "-i", video + ".mov", "-map", "0:a", "-c:a", "pcm_s16le", amb])

    # voice at full level; piano very quiet under it from scene 7, fading in and out
    mix = os.path.join(tmp, "mix.wav")
    music_len = TOTAL - MUSIC_IN
    run(["ffmpeg", "-v", "error", "-y", "-i", VOICE, "-i", PIANO, "-i", amb, "-filter_complex",
         f"[0:a]aresample=48000,apad=whole_dur={TOTAL}[v];"
         f"[1:a]aresample=48000,atrim=0:{music_len:.2f},volume=-34dB,afade=t=in:d=3,"
         f"afade=t=out:st={music_len - 2.5:.2f}:d=2.5,adelay={int(MUSIC_IN * 1000)}:all=1[m];"
         "[2:a]aresample=48000,volume=1dB[r];"
         "[v][m][r]amix=inputs=3:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]",
         "-map", "[a]", "-ac", "2", mix])

    srt, ass = write_subs(tmp)
    clean = os.path.join(ROOT, "final_clean.mp4")
    run(["ffmpeg", "-v", "error", "-y", "-i", video, "-i", mix, "-map", "0:v", "-map", "1:a", "-c:v", "copy",
         "-c:a", "aac", "-b:a", "192k", "-t", str(TOTAL), "-movflags", "+faststart", clean])
    subs = os.path.join(ROOT, "final_subs.mp4")
    run(["ffmpeg", "-v", "error", "-y", "-i", video, "-i", mix, "-map", "0:v", "-map", "1:a",
         "-vf", f"ass={ass}", "-c:v", "libx264", "-crf", "18", "-preset", "slow", "-c:a", "aac", "-b:a", "192k",
         "-t", str(TOTAL), "-movflags", "+faststart", subs])
    # delivery copies: 1080p under 30 MB for download, 720p under 15 MB for the review page
    deliver = os.path.join(ROOT, "deliver")
    os.makedirs(deliver, exist_ok=True)
    for master, name in ((subs, "FitPatches_berberin_final_subtitri"), (clean, "FitPatches_berberin_final_bez_subtitri")):
        out = os.path.join(deliver, name + "_1080p.mp4")
        log = os.path.join(tmp, name)
        for pas in (1, 2):
            run(["ffmpeg", "-v", "error", "-y", "-i", master, "-c:v", "libx264", "-preset", "slow", "-b:v", "1900k",
                 "-pass", str(pas), "-passlogfile", log] +
                (["-an", "-f", "mp4", os.devnull] if pas == 1 else
                 ["-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", out]))
    run(["ffmpeg", "-v", "error", "-y", "-i", subs, "-vf", "scale=720:1280:flags=lanczos", "-c:v", "libx264",
         "-crf", "24", "-preset", "slow", "-maxrate", "1000k", "-bufsize", "2000k", "-c:a", "aac", "-b:a", "96k",
         "-movflags", "+faststart", os.path.join(deliver, "preview_720p.mp4")])
    print("wrote", clean, subs, srt, f"({TOTAL}s)")


if __name__ == "__main__":
    main()
