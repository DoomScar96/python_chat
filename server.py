import socket
import threading

HOST = '127.0.0.1'
PORT = 5002

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))
print("Server starting...")


class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("Новое подключение", clientAddress)

    def run(self):
        msg = ''
        while True:
            data = self.csocket.recv(4096)
            msg = data.decode()
            print(msg)
            if msg == '':
                print('Отключение')
                break


while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()
