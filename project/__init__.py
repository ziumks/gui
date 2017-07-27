import project
from PyQt5.QtWidgets import *
import sys
import project.stscrn as st

app = QApplication(sys.argv)
screen = st.Form()
screen.show()
sys.exit(app.exec_())
