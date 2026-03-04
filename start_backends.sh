#!/usr/bin/env bash
# Starts all 3 backend servers in the background

cd "$(dirname "$0")"
source venv/bin/activate

echo "Starting backend servers..."

python backend_server.py 1 5001 &
python backend_server.py 2 5002 &
python backend_server.py 3 5003 &

echo "Backend servers running on ports 5001, 5002, 5003"
echo "Press Ctrl+C to stop all"

trap "kill 0" EXIT
wait
