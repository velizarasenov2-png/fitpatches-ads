"""Local preview of the FitPatches store with an unpublished theme.
Proxies every request to fitpatches.net and adds preview_theme_id, so the cart works too.
usage: python3 preview_proxy.py <port> <theme_id>
"""
import http.server
import re
import socketserver
import sys

import requests

UP = 'https://fitpatches.net'
PORT = int(sys.argv[1])
THEME = sys.argv[2]
START = '/products/fitpatches-berberinovi-plastiri-30'
SKIP = {'content-length', 'content-encoding', 'transfer-encoding', 'connection', 'keep-alive',
        'strict-transport-security', 'content-security-policy', 'content-security-policy-report-only',
        'alt-svc', 'set-cookie', 'x-frame-options'}
TEXTUAL = ('text/html', 'javascript', 'text/css')


class H(http.server.BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'

    def log_message(self, *a):
        pass

    def do_GET(self):
        self.fwd()

    def do_POST(self):
        self.fwd()

    def do_HEAD(self):
        self.fwd()

    def fwd(self):
        path = self.path
        if path in ('/', ''):
            self.send_response(302)
            self.send_header('Location', START)
            self.send_header('Content-Length', '0')
            self.end_headers()
            return
        if 'preview_theme_id=' not in path and '_shopify_essential=' not in (self.headers.get('Cookie') or ''):
            path += ('&' if '?' in path else '?') + 'preview_theme_id=' + THEME
        n = int(self.headers.get('Content-Length') or 0)
        body = self.rfile.read(n) if n else None
        hdr = {k: v for k, v in self.headers.items()
               if k.lower() not in ('host', 'accept-encoding', 'content-length', 'connection', 'origin', 'referer', 'user-agent')}
        hdr['Accept-Encoding'] = 'identity'
        if self.headers.get('Origin'):
            hdr['Origin'] = UP
        hdr['Referer'] = UP + START
        try:
            r = requests.request(self.command, UP + path, headers=hdr, data=body, allow_redirects=False, timeout=60)
        except Exception as e:  # upstream down
            msg = ('Upstream error: %s' % e).encode()
            self.send_response(502)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.send_header('Content-Length', str(len(msg)))
            self.end_headers()
            self.wfile.write(msg)
            return
        data = r.content
        ct = r.headers.get('Content-Type', '')
        if any(t in ct for t in TEXTUAL):
            t = data.decode('utf-8', 'replace')
            t = t.replace('https://fitpatches.net/', '/').replace('"https://fitpatches.net"', '""')
            t = re.sub(r'(["\'(=])//fitpatches\.net/', r'\1/', t)
            t = re.sub(r'(["\'(=])//(?=[a-z0-9.-]+\.[a-z]{2,}/)', r'\1https://', t)
            t = t.replace('connect.facebook.net', 'fb-blocked.invalid')  # no Meta pixel events from previews
            data = t.encode('utf-8')
        self.send_response(r.status_code)
        for k, v in r.headers.items():
            if k.lower() in SKIP:
                continue
            if k.lower() == 'location':
                v = v.replace('https://fitpatches.net', '')
            self.send_header(k, v)
        raw = getattr(r.raw, 'headers', None)
        cookies = raw.getlist('Set-Cookie') if raw is not None and hasattr(raw, 'getlist') else []
        for c in cookies:
            c = re.sub(r';\s*domain=[^;]*', '', c, flags=re.I)
            c = re.sub(r';\s*secure', '', c, flags=re.I)
            c = re.sub(r';\s*samesite=none', '; SameSite=Lax', c, flags=re.I)
            self.send_header('Set-Cookie', c)
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        if self.command != 'HEAD':
            self.wfile.write(data)


class S(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True


if __name__ == '__main__':
    S(('0.0.0.0', PORT), H).serve_forever()
