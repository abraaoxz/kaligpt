#!/bin/bash

cd /opt/kaligpt
source venv/bin/activate

uvicorn server:app --host 127.0.0.1 --port 8000 &
sleep 2

python3 kaligpt.py

