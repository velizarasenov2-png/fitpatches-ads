"""Build standalone.html: the same page with every img/ picture embedded (base64 JPEG), so it opens
anywhere as a single file (phone preview, upload, send). Images are re-compressed to 1000px wide."""
import base64, io, os, re
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
html = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()


def embed(m):
    path = os.path.join(ROOT, m.group(1))
    # ANIMATED: an animated WebP/GIF is embedded as it is, so the animation survives
    im0 = Image.open(path)
    if getattr(im0, "is_animated", False):
        mime = "image/gif" if path.endswith(".gif") else "image/webp"
        return 'src="data:' + mime + ';base64,' + base64.b64encode(open(path, "rb").read()).decode() + '"'
    im = Image.open(path).convert("RGB")
    w = 160 if ("avatar" in path or "author" in path) else 640
    if im.width > w:
        im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    buf = io.BytesIO(); im.save(buf, "WEBP", quality=60, method=6)
    return 'src="data:image/webp;base64,' + base64.b64encode(buf.getvalue()).decode() + '"'


out = re.sub(r'src="(img/[^"]+)"', embed, html)
out = out.replace(' loading="lazy"', '')  # embedded images: show all at once
open(os.path.join(ROOT, "standalone.html"), "w", encoding="utf-8").write(out)
print("standalone.html", round(len(out.encode()) / 1e6, 2), "MB,", out.count("data:image/"), "images")
