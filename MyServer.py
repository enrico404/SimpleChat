# python3

import socket
from threading import Thread


class Server(object):
    def __init__(self):
        self.stream_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = 'localhost'
        self.port = 8080
        self.stream_socket.bind((self.host, self.port))
        self.welcome_message = "Welcome, write 'q' for exit \n"
        self.stream_socket.listen(5)
        self.clients = []  # lists of all clients connected

    def handle_client(self, client):
        while True:
            data = client.recv(1024)
            temp = data.decode()
            if temp == "q":
                client.close()
                self.clients.remove(client)
                break

            if self.clients[0] == client:
                self.clients[1].send(data)
            else:
                self.clients[0].send(data)



    def server_running(self):
        while True:
            client, addr = self.stream_socket.accept()
            print("client accepted")
            client.send(self.welcome_message.encode())

            if client not in self.clients:
                self.clients.append(client)
                Thread(target=self.handle_client, args=(client,)).start()
