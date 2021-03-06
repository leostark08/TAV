# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deepscan.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DeepScanLayout(QtWidgets.QMainWindow):
    def setupUi(self, DeepScanLayout):
        DeepScanLayout.setObjectName("DeepScanLayout")
        DeepScanLayout.resize(900, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "views/icons/vku_antivirus_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DeepScanLayout.setWindowIcon(icon)
        DeepScanLayout.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(DeepScanLayout)
        self.centralwidget.setObjectName("centralwidget")
        self.btnHome = QtWidgets.QPushButton(self.centralwidget)
        self.btnHome.setGeometry(QtCore.QRect(10, 10, 50, 50))
        self.btnHome.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnHome.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            "views/icons/vku_antivirus_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnHome.setIcon(icon1)
        self.btnHome.setIconSize(QtCore.QSize(40, 40))
        self.btnHome.setObjectName("btnHome")
        self.lbl_name = QtWidgets.QLabel(self.centralwidget)
        self.lbl_name.setGeometry(QtCore.QRect(375, 0, 180, 75))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_name.setFont(font)
        self.lbl_name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_name.setStyleSheet("color: #c82032;")
        self.lbl_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_name.setObjectName("lbl_name")
        self.lbl_icon = QtWidgets.QLabel(self.centralwidget)
        self.lbl_icon.setGeometry(QtCore.QRect(300, 0, 75, 75))
        self.lbl_icon.setText("")
        self.lbl_icon.setPixmap(QtGui.QPixmap("views/icons/deep.png"))
        self.lbl_icon.setScaledContents(True)
        self.lbl_icon.setObjectName("lbl_icon")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setEnabled(True)
        self.scrollArea.setGeometry(QtCore.QRect(20, 220, 865, 361))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setVisible(False)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 863, 359))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.logBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.logBrowser.setGeometry(QtCore.QRect(0, 0, 865, 360))
        self.logBrowser.setMaximumSize(QtCore.QSize(865, 360))
        self.logBrowser.setObjectName("logBrowser")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(
            QtCore.QRect(690, 170, 195, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.buttonBar = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.buttonBar.setContentsMargins(0, 0, 0, 0)
        self.buttonBar.setObjectName("buttonBar")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setVisible(False)
        self.buttonBar.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setVisible(False)
        self.buttonBar.addWidget(self.pushButton_2)
        self.circularProgressBarBase = QtWidgets.QFrame(self.centralwidget)
        self.circularProgressBarBase.setGeometry(
            QtCore.QRect(290, 150, 320, 380))
        self.circularProgressBarBase.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgressBarBase.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressBarBase.setObjectName("circularProgressBarBase")
        self.circularProgress = QtWidgets.QFrame(self.circularProgressBarBase)
        self.circularProgress.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.circularProgress.setStyleSheet("QFrame{\n"
                                            "    border-radius: 150px;\n"
                                            "    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgb(247, 193, 131), stop:0.750 rgb(247, 147, 30));\n"
                                            "}")
        self.circularProgress.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgress.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgress.setObjectName("circularProgress")
        self.circularBg = QtWidgets.QFrame(self.circularProgressBarBase)
        self.circularBg.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.circularBg.setStyleSheet("QFrame{\n"
                                      "    border-radius: 150px;\n"
                                      "    background-color: rgba(77, 77, 127, 120);\n"
                                      "}")
        self.circularBg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularBg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularBg.setObjectName("circularBg")
        self.container = QtWidgets.QFrame(self.circularProgressBarBase)
        self.container.setGeometry(QtCore.QRect(25, 25, 270, 270))
        self.container.setStyleSheet("QFrame{\n"
                                     "    border-radius: 135px;\n"
                                     "    background-color: rgb(255, 255, 255);\n"
                                     "}")
        self.container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container.setObjectName("container")
        self.lbTitle = QtWidgets.QLabel(self.container)
        self.lbTitle.setGeometry(QtCore.QRect(0, 20, 271, 45))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lbTitle.sizePolicy().hasHeightForWidth())
        self.lbTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.lbTitle.setFont(font)
        self.lbTitle.setStyleSheet("background-color: none;\n"
                                   "color: #c82032;")
        self.lbTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lbTitle.setObjectName("lbTitle")
        self.lbPercentage = QtWidgets.QLabel(self.container)
        self.lbPercentage.setGeometry(QtCore.QRect(10, 50, 261, 172))
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(60)
        self.lbPercentage.setFont(font)
        self.lbPercentage.setStyleSheet("background-color: none;\n"
                                        "color: #f7961e;")
        self.lbPercentage.setAlignment(QtCore.Qt.AlignCenter)
        self.lbPercentage.setObjectName("lbPercentage")
        self.lbDeleted = QtWidgets.QLabel(self.container)
        self.lbDeleted.setGeometry(QtCore.QRect(0, 215, 271, 25))
        self.lbDeleted.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbDeleted.setFont(font)
        self.lbDeleted.setStyleSheet("color:#c82032;\n"
                                     "background-color: none;")
        self.lbDeleted.setAlignment(QtCore.Qt.AlignCenter)
        self.lbDeleted.setObjectName("lbDeleted")
        self.lbDetected = QtWidgets.QLabel(self.container)
        self.lbDetected.setGeometry(QtCore.QRect(0, 190, 271, 25))
        self.lbDetected.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbDetected.setFont(font)
        self.lbDetected.setStyleSheet("color:#c82032;\n"
                                      "background-color: none;")
        self.lbDetected.setAlignment(QtCore.Qt.AlignCenter)
        self.lbDetected.setObjectName("lbDetected")
        self.lbScanning = QtWidgets.QLabel(self.container)
        self.lbScanning.setGeometry(QtCore.QRect(0, 240, 271, 25))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lbScanning.sizePolicy().hasHeightForWidth())
        self.lbScanning.setSizePolicy(sizePolicy)
        self.lbScanning.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbScanning.setFont(font)
        self.lbScanning.setStyleSheet("color:#c82032;\n"
                                      "background-color: none;")
        self.lbScanning.setAlignment(QtCore.Qt.AlignCenter)
        self.lbScanning.setObjectName("lbScanning")
        self.horizontalLayoutWidget = QtWidgets.QWidget(
            self.circularProgressBarBase)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 330, 271, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnPause = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnPause.setCheckable(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btnPause.sizePolicy().hasHeightForWidth())
        self.btnPause.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnPause.setFont(font)
        self.btnPause.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnPause.setStyleSheet("color: #c82032;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("views/icons/pause_resume.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPause.setIcon(icon2)
        self.btnPause.setObjectName("btnPause")
        self.horizontalLayout.addWidget(self.btnPause)
        self.btnCancel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btnCancel.sizePolicy().hasHeightForWidth())
        self.btnCancel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnCancel.setFont(font)
        self.btnCancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCancel.setStyleSheet("color: #c82032;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("views/icons/cancel_icon.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancel.setIcon(icon3)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout.addWidget(self.btnCancel)
        self.circularBg.raise_()
        self.circularProgress.raise_()
        self.container.raise_()
        self.horizontalLayoutWidget.raise_()
        DeepScanLayout.setCentralWidget(self.centralwidget)

        self.retranslateUi(DeepScanLayout)
        QtCore.QMetaObject.connectSlotsByName(DeepScanLayout)

    def retranslateUi(self, DeepScanLayout):
        _translate = QtCore.QCoreApplication.translate
        DeepScanLayout.setWindowTitle(
            _translate("DeepScanLayout", "Deep Scan"))
        self.lbl_name.setText(_translate("DeepScanLayout", "DEEP SCAN"))
        self.logBrowser.setHtml(_translate("DeepScanLayout",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("DeepScanLayout", "PushButton"))
        self.pushButton_2.setText(_translate("DeepScanLayout", "PushButton"))
        self.lbTitle.setText(_translate("DeepScanLayout",
                                        "<html><head/><body><p><span style=\" font-weight:600; color:#c82032;\">DEEP SCAN</span></p></body></html>"))
        self.lbPercentage.setText(_translate("DeepScanLayout",
                                             "<html><head/><body><p>100<span style=\" font-size:58pt; vertical-align:super;\">%</span></p></body></html>"))
        self.lbDetected.setText(_translate("DeepScanLayout", "Detected: 0"))
        self.lbDeleted.setText(_translate("DeepScanLayout", "Deleted: 0"))
        self.lbScanning.setText(_translate("DeepScanLayout", "Scanning..."))
        self.btnPause.setText(_translate("DeepScanLayout", "Pause"))
        self.btnCancel.setText(_translate("DeepScanLayout", "Cancel"))
