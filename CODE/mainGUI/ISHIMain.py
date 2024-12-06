from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(1280, 720)
        Widget.setMinimumSize(QtCore.QSize(1280, 720))
        Widget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label = QtWidgets.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(300, 10, 721, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\Users\\HI\\Downloads\\Untitled_design.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabelfwr(Widget)
        self.label_2.setGeometry(QtCore.QRect(0, 540, 1281, 201))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:\\Users\\HI\\Downloads\\b.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Widget)
        self.label_3.setGeometry(QtCore.QRect(300, 110, 721, 391))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("C:\\Users\\HI\\Downloads\\82ab4698e35dbb487566f3cec0503f04.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Widget)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 261, 191))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("E:/ISHI TECHNOLOGY/IMAGES/G.U.I Material/ExtraGui/B.G_Template_1.gif"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.Talking = QtWidgets.QLabel(Widget)
        self.Talking.setGeometry(QtCore.QRect(-260, 120, 541, 411))
        self.Talking.setText("")
        self.Talking.setPixmap(QtGui.QPixmap("E:/ISHI TECHNOLOGY/IMAGES/G.U.I Material/VoiceReg/Siri_1.gif"))
        self.Talking.setScaledContents(False)
        self.Talking.setObjectName("Talking")
        self.listing = QtWidgets.QLabel(Widget)
        self.listing.setGeometry(QtCore.QRect(-50, 210, 401, 291))
        self.listing.setText("")
        self.listing.setPixmap(QtGui.QPixmap("C:\\Users\\HI\\Downloads\\6ba174bf48e9b6dc8d8bd19d13c9caa9.gif"))
        self.listing.setScaledContents(True)
        self.listing.setObjectName("listing")
        self.reload = QtWidgets.QLabel(Widget)
        self.reload.setGeometry(QtCore.QRect(-110, 250, 341, 231))
        self.reload.setText("")
        self.reload.setPixmap(QtGui.QPixmap("E:/ISHI TECHNOLOGY/IMAGES/G.U.I Material/VoiceReg/Qualt.gif"))
        self.reload.setScaledContents(False)
        self.reload.setObjectName("reload")
        self.reload_2 = QtWidgets.QLabel(Widget)
        self.reload_2.setGeometry(QtCore.QRect(-70, 190, 381, 351))
        self.reload_2.setText("")
        self.reload_2.setPixmap(QtGui.QPixmap("C:\\Users\\HI\\Downloads\\Untitled-design-unscreen.gif"))
        self.reload_2.setScaledContents(True)
        self.reload_2.setObjectName("reload_2")
        self.label_5 = QtWidgets.QLabel(Widget)
        self.label_5.setGeometry(QtCore.QRect(930, 0, 481, 551))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("C:\\Users\\HI\\Downloads\\f47c61e6c304adb00430e31c48aded00.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_3.raise_()
        self.Talking.raise_()
        self.listing.raise_()
        self.reload.raise_()
        self.reload_2.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label.raise_()
        self.label_2.raise_()

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
