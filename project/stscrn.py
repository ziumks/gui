import sys

from PyQt5.QtWidgets import *

import project as login


class Form(QWidget):
    def __init__(self):
        super().__init__()
        startlabel = QLabel("관리프로그램을 시작하시겠습니까?")

        submitYButton = QPushButton("&Y")
        submitNButton = QPushButton("&N")

        buttonlayout1 = QVBoxLayout()
        buttonlayout1.addWidget(startlabel)
        buttonlayout1.addWidget(submitYButton)
        buttonlayout1.addWidget(submitNButton)

        submitYButton.clicked.connect(self.next)
        submitNButton.clicked.connect(self.finish)

        mainlayout = QGridLayout()
        # mainLayout.addWidget(nameLabel, 0, 0)
        mainlayout.addLayout(buttonlayout1, 0, 1)

        self.setLayout(mainlayout)
        self.setWindowTitle("Hello Qt")

    def finish(self):
        sys.exit()

    def next(self):
        login.Login
        self.close()
