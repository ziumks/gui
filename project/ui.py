import sys
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import *
import pymysql as sql
import re


conn = sql.connect(host='192.168.0.14', user='name', password='name', db='ZiumIOT', charset='utf8')
curs = conn.cursor()
form_class = uic.loadUiType('../Window.ui')[0]
next_class = uic.loadUiType('../login.ui')[1]


class Ui(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("전기안전공사 DB관리")
        self.btn.clicked.connect(self.btn_clicked)
        self.initUi()

    def initUi(self):
        exitAction = self.actionexit
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        self.Filemenu.addAction(exitAction)

        insertAction = self.actioninsert
        insertAction.setShortcut("Ctrl+I")
        insertAction.setStatusTip("Insert data into DB")
        #insertAction.triggered.connect(self.insert)

        modifyAction = self.actionmodify
        modifyAction.setShortcut("Ctrl+M")
        modifyAction.setStatusTip("modify some data")
        modifyAction.triggered.connect(self.modifyDialog)

        deleteAction = self.actiondelete
        deleteAction.setShortcut("Ctrl+D")
        deleteAction.setStatusTip("delete some data from db")
        #deleteAction.setStatusTip.connect()

    def btn_clicked(self):
        # addr = self.IDEdit.getText()
        r = re.compile(pattern='\d+')
        myID = self.IDEdit.toPlainText().replace('\n', '')
        myName = self.NameEdit.toPlainText().replace('\n', '')
        myAddr = self.AddrEdit.toPlainText().replace('\n', '')
        if ((myID or myName or myAddr) == "") or (r.findall(myID).__len__() == 0):
            QMessageBox.about(self, "error", "입력을 확인해주세요")
        else:
            QMessageBox.about(self, "msg", "DB에 저장됩니다.")
            qry = "Insert into exer (device_ID, deviceName, deviceAddr) values(%s,%s,%s);"
            curs.execute(qry, (myID, myName, myAddr))
            conn.commit()

    def insert(self):
        pass

    def modifyDialog(self):

        text, ok = QInputDialog.getText(self, 'DB를 수정합니다', '수정할 ID를 입력하세요')
        r = re.compile(pattern='\d+')
        if ok:
            if r.findall(text).__len__() == 0:
                QMessageBox.about(self, 'error', '숫자로 입력하세요')
            else:
                self.IDEdit.setText(text)
                self.btn.setText('수정')
                qry = "select deviceName, deviceAddr from exer where device_ID = %s;"
                curs.execute(qry, text) # db가 없을 때 생기는 예외처리 필요
                rows = curs.fetchall()
                for row in rows:
                    self.NameEdit.setText(row[0])
                    self.AddrEdit.setText(row[1])
                conn.commit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Ui()
    w.show()
    sys.exit(app.exec())
