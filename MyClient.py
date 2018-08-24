# python3
import sys
import socket
from threading import Thread
from PyQt5 import QtCore

from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject


class Client(QObject):
    update = QtCore.pyqtSignal(str) #il segnale va dichiarato a livello di classe
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
        msg = self.nome+": "+ msg
        msg_cod = msg.encode()
        self.stream_socket.send(msg_cod)
        if msg == "q":
            self.stop = True

    def response_control(self):
        while True:
            if self.stop == True:
                self.stream_socket.close()
                return
            resp = self.stream_socket.recv(1024) #max 1024 bytes of response
            resp_dec = resp.decode()

            self.update.emit(resp_dec) #emetto il segnale per dire al main thread di aggiorare la view
