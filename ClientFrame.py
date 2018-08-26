import sys
from PyQt5.QtWidgets import *
from MyClient import  Client
from PyQt5 import QtGui
from PyQt5 import QtCore
from threading import Thread


class ClientFrame(QWidget):
    def __init__(self):
        super().__init__()
        self.cl = Client()
        self.log = False
        self.stylesheet = """
            QPushButton{
                border-radius: 12px;
                background-color: #3498db;
                color: white;
            }
            QPushButton:hover{
                background-color: #2980b9;
                
            }
            
            QTextEdit{
                border:1px solid gray;
                color: black;
                
            }
            
            QLineEdit{
                padding-left: 10px;
                border:1px solid gray;
                border-radius: 12px;
            }
            QLineEdit:hover{
                
                border:1px solid #3498db;
                border-radius: 14px;
               
            }
        
        """



    def init_window(self):
        self.setWindowTitle("Simple Chat")
        self.move(300, 300)
        self.setFixedSize(600,600)
        self.show()
        self.init_gui()

    def init_gui(self):
        self.setStyleSheet(self.stylesheet)
        self.textview = QTextEdit(self)
        self.textview.move(15, 15)
        self.textview.resize(570, 500)
        self.textview.setEnabled(False)
        self.textview.setText("Inserire il nome utente: ")
        self.textview.show()

        self.cl.update.connect(self.textview.append)  # connetto il segnale definito nella classe myclient e appendo il testo alla textview

        self.text_message = QLineEdit(self)
        self.text_message.setGeometry(15, 540, 440, 30)
        self.text_message.show()




        self.send = QPushButton("Send", self)
        self.send.setGeometry(483 , 540, 100, 30)
        self.send.clicked.connect(self.sendClick)
        self.send.show()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Enter or QtCore.Qt.Key_Return:
            if self.text_message.text() != "":
                self.sendClick()

    def start(self):
        self.cl.log(self.text_message.text(),self.textview)
        self.log = True
        self.text_message.setText("")


    def sendClick(self):
        if self.log == False:
            print("loggo...")
            self.start()
        text = self.text_message.text()
        self.text_message.setText("")
        self.cl.send_message(text)



