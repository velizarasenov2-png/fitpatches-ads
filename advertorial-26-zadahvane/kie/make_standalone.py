"""Build standalone.html: the same page with every img/ picture embedded (base64 JPEG), so it opens
anywhere as a single file (phone preview, upload, send). Images are re-compressed to 1000px wide."""
import base64, io, os, re
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
html = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()


def embed(m):
    path = os.path.join(ROOT, m.group(1))
    im = Image.open(path).convert("RGB")
    w = 120 if "avatar" in path else 860
    if im.width > w:
        im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    buf = io.BytesIO(); im.save(buf, "WEBP", quality=72, method=6)
    return 'src="data:image/webp;base64,' + base64.b64encode(buf.getvalue()).decode() + '"'


out = re.sub(r'src="(img/[^"]+)"', embed, html)
open(os.path.join(ROOT, "standalone.html"), "w", encoding="utf-8").write(out)
print("standalone.html", round(len(out.encode()) / 1e6, 2), "MB,", out.count("data:image/webp"), "images")
