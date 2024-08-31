#/bin/bash
apt update && DEBIAN_FRONTEND=noninteractive apt install python3 python3-pip -y && pip install pytelegrambotapi telethon --break-system-packages && cd /tmp/code && python3 main.py
