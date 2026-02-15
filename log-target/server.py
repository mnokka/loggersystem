import http.server
import socketserver
import threading
import time

LOG_FILE = "/logs/received.log"
PORT = 7777

lines = []
pos = 0

def follow_log():
    global pos
    while True:
        try:
            with open(LOG_FILE, "r") as f:
                f.seek(pos)
                new = f.readlines()
                if new:
                    lines.extend(l.rstrip() for l in new)
                pos = f.tell()
        except FileNotFoundError:
            pass
        time.sleep(2)

threading.Thread(target=follow_log, daemon=True).start()

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/logs":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write("\n".join(lines[-1000:]).encode())
        else:
            super().do_GET()

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Web UI: http://localhost:{PORT}")
    httpd.serve_forever()
