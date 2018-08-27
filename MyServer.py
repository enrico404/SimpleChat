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
        self.welcome_message = "Welcome!! \n"
        self.stream_socket.listen(5)
        self.clients = []  # lists of all clients connected

    def handle_client(self, client):
        while True:
            data = client.recv(1024)
            if not data:
                break
            temp = data.decode()

            print("messagge received: "+temp)
            if temp == "ABC_EXIT_SIGNAL":
                break
            for cl in self.clients:
                cl.send(data)

        # close the client connection from the server side
        temp ="ABC_EXIT_SIGNAL"
        client.send(temp.encode()) # send the close message to the client
        client.close()
        self.clients.remove(client)


    def server_running(self):
        while True:
            client, addr = self.stream_socket.accept()
            print("client accepted")
            client.send(self.welcome_message.encode())

            if client not in self.clients:
                self.clients.append(client)
                Thread(target=self.handle_client, args=(client,)).start()
