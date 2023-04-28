import machine

class PINS:
    D0 = 16
    D1 = 5
    D2 = 4
    D3 = 0
    D4 = 2
    D5 = 14
    D6 = 12
    D7 = 13
    D8 = 15

OUT = machine.Pin.OUT
IN = machine.Pin.IN

WIFI_SSID = "YOUR_WIFI_SSID"
WIFI_PASSWORD = "YOUR_WIFI_PASSWORD"

status_led = machine.Pin(PINS.D0, OUT)      # Blink when running
wifi_led   = machine.Pin(PINS.D1, OUT)      # Light up when connected to WiFi
wake_on_lan_pin = machine.Pin(PINS.D2, OUT)
input_pin = machine.ADC(0)