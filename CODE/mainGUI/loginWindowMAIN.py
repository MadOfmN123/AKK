import sys
import self
from PyQt5.QtWidgets import QWidget, QLineEdit
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui

from loginWindowGUI import Ui_LoginwindowClass


class loginWindowGUI(QWidget):
    def __init__(self):
        super(loginWindowGUI, self).__init__()
        self.loginUI = Ui_LoginwindowClass()
        self.loginUI.setupUi(self)

        self.loginUI.label_2.hide()
        self.loginUI.passwordentry.setEchoMode(QLineEdit.Password)
        self.loginUI.pushButton_4.clicked.connect(self.validateLogin)

        self.loginUI.label_2Movie = QtGui.QMovie("C:\\Users\\HI\\Downloads\\Wrong Pass.gif")
        self.loginUI.label_2.setMovie(self.loginUI.label_2Movie)

        self.loginUI.pushButton.clicked.connect(self.pushButton)
        self.loginUI.pushButton_4.clicked.connect(self.validateLogin)

    def pushButton(self):
        self.loginUI.usernameentry.clear()
        self.loginUI.passwordentry.clear()
        self.stopMovie()

    def validateLogin(self):
        username = self.loginUI.usernameentry.text()
        password = self.loginUI.passwordentry.text()
        if username == "sai" and password == "pass":
            print("login success")
            self.Ishi()

        else:
            self.playMovie()

    def Ishi(self):
        from ISHITechnologyMAIN import ishiCodingClass
        self.showface = ishiCodingClass()
        ui.close()
        self.showface.show()
    def playMovie(self):
        self.loginUI.label_2.show()
        self.loginUI.label_2Movie.start()

    def stopMovie(self):
        self.loginUI.label_2.hide()
        self.loginUI.label_2Movie.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = loginWindowGUI()
    ui.show()
    sys.exit(app.exec_())
