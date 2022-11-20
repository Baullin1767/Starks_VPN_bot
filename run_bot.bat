@echo off

call %~dp0VPN_bot\venv\Scripts\activate

cd %~dp0VPN_bot

set TOKEN=5748225409:AAHZDbMhBHNRejF4LOtQTt5WlzLq2i2g6zI

python vpn_bot.py

pause