# python3

import socket
from threading import Thread


class Client(object):
    def __init__(self):
        self.stream_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = 'localhost'
        self.port = 8080
        self.server_address = ((self.host, self.port))

    def log(self):
        self.stream_socket.connect(self.server_address)
        print("connected!")
        Thread(target=self.response_control).start()
        msg = input("Inserire il nome utente: \n")
        self.nome = msg

    def send_message(self):
        msg = ""
        while msg != "q":
            msg = input("Inserire il messsaggio che si vuole spedire: \n")
            msg_cod = msg.encode()
            self.stream_socket.send(msg_cod)
        self.stream_socket.close()

    def response_control(self):
        while True:
            resp = self.stream_socket.recv(1024) #max 1024 bytes of response
            resp_dec = resp.decode()
            print("message: "+ resp_dec)
