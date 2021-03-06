from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # browse files button
        self.Browse = QtWidgets.QPushButton(self.centralwidget)
        self.Browse.setGeometry(QtCore.QRect(100, 20, 120, 28))
        self.Browse.setObjectName("Browse")
        #surface rendering button
        self.sRender = QtWidgets.QPushButton(self.centralwidget)
        self.sRender.setGeometry(QtCore.QRect(100, 60, 120, 28))
        self.sRender.setObjectName("sRender")
        #iso label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 100, 111, 16))
        self.label.setObjectName("label")
        #iso slider label
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 110, 61, 20))
        self.label_2.setObjectName("label_2")
        #iso slider
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(30, 130, 251, 16))
        self.horizontalSlider.setMaximum(150)
        self.horizontalSlider.setProperty("value", 25)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        #volume rendering button
        self.vRender = QtWidgets.QPushButton(self.centralwidget)
        self.vRender.setGeometry(QtCore.QRect(100, 170, 120, 28))
        self.vRender.setObjectName("vRender")
        #skin color label
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 210, 111, 16))
        self.label_3.setObjectName("label_3")
        #skin red color label
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 240, 111, 16))
        self.label_4.setObjectName("label_4")
        #skin red color slider label
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(260, 240, 61, 20))
        self.label_5.setObjectName("label_5")
        #red color slider
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(30, 260, 251, 16))
        self.horizontalSlider_2.setMaximum(10)
        self.horizontalSlider_2.setProperty("value",5)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        #skin green color label
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 290, 111, 16))
        self.label_6.setObjectName("label_6")
        #skin green color slider label
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(260, 290, 61, 20))
        self.label_7.setObjectName("label_7")
        #blue green slider
        self.horizontalSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(30, 310, 251, 16))
        self.horizontalSlider_3.setMaximum(10)
        self.horizontalSlider_3.setProperty("value",5)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        #skin blue color label
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 340, 111, 16))
        self.label_8.setObjectName("label_8")
        #skin blue color slider label
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(260, 340, 61, 20))
        self.label_9.setObjectName("label_9")
        #blue color slider
        self.horizontalSlider_4 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_4.setGeometry(QtCore.QRect(30, 360, 251, 16))
        self.horizontalSlider_4.setMaximum(10)
        self.horizontalSlider_4.setProperty("value",5)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        #Bone color label
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 400, 111, 16))
        self.label_10.setObjectName("label_10")
        #Bone red color label
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(30, 430, 111, 16))
        self.label_11.setObjectName("label_11")
        #Bone red color slider label
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(260, 430, 61, 20))
        self.label_12.setObjectName("label_12")
        #Bone color slider
        self.horizontalSlider_5 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_5.setGeometry(QtCore.QRect(30, 450, 251, 16))
        self.horizontalSlider_5.setMaximum(10)
        self.horizontalSlider_5.setProperty("value",5)
        self.horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_5.setObjectName("horizontalSlider_5")
        #Bone green color label
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(30, 480, 111, 16))
        self.label_13.setObjectName("label_13")
        #Bone green color slider label
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(260, 480, 61, 20))
        self.label_14.setObjectName("label_14")
        #Bone green slider
        self.horizontalSlider_6 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_6.setGeometry(QtCore.QRect(30, 500, 251, 16))
        self.horizontalSlider_6.setMaximum(10)
        self.horizontalSlider_6.setProperty("value",5)
        self.horizontalSlider_6.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_6.setObjectName("horizontalSlider_6")
        #Bone blue color label
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(30, 530, 111, 16))
        self.label_15.setObjectName("label_15")
        #Bone blue color slider label
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(260, 530, 61, 20))
        self.label_16.setObjectName("label_16")
        #Bone blue slider
        self.horizontalSlider_7 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_7.setGeometry(QtCore.QRect(30, 550, 251, 16))
        self.horizontalSlider_7.setMaximum(10)
        self.horizontalSlider_7.setProperty("value",5)
        self.horizontalSlider_7.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_7.setObjectName("horizontalSlider_7")

        #skin opacity label
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(30, 620, 111, 16))
        self.label_17.setObjectName("label_17")
        #skin blue color slider label
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(260, 620, 61, 20))
        self.label_18.setObjectName("label_18")
        #skin opacity slider
        self.horizontalSlider_8 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_8.setGeometry(QtCore.QRect(30, 640, 251, 16))
        self.horizontalSlider_8.setMaximum(100)
        self.horizontalSlider_8.setProperty("value",15)
        self.horizontalSlider_8.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_8.setObjectName("horizontalSlider_8")
        #bone opacity label
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(30, 670, 111, 16))
        self.label_19.setObjectName("label_19")
        #bone blue color slider label
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(260, 670, 61, 20))
        self.label_20.setObjectName("label_20")
        #bone opacity slider
        self.horizontalSlider_9 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_9.setGeometry(QtCore.QRect(30, 690, 251, 16))
        self.horizontalSlider_9.setMaximum(100)
        self.horizontalSlider_9.setProperty("value",15)
        self.horizontalSlider_9.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_9.setObjectName("horizontalSlider_9")
        
       
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionKlvafjl_k = QtWidgets.QAction(MainWindow)
        self.actionKlvafjl_k.setObjectName("actionKlvafjl_k")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")

        self.retranslateUi(MainWindow)
        self.horizontalSlider.sliderMoved['int'].connect(self.label_2.setNum)
        self.horizontalSlider_2.sliderMoved['int'].connect(self.label_5.setNum)
        self.horizontalSlider_3.sliderMoved['int'].connect(self.label_7.setNum)
        self.horizontalSlider_4.sliderMoved['int'].connect(self.label_9.setNum)
        self.horizontalSlider_5.sliderMoved['int'].connect(self.label_12.setNum)
        self.horizontalSlider_6.sliderMoved['int'].connect(self.label_14.setNum)
        self.horizontalSlider_7.sliderMoved['int'].connect(self.label_16.setNum)
        self.horizontalSlider_8.sliderMoved['int'].connect(self.label_18.setNum)
        self.horizontalSlider_9.sliderMoved['int'].connect(self.label_20.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CT Data Viewer"))
        self.label.setText(_translate("MainWindow", "Iso value"))
        self.label_2.setText(_translate("MainWindow", "25"))
        self.Browse.setText(_translate("MainWindow", "Load Files"))
        self.sRender.setText(_translate("MainWindow", "Surface Rendering"))
        self.vRender.setText(_translate("MainWindow", "Ray Casting"))
        self.label_3.setText(_translate("MainWindow", "Skin Color"))
        self.label_4.setText(_translate("MainWindow", "Red"))
        self.label_5.setText(_translate("MainWindow", "5"))
        self.label_6.setText(_translate("MainWindow", "Green"))
        self.label_7.setText(_translate("MainWindow", "5"))
        self.label_8.setText(_translate("MainWindow", "Blue"))
        self.label_9.setText(_translate("MainWindow", "5"))
        self.label_10.setText(_translate("MainWindow", "Bone Color"))
        self.label_11.setText(_translate("MainWindow", "Red"))
        self.label_12.setText(_translate("MainWindow", "5"))
        self.label_13.setText(_translate("MainWindow", "Green"))
        self.label_14.setText(_translate("MainWindow", "5"))
        self.label_15.setText(_translate("MainWindow", "Blue"))
        self.label_16.setText(_translate("MainWindow", "5"))
        self.label_17.setText(_translate("MainWindow", "Skin Opacity"))
        self.label_18.setText(_translate("MainWindow", "15"))
        self.label_19.setText(_translate("MainWindow", "Bone Opacity"))
        self.label_20.setText(_translate("MainWindow", "15"))
        self.actionKlvafjl_k.setText(_translate("MainWindow", "klvafjl k"))
        self.actionClose.setText(_translate("MainWindow", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())