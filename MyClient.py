# python3
import sys
import socket
from threading import Thread
from PyQt5 import QtCore

from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject


class Client(QObject):
    update = QtCore.pyqtSignal(str) # the signal must be declared at class level
    def __init__(self):
        super().__init__()
        self.stream_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = 'localhost'
        self.port = 8080
        self.server_address = ((self.host, self.port))
        self.stop = False # if true i have to close the connection



    def log(self, nome_user, textview):
        self.nome = nome_user
        self.textview = textview
        self.stream_socket.connect(self.server_address)
        print("connected!")
        Thread(target=self.response_control).start()


    def send_message(self, msg):
        if msg != "ABC_EXIT_SIGNAL":
            msg = self.nome+":  "+ msg
            msg_cod = msg.encode()
            self.stream_socket.send(msg_cod)
        else:
            self.stream_socket.send(msg.encode())
    def response_control(self):
        while True:

            resp = self.stream_socket.recv(1024) #max 1024 bytes of response
            resp_dec = resp.decode()

            if resp_dec == "ABC_EXIT_SIGNAL":  # if response is q i have to close the connection from the client side
                break
            self.update.emit(resp_dec) # emit the signal to update the textview

        self.stream_socket.close()
        print("connection closed")