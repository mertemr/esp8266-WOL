# esp8266-WOL
Wake-On-Lan with MicroPython ESP8266.

## How it works?
My motherboard does not support Wake-On-Lan. So I decided to use ESP8266 to wake up my computer. ESP8266 is connected to the motherboard's power button pins. When ESP8266 receives a connection, it sends a signal to the motherboard to turn on the computer.

## Installation
1. Clone the repository:
```
git clone https://github.com/mertemr/esp8266-WOL
```

2. Install **amp** and **esptool**:
```bash
pip3 install adafruit-ampy esptool
```

3. If [MicroPython](https://micropython.org/download/?port=esp8266) is not installed on ESP8266, install it:
```bash
esptool --port PORT erase_flash
esptool --port PORT --baud 115200 write_flash --flash_size=detect 0 FILE.bin
```

3. Upload the code to ESP8266:
```bash
ampy --port PORT put main.py
ampy --port PORT put config.py
```

4. Restart ESP8266

## Usage
1. Edit [config.py](./config.py) for your installation. (wifi, connections, etc.)
2. Connect ESP8266 to the motherboard's power button pins and external power supply.
3. Assign a static DHCP IP address to ESP8266.
3. Set-up your router to forward port 9 to ESP8266.
4. Done. You can use [wol.py](./wol.py) to wake up your computer from anywhere.
