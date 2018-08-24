# python3

import socket
from threading import Thread

from PyQt5.QtCore import QObject


class Server(QObject):
    def __init__(self):
        super().__init__()
        self.stream_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = 'localhost'
        self.port = 8080
        self.stream_socket.bind((self.host, self.port))
        self.welcome_message = "Welcome, write 'q' for exit \n"
        self.stream_socket.listen(5)
        self.clients = []  # lists of all clients connected

    def handle_client(self):
        while True:
            data = self.client.recv(1024)
            temp = data.decode()

            print("messaggio ricevuto: "+temp)
            if temp == "q":
                self.client.close()
                self.clients.remove(self.client)
                break
            for cl in self.clients:
                cl.send(data)

            #if self.clients[0] == self.client:
             #   self.clients[1].send(data)
            #else:
             #   self.clients[0].send(data)



    def server_running(self):
        while True:
            self.client, addr = self.stream_socket.accept()
            print("client accepted")
            self.client.send(self.welcome_message.encode())

            if self.client not in self.clients:
                self.clients.append(self.client)
                Thread(target=self.handle_client).start()
