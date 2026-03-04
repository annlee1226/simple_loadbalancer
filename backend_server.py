import sys
from flask import Flask

app = Flask(__name__)

server_name = sys.argv[1] if len(sys.argv) > 1 else "Unknown"


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def handle_request(path):
    return f"Hello from Server {server_name}\n"


if __name__ == "__main__":
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 5001
    app.run(port=port)
