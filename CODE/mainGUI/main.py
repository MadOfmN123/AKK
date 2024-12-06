import sys

from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import QtGui

from mainGUIFile import Ui_Dialog


class mainGUIFile(QDialog):
    def __init__(self):
        super(mainGUIFile, self).__init__()
        print("Setting Up GUI")
        self.firstUI = Ui_Dialog()
        self.firstUI.setupUi(self)

        self.firstUI.movie = QtGui.QMovie("E:\\ISHI TECHNOLOGY\\IMAGES\\G.U.I Material\\ExtraGui\\Jarvis_Gui (2).gif")
        self.firstUI.label_2.setMovie(self.firstUI.movie)
        self.firstUI.movie.start()

        self.firstUI.pushButton_2.clicked.connect(self.LG)
        self.firstUI.pushButton.clicked.connect(self.FR)

    def LG (self):
        from loginWindowMAIN import loginWindowGUI
        self.showlogin = loginWindowGUI()
        ui.close()
        self.showlogin.show()

    def FR (self):
        from faceRECOG import FaceRECOG
        self.showface = FaceRECOG()
        ui.close()
        self.showface.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = mainGUIFile()
    ui.show()
    sys.exit(app.exec_())
