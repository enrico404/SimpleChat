from ClientFrame import *
import sys
from PyQt5.QtWidgets import QApplication



app = QApplication(sys.argv)
cl_frame = ClientFrame()
cl_frame.init_window()
sys.exit(app.exec_())

