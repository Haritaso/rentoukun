import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from ui import Ui_MainWindow
from mastodon import Mastodon
import asyncio

class Test(QMainWindow):
    def __init__(self,parent=None):
        super(Test, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.btn1 = self.ui.pushButton
        self.btn1.clicked.connect(self.make_clientid)
        self.btn3 = self.ui.pushButton_3
        self.btn3.clicked.connect(self.make_token)
        self.btn2 = self.ui.pushButton_2
        self.btn2.clicked.connect(self.tootstatus)

    def make_clientid(self):
        appname = self.ui.lineEdit.text()
        url = self.ui.lineEdit_2.text()
        cid_file = 'client_id.txt'
        Mastodon.create_app(
            appname,
            api_base_url= url,
            to_file= cid_file
        )
        with open(cid_file) as ci:
            self.ui.lineEdit_3.setText(ci.read())
    
    def make_token(self):
        clientid = "client_id.txt"
        url = self.ui.lineEdit_4.text()
        email = self.ui.lineEdit_5.text()
        password = self.ui.lineEdit_6.text()
        token = "access_token.txt"
        mastodon = Mastodon(
            client_id= clientid,
            api_base_url= url,
        )
        mastodon.log_in(
            username= email,
            password= password,
            to_file= token
        )
        with open(token) as at:
            self.ui.lineEdit_7.setText(at.read())
    def tootstatus(self):
        url = self.ui.lineEdit_4.text()
        cid_file = 'client_id.txt'
        token_file = 'access_token.txt'

        mastodon = Mastodon(
            client_id=cid_file,
            access_token=token_file,
            api_base_url=url
        )
        status = self.ui.textEdit.toPlainText()
        count = self.ui.spinBox.value()
        cw = self.ui.radioButton.isChecked()
        cwstatus = self.ui.lineEdit_8.text()
        visibility = self.ui.comboBox.currentText()
        print(status)
        print(count)
        print(cw)
        print(cwstatus)
        print(visibility)
        for i in range(count):
            if cw == True:
                mastodon.status_post(
                    status = status,
                    spoiler_text= cwstatus,
                    visibility = visibility
                )
            else:
                mastodon.status_post(
                    status = status,
                    visibility = visibility
                )
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Test()
    window.show()
    sys.exit(app.exec_())