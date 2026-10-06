"""Rough-cut assembly following the script's montage notes.

- trims every clip to its scripted length (start offset adjustable in EDL)
- 1 s black card "Един месец по-късно" between scene 8 and 9 (thin white font, small)
- 2 s end screen "Виж как работят →"
- missing clips become labelled black placeholders so the timing is always the final timing
Usage: python3 assemble.py [--vo path/to/voiceover.mp3]
"""
import os
import subprocess
import sys
import tempfile

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
CLIPS = os.path.join(ROOT, "clips")
OUT = os.path.join(ROOT, "rough_cut.mp4")
FONT = "/usr/share/fonts/opentype/inter/Inter-Light.otf"
W, H, FPS = 720, 1280, 24

# (name, seconds, start offset in the generated clip)
EDL = [
    ("S01", 6, 0), ("S02", 8, 0), ("S03a", 5, 0.5), ("S03b", 5, 0.5),
    ("S04a", 2, 1.0), ("S04b", 2, 1.0), ("S04c", 2, 1.0), ("S04d", 2, 1.0),
    ("S05", 10, 0), ("S06a", 5, 0.5), ("S06b", 5, 0.5),
    ("S07a", 5, 0.5), ("S07b", 5, 0.5), ("S07c", 4, 0),
    ("S08", 6, 0),
    ("CARD", 1, 0),
    ("S09a", 6, 0), ("S09b", 5, 0.5), ("S09c", 5, 0.5), ("S10", 6, 2.0),
    ("END", 2, 0),
]


def text_frame(text, size, color="white"):
    t = text.replace(":", r"\:").replace("'", r"\'")
    return (f"drawtext=fontfile={FONT}:text='{t}':fontcolor={color}:fontsize={size}:"
            "x=(w-text_w)/2:y=(h-text_h)/2")


def segment(name, dur, start, out):
    src = os.path.join(CLIPS, f"{name}.mp4")
    norm = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},format=yuv420p"
    if os.path.exists(src):
        cmd = ["ffmpeg", "-v", "error", "-y", "-ss", str(start), "-t", str(dur), "-i", src,
               "-vf", norm, "-af", "aresample=48000,volume=0.6", "-ac", "2",
               "-c:v", "libx264", "-crf", "18", "-c:a", "aac", "-shortest", out]
        # clips without audio get a silent track
        has_audio = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries",
                                    "stream=index", "-of", "csv=p=0", src],
                                   capture_output=True, text=True).stdout.strip()
        if not has_audio:
            cmd = ["ffmpeg", "-v", "error", "-y", "-ss", str(start), "-t", str(dur), "-i", src,
                   "-f", "lavfi", "-t", str(dur), "-i", "anullsrc=r=48000:cl=stereo",
                   "-vf", norm, "-c:v", "libx264", "-crf", "18", "-c:a", "aac", "-shortest", out]
    else:
        if name == "CARD":
            vf = text_frame("Един месец по-късно", 34)
        elif name == "END":
            vf = text_frame("Виж как работят →", 46)
        else:
            vf = text_frame(f"{name} — предстои", 30, "gray")
        cmd = ["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", f"color=black:s={W}x{H}:r={FPS}:d={dur}",
               "-f", "lavfi", "-t", str(dur), "-i", "anullsrc=r=48000:cl=stereo",
               "-vf", vf + ",format=yuv420p", "-c:v", "libx264", "-crf", "18", "-c:a", "aac", "-shortest", out]
    subprocess.run(cmd, check=True)


def main():
    vo = sys.argv[sys.argv.index("--vo") + 1] if "--vo" in sys.argv else None
    tmp = tempfile.mkdtemp()
    parts = []
    for i, (name, dur, start) in enumerate(EDL):
        p = os.path.join(tmp, f"{i:02d}_{name}.mp4")
        segment(name, dur, start, p)
        parts.append(p)
    lst = os.path.join(tmp, "list.txt")
    with open(lst, "w") as f:
        f.writelines(f"file '{p}'\n" for p in parts)
    silent = os.path.join(tmp, "cut.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst,
                    "-c", "copy", silent], check=True)
    if vo:
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", silent, "-i", vo, "-filter_complex",
                        "[0:a]volume=0.35[a0];[a0][1:a]amix=inputs=2:duration=first:normalize=0[a]",
                        "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", OUT], check=True)
    else:
        os.replace(silent, OUT)
    total = sum(d for _, d, _ in EDL)
    print(f"wrote {OUT} ({total}s)")


if __name__ == "__main__":
    main()
