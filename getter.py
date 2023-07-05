import socket
import cv2
import numpy as np
import time

def receive_image(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ip, port))
    sock.listen(1)
    print("Waiting for a connection...")

    conn, addr = sock.accept()
    print("Connected by", addr)
    start_time = time.time()
    data = b""
    while True:
        chunk = conn.recv(4096)
        if not chunk:
            break
        data += chunk
    conn.close()
    end_time = time.time()
    print("Image received. Time taken:", end_time - start_time, "seconds")

    nparr = np.frombuffer(data, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return image


if __name__ == "__main__":
    ip = "10.74.8.13"
    port = 12345
    received_image = receive_image(ip, port)
    print(received_image.shape)
