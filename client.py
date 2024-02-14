import socket
from threading import Thread
import threading


HOST = '127.0.0.1'
PORT = 5002

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
#client.sendall(byte)


def task1():
    while True:
        in_data = client.recv(4096)
        print('От сервера: ', in_data.decode())

def task2():
    while True:
        out_data = input()
        client.sendall(bytes(out_data, 'UTF_8'))
        print('Отправлено: ', str(out_data))

t1 = Thread(target=task2)
t2 = Thread(target=task1)

t1.start()
t2.start()
