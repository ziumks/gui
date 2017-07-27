from PyQt5.QtWidgets import *
import sys
from PyQt5 import uic
from PyQt5 import QtWidgets

form_class = uic.loadUiType('../login.ui')


class Login(QMdiSubWindow):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            #self.loginbtn.clicked.connect(self.finish)


        def finish(self):
            sys.exit

if __name__ == '__main__"':
#    app = QApplication(sys.argv)
    screen = Login()
    #screen.show()
#    app.exec()
