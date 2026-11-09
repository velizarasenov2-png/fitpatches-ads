"""Animated hero: the yellow (visceral fat) on the LEFT scan pulses. Writes img/hero-dexa.webp (page) and
hero-dexa.gif (for anywhere that needs a GIF)."""
import math, os
import numpy as np
from PIL import Image, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
src = Image.open(os.path.join(HERE, "..", "img", "hero-dexa.jpg")).convert("RGB")   # 1200x1200, static
W, H = src.size
arr = np.asarray(src).astype(np.float32) / 255.0
hsv = np.asarray(src.convert("HSV")).astype(np.float32)
h, s, v = hsv[..., 0] * 360 / 255, hsv[..., 1] / 255, hsv[..., 2] / 255
mask = ((h > 30) & (h < 66) & (s > 0.45) & (v > 0.55)).astype(np.float32)   # yellow / yellow-orange
mask[:, int(W * 0.497):] = 0                                                  # left scan only
m = Image.fromarray((mask * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(3))
glow = Image.fromarray((mask * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(14))
m = np.asarray(m).astype(np.float32)[..., None] / 255
g = np.asarray(glow).astype(np.float32)[..., None] / 255
hot = np.clip(arr * 1.35 + np.array([0.10, 0.06, -0.02]), 0, 1)            # brighter, warmer yellow
frames = []
N = 18
for i in range(N):
    k = (1 - math.cos(2 * math.pi * i / N)) / 2                                 # 0 → 1 → 0
    out = arr * (1 - m * k * 0.85) + hot * (m * k * 0.85)
    out = 1 - (1 - out) * (1 - g * k * np.array([0.55, 0.42, 0.05]))           # soft yellow halo (screen)
    frames.append(Image.fromarray((np.clip(out, 0, 1) * 255).astype(np.uint8)))
web = [f.resize((900, 900), Image.LANCZOS) for f in frames]
web[0].save(os.path.join(HERE, "..", "img", "hero-dexa.webp"), save_all=True, append_images=web[1:],
            duration=85, loop=0, quality=80, method=6)
gif = [f.resize((720, 720), Image.LANCZOS).convert("P", palette=Image.ADAPTIVE, colors=256) for f in frames]
gif[0].save(os.path.join(HERE, "..", "hero-dexa.gif"), save_all=True, append_images=gif[1:], duration=85, loop=0, optimize=True)
frames[N // 2].resize((600, 600)).save("/tmp/claude-0/-home-user-fitpatches-ads/baa6b13c-2de6-5efe-9303-3312ac01b124/scratchpad/peak.png")
frames[0].resize((600, 600)).save("/tmp/claude-0/-home-user-fitpatches-ads/baa6b13c-2de6-5efe-9303-3312ac01b124/scratchpad/rest.png")
print("ok")
