# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\MyProjects\Antivirus\TAV\views\quickscan.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QuickScanLayout(object):
    def setupUi(self, QuickScanLayout):
        QuickScanLayout.setObjectName("QuickScanLayout")
        QuickScanLayout.resize(900, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(QuickScanLayout.sizePolicy().hasHeightForWidth())
        QuickScanLayout.setSizePolicy(sizePolicy)
        QuickScanLayout.setMinimumSize(QtCore.QSize(900, 600))
        QuickScanLayout.setMaximumSize(QtCore.QSize(900, 600))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        QuickScanLayout.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("e:\\MyProjects\\Antivirus\\TAV\\views\\icons/tav_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        QuickScanLayout.setWindowIcon(icon)
        QuickScanLayout.setStyleSheet("background-color: rgb(255, 255, 255);")
        QuickScanLayout.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(QuickScanLayout)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_icon = QtWidgets.QLabel(self.centralwidget)
        self.lbl_icon.setGeometry(QtCore.QRect(300, 0, 75, 75))
        self.lbl_icon.setText("")
        self.lbl_icon.setPixmap(QtGui.QPixmap("e:\\MyProjects\\Antivirus\\TAV\\views\\icons/quick.png"))
        self.lbl_icon.setScaledContents(True)
        self.lbl_icon.setObjectName("lbl_icon")
        self.lbl_name = QtWidgets.QLabel(self.centralwidget)
        self.lbl_name.setGeometry(QtCore.QRect(375, 0, 180, 75))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_name.setFont(font)
        self.lbl_name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_name.setStyleSheet("color: rgb(181, 61, 0);")
        self.lbl_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_name.setObjectName("lbl_name")
        self.btnHome = QtWidgets.QPushButton(self.centralwidget)
        self.btnHome.setGeometry(QtCore.QRect(17, 13, 50, 50))
        self.btnHome.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnHome.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("e:\\MyProjects\\Antivirus\\TAV\\views\\icons/home_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnHome.setIcon(icon1)
        self.btnHome.setIconSize(QtCore.QSize(40, 40))
        self.btnHome.setObjectName("btnHome")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 540, 861, 49))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.logToolBar = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.logToolBar.setContentsMargins(0, 0, 0, 0)
        self.logToolBar.setObjectName("logToolBar")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.progressBarScan = QtWidgets.QProgressBar(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBarScan.sizePolicy().hasHeightForWidth())
        self.progressBarScan.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.progressBarScan.setFont(font)
        self.progressBarScan.setStyleSheet("QProgressBar::chunk\n"
"{\n"
"    background-color: rgb(247, 147, 30);\n"
"}\n"
"QProgressBar\n"
"{\n"
"color: rgb(255, 255, 255);\n"
"background-color :rgb(247, 234, 186);\n"
"border : 1px;\n"
"}\n"
"")
        self.progressBarScan.setProperty("value", 70)
        self.progressBarScan.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBarScan.setInvertedAppearance(False)
        self.progressBarScan.setObjectName("progressBarScan")
        self.verticalLayout_4.addWidget(self.progressBarScan)
        self.lblStatus = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lblStatus.setFont(font)
        self.lblStatus.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblStatus.setStyleSheet("color: rgb(181, 61, 0);")
        self.lblStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.lblStatus.setObjectName("lblStatus")
        self.verticalLayout_4.addWidget(self.lblStatus)
        self.logToolBar.addLayout(self.verticalLayout_4)
        self.btnClearLog = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnClearLog.setFont(font)
        self.btnClearLog.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnClearLog.setStyleSheet("color: rgb(181, 61, 0);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("e:\\MyProjects\\Antivirus\\TAV\\views\\icons/eraser_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClearLog.setIcon(icon2)
        self.btnClearLog.setObjectName("btnClearLog")
        self.logToolBar.addWidget(self.btnClearLog)
        self.btnCancel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnCancel.setFont(font)
        self.btnCancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCancel.setStyleSheet("color: rgb(181, 61, 0);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("e:\\MyProjects\\Antivirus\\TAV\\views\\icons/cancel_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancel.setIcon(icon3)
        self.btnCancel.setObjectName("btnCancel")
        self.logToolBar.addWidget(self.btnCancel)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 100, 631, 78))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.optionFullScan = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.optionFullScan.sizePolicy().hasHeightForWidth())
        self.optionFullScan.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.optionFullScan.setFont(font)
        self.optionFullScan.setStyleSheet("color: rgb(181, 61, 0);")
        self.optionFullScan.setChecked(True)
        self.optionFullScan.setObjectName("optionFullScan")
        self.verticalLayout.addWidget(self.optionFullScan)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.optionSpecificScan = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.optionSpecificScan.setFont(font)
        self.optionSpecificScan.setStyleSheet("color: rgb(181, 61, 0);")
        self.optionSpecificScan.setObjectName("optionSpecificScan")
        self.horizontalLayout_2.addWidget(self.optionSpecificScan)
        self.folderPath = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.folderPath.setEnabled(True)
        self.folderPath.setObjectName("folderPath")
        self.horizontalLayout_2.addWidget(self.folderPath)
        self.btnChooseFolder = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnChooseFolder.setEnabled(True)
        self.btnChooseFolder.setStyleSheet("color: rgb(181, 61, 0);")
        self.btnChooseFolder.setObjectName("btnChooseFolder")
        self.horizontalLayout_2.addWidget(self.btnChooseFolder)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.btnScan = QtWidgets.QPushButton(self.centralwidget)
        self.btnScan.setGeometry(QtCore.QRect(700, 95, 180, 75))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnScan.sizePolicy().hasHeightForWidth())
        self.btnScan.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btnScan.setFont(font)
        self.btnScan.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnScan.setStyleSheet("color: #f7931e;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("e:\\MyProjects\\Antivirus\\TAV\\views\\icons/scan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnScan.setIcon(icon4)
        self.btnScan.setIconSize(QtCore.QSize(40, 40))
        self.btnScan.setObjectName("btnScan")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 180, 861, 341))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("color: rgb(255, 0, 0);")
        self.tabWidget.setObjectName("tabWidget")
        self.tabAll = QtWidgets.QWidget()
        self.tabAll.setObjectName("tabAll")
        self.scrollArea = QtWidgets.QScrollArea(self.tabAll)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 865, 331))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 863, 329))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.logBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.logBrowser.setGeometry(QtCore.QRect(0, 0, 865, 331))
        self.logBrowser.setMaximumSize(QtCore.QSize(865, 360))
        self.logBrowser.setObjectName("logBrowser")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.tabAll, "")
        self.tabMalware = QtWidgets.QWidget()
        self.tabMalware.setObjectName("tabMalware")
        self.scrollAreaMalware = QtWidgets.QScrollArea(self.tabMalware)
        self.scrollAreaMalware.setGeometry(QtCore.QRect(0, 0, 865, 331))
        self.scrollAreaMalware.setWidgetResizable(True)
        self.scrollAreaMalware.setObjectName("scrollAreaMalware")
        self.scrollAreaWidgetContentsMalware = QtWidgets.QWidget()
        self.scrollAreaWidgetContentsMalware.setGeometry(QtCore.QRect(0, 0, 863, 329))
        self.scrollAreaWidgetContentsMalware.setObjectName("scrollAreaWidgetContentsMalware")
        self.logBrowserMalware = QtWidgets.QTextBrowser(self.scrollAreaWidgetContentsMalware)
        self.logBrowserMalware.setGeometry(QtCore.QRect(0, 0, 865, 331))
        self.logBrowserMalware.setMaximumSize(QtCore.QSize(865, 360))
        self.logBrowserMalware.setObjectName("logBrowserMalware")
        self.scrollAreaMalware.setWidget(self.scrollAreaWidgetContentsMalware)
        self.tabWidget.addTab(self.tabMalware, "")
        QuickScanLayout.setCentralWidget(self.centralwidget)

        self.retranslateUi(QuickScanLayout)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(QuickScanLayout)

    def retranslateUi(self, QuickScanLayout):
        _translate = QtCore.QCoreApplication.translate
        QuickScanLayout.setWindowTitle(_translate("QuickScanLayout", "Quick Scan"))
        self.lbl_name.setText(_translate("QuickScanLayout", "QUICK SCAN"))
        self.lblStatus.setText(_translate("QuickScanLayout", "Status"))
        self.btnClearLog.setText(_translate("QuickScanLayout", "Clear log"))
        self.btnCancel.setText(_translate("QuickScanLayout", "Cancel"))
        self.optionFullScan.setText(_translate("QuickScanLayout", "Full scan"))
        self.optionSpecificScan.setText(_translate("QuickScanLayout", "Specific scan"))
        self.btnChooseFolder.setText(_translate("QuickScanLayout", "Choose folder"))
        self.btnScan.setText(_translate("QuickScanLayout", "SCAN"))
        self.logBrowser.setHtml(_translate("QuickScanLayout", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAll), _translate("QuickScanLayout", "All"))
        self.logBrowserMalware.setHtml(_translate("QuickScanLayout", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMalware), _translate("QuickScanLayout", "Malware"))
