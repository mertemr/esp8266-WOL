try:
    import usocket as socket
except ImportError:
    import socket

import network
from time import sleep

from config import (
    WIFI_SSID,
    WIFI_PASSWORD,
    status_led,
    wifi_led,
    wake_on_lan_pin,
)

def blink(pin, delay):
    pin.on()
    sleep(delay)
    pin.off()
    sleep(delay)

def awake_server():
    wake_on_lan_pin.on()
    sleep(2)
    wake_on_lan_pin.off()

def run():
    status_led.off()
    wifi_led.off()
    wake_on_lan_pin.off()
    
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print(f"Connecting to {WIFI_SSID}...")
        sta_if.active(True)
        sta_if.connect(WIFI_SSID, WIFI_PASSWORD)
        while not sta_if.isconnected():
            pass
        print(f"Successfully connected to {WIFI_SSID}!")
    print('Network config:', sta_if.ifconfig())
    wifi_led.on()

    soc = socket.socket()
    soc.bind(('', 9))
    soc.setblocking(False)
    soc.listen(5)

    client = None
    while True:
        try:
            if client is None:
                print('Waiting for connection...')
                client, addr = soc.accept()
                print('Got connection from', addr)
            else:
                print('Waiting for data...')
            data = client.recv(1024)
            print('Data received:', data.decode())
            if data == b'awake':
                awake_server()
                client.close()
                client = None
            else:
                client.send(b'Invalid command.')
                client.close()
                client = None
        except Exception:
            pass
        blink(status_led, 0.7)

run()