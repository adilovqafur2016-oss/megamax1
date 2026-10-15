#!/usr/bin/env bash
# MegaMax1 v1.9 – Linux launcher
cd "$(dirname "$0")"
export PYTHONUNBUFFERED=1

if ! command -v python3 &>/dev/null; then
    echo "python3 tapılmadı. Quraşdır: sudo apt install python3 python3-pip"
    exit 1
fi

python3 -c "import ursina" 2>/dev/null || {
    echo "ursina yoxdur. Quraşdırıram..."
    pip3 install --user ursina pillow
}

python3 main.py
