from SimpleChat.Client import Client
from threading import  Thread
#parte grafica



cl = Client()
cl.log()

Thread(cl.send_message()).start()