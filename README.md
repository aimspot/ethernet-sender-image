# ethernet-sender-image

# Main code
`
import socket
import cv2
import numpy as np
import time

def send_image(image, ip, port):
    # Преобразование изображения в массив байт
    _, img_encoded = cv2.imencode('.jpg', image)
    data = np.array(img_encoded).tobytes()

    # Создание сокета и отправка данных
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    
    # Замер времени отправки
    start_time = time.time()
    sock.sendall(data)
    
    # Закрытие сокета и вывод времени отправки
    sock.close()
    end_time = time.time()
    print("Image sent. Time taken:", end_time - start_time, "seconds")

def receive_image(ip, port):
    # Создание сокета и прослушивание порта
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ip, port))
    sock.listen(1)
    print("Waiting for a connection...")

    # Принятие подключения и получение данных
    conn, addr = sock.accept()
    print("Connected by", addr)
    data = b""
    while True:
        chunk = conn.recv(4096)
        if not chunk:
            break
        data += chunk
    conn.close()

    # Преобразование массива байт в изображение
    nparr = np.frombuffer(data, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return image

# Пример использования
ip = "192.168.1.100"
port = 12345

# Захват изображения с камеры
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cap.release()

# Отправка изображения
send_image(frame, ip, port)

# Получение изображения
start_time = time.time()
received_image = receive_image(ip, port)
end_time = time.time()
print("Image received. Time taken:", end_time - start_time, "seconds")

cv2.imshow("Received Image", received_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
`