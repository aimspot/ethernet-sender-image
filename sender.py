import socket
import cv2
import numpy as np
import time

def send_image(image, ip, port):
    _, img_encoded = cv2.imencode('.jpg', image)
    data = np.array(img_encoded).tobytes()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    
    start_time = time.time()
    sock.sendall(data)
    
    sock.close()
    end_time = time.time()
    print("Image sent. Time taken:", end_time - start_time, "seconds")

if __name__ == "__main__":
    ip = "192.168.1.100"
    port = 12345

    
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    send_image(frame, ip, port)