"""9:16 end card: the real FitPatches pouch on its own pink, feathered into a matching background."""
import os
from PIL import Image, ImageFilter, ImageDraw
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
W, H = 1440, 2560
p = Image.open(os.path.join(ROOT, "refs", "pouch.png")).convert("RGB")
bg = p.resize((W, H)).filter(ImageFilter.GaussianBlur(120))  # the photo's own pink, smoothly extended
scale = 1240 / p.width
p = p.resize((1240, int(p.height * scale)), Image.LANCZOS)
mask = Image.new("L", p.size, 0)
ImageDraw.Draw(mask).rectangle([60, 60, p.width - 60, p.height - 60], fill=255)
mask = mask.filter(ImageFilter.GaussianBlur(50))
bg.paste(p, ((W - p.width) // 2, 230), mask)
bg.save(os.path.join(ROOT, "refs", "endcard_pouch.jpg"), quality=95)
