import itertools
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.request
import urllib.error

BACKENDS = [
    "http://localhost:5001",
    "http://localhost:5002",
    "http://localhost:5003",
]

backend_cycle = itertools.cycle(BACKENDS)


class LoadBalancerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        backend = next(backend_cycle)
        target_url = backend + self.path

        try:
            with urllib.request.urlopen(target_url) as resp:
                body = resp.read()
                self.send_response(resp.status)
                self.send_header("Content-Type", resp.getheader("Content-Type", "text/html"))
                self.end_headers()
                self.wfile.write(body)
        except urllib.error.URLError as e:
            self.send_response(502)
            self.end_headers()
            self.wfile.write(f"Backend unavailable: {e}\n".encode())

    def log_message(self, format, *args):
        backend = BACKENDS[(next_index() - 1) % len(BACKENDS)]
        print(f"[LB] {self.address_string()} -> {args[0]}")


#Simple counter to track backends
_counter = itertools.count(0)


def next_index():
    return next(_counter)


#Override log_message is cleaner
LoadBalancerHandler.log_message = lambda self, fmt, *args: print(
    f"[Load Balancer] {args[0]}"
)

if __name__ == "__main__":
    port = 8080
    server = HTTPServer(("", port), LoadBalancerHandler)
    print(f"Load balancer listening on port {port}")
    print(f"Forwarding to backends: {BACKENDS}")
    server.serve_forever()
