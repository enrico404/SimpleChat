import sys
from PyQt5.QtWidgets import *
from MyClient import  Client
from PyQt5.QtCore import pyqtSignal
from threading import Thread


class ClientFrame(QWidget):
    def __init__(self):
        super().__init__()
        self.cl = Client()
        self.log = False




    def init_window(self):
        self.setWindowTitle("Simple Chat")
        self.setGeometry(300, 300, 600, 600)
        self.show()
        self.init_gui()

    def init_gui(self):
        self.textview = QTextEdit(self)
        self.textview.move(15, 15)
        self.textview.resize(570, 500)
        self.textview.setEnabled(False)
        self.textview.setText("Inserire il nome utente: ")
        self.textview.show()

        self.cl.update.connect(self.textview.append)  # connetto il segnale definito nella classe myclient e appendo il testo alla textview

        self.text_message = QLineEdit(self)
        self.text_message.setGeometry(15, 540, 430, 30)
        self.text_message.show()

        self.send = QPushButton("Send", self)
        self.send.setGeometry(483 , 540, 100, 30)
        self.send.clicked.connect(self.sendClick)
        self.send.show()


    def start(self):
        self.cl.log(self.text_message.text(),self.textview)
        self.log = True

    def sendClick(self):
        if self.log == False:
            print("loggo...")
            self.start()
        text = self.text_message.text()
        self.cl.send_message(text)



