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
    input_pin
)

def blink(pin, delay):
    global counter
    pin.on()
    sleep(delay)
    pin.off()
    sleep(delay)

def awake_server(is_awaken):
    if is_awaken:
        print('Already awaken.')
        for _ in range(3):
            blink(wifi_led, 0.125)
        wifi_led.on()
        return
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

    is_awaken = False
    client = None
    while True:
        value = input_pin.read()
        voltage = value * 3.3 / 1024
        is_awaken = True if voltage > 1.7 else False            
        if is_awaken:
            status_led.off()
            sleep(60)
            continue
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
                awake_server(is_awaken)
                client.close()
                client = None
            else:
                client.send(b'Invalid command.')
                client.close()
                client = None
        except Exception:
            pass
        blink(status_led, 0.5)

run()