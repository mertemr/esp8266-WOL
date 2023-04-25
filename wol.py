import socket
import time

ip_address = "YOUR_IP_ADDRESS"

port = 9
data = b"awake"

def send_wol():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip_address, port))
    print(f"Sending {data.decode()} to {ip_address}:{port}.")
    sock.sendall(data)
    time.sleep(3)
    sock.close()

if __name__ == "__main__":
    assert ip_address != "YOUR_IP_ADDRESS", "Please set your IP address."
    send_wol()
