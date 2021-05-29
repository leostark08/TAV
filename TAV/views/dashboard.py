# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DashboardLayout(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.window = QtWidgets.QMainWindow()

    def setupUi(self, DashboardLayout):
        DashboardLayout.setObjectName("DashboardLayout")
        DashboardLayout.resize(900, 600)
        DashboardLayout.setMinimumSize(QtCore.QSize(900, 600))
        DashboardLayout.setMaximumSize(QtCore.QSize(900, 600))
        font = QtGui.QFont()
        font.setFamily("Arial")
        DashboardLayout.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("views/icons/tav_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DashboardLayout.setWindowIcon(icon)
        DashboardLayout.setAutoFillBackground(False)
        DashboardLayout.setStyleSheet("background-color: #ffffff;")
        self.centralwidget = QtWidgets.QWidget(DashboardLayout)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_logo = QtWidgets.QLabel(self.centralwidget)
        self.lbl_logo.setGeometry(QtCore.QRect(25, 0, 100, 100))
        font = QtGui.QFont()
        self.lbl_logo.setFont(font)
        self.lbl_logo.setText("")
        self.lbl_logo.setPixmap(QtGui.QPixmap("views/icons/tav_logo.png"))
        self.lbl_logo.setScaledContents(True)
        self.lbl_logo.setObjectName("lbl_logo")
        self.lbl_decription = QtWidgets.QLabel(self.centralwidget)
        self.lbl_decription.setGeometry(QtCore.QRect(0, 100, 150, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_decription.setFont(font)
        self.lbl_decription.setAutoFillBackground(False)
        self.lbl_decription.setStyleSheet("color: rgb(181, 61, 0); color: #f7931e;")
        self.lbl_decription.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_decription.setObjectName("lbl_decription")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(570, 30, 298, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.horizontalLayoutWidget.setFont(font)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnOptions = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.btnOptions.setFont(font)
        self.btnOptions.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnOptions.setStyleSheet("background-color: rgb(255, 255, 255); color: #f7931e;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("views/icons/options.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOptions.setIcon(icon1)
        self.btnOptions.setObjectName("btnOptions")
        self.horizontalLayout.addWidget(self.btnOptions)
        self.btnAccount = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.btnAccount.setFont(font)
        self.btnAccount.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAccount.setStyleSheet("background-color: rgb(255, 255, 255); color: #f7931e;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("views/icons/personal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAccount.setIcon(icon2)
        self.btnAccount.setObjectName("btnAccount")
        self.horizontalLayout.addWidget(self.btnAccount)
        self.btnSettings = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.btnSettings.setFont(font)
        self.btnSettings.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSettings.setStyleSheet("background-color: rgb(255, 255, 255); color: #f7931e;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("views/icons/setting_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSettings.setIcon(icon3)
        self.btnSettings.setObjectName("btnSettings")
        self.horizontalLayout.addWidget(self.btnSettings)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 170, 841, 191))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.horizontalLayoutWidget_2.setFont(font)
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnQuickScan = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnQuickScan.sizePolicy().hasHeightForWidth())
        self.btnQuickScan.setSizePolicy(sizePolicy)
        self.btnQuickScan.setMinimumSize(QtCore.QSize(100, 150))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btnQuickScan.setFont(font)
        self.btnQuickScan.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnQuickScan.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.btnQuickScan.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnQuickScan.setAutoFillBackground(False)
        self.btnQuickScan.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "font: 75 13pt \"Arial\";\n"
                                        "color: rgb(181, 61, 0);")
        self.btnQuickScan.setInputMethodHints(QtCore.Qt.ImhNone)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("views/icons/quick.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnQuickScan.setIcon(icon4)
        self.btnQuickScan.setIconSize(QtCore.QSize(60, 60))
        self.btnQuickScan.setCheckable(False)
        self.btnQuickScan.setAutoDefault(False)
        self.btnQuickScan.setObjectName("btnQuickScan")
        self.horizontalLayout_2.addWidget(self.btnQuickScan)
        self.btnDeepScan = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDeepScan.sizePolicy().hasHeightForWidth())
        self.btnDeepScan.setSizePolicy(sizePolicy)
        self.btnDeepScan.setMinimumSize(QtCore.QSize(100, 150))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btnDeepScan.setFont(font)
        self.btnDeepScan.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnDeepScan.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.btnDeepScan.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnDeepScan.setAutoFillBackground(False)
        self.btnDeepScan.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "font: 75 13pt \"Arial\";\n"
                                       "color: rgb(181, 61, 0);")
        self.btnDeepScan.setInputMethodHints(QtCore.Qt.ImhNone)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("views/icons/deep.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDeepScan.setIcon(icon5)
        self.btnDeepScan.setIconSize(QtCore.QSize(60, 60))
        self.btnDeepScan.setCheckable(False)
        self.btnDeepScan.setAutoDefault(False)
        self.btnDeepScan.setObjectName("btnDeepScan")
        self.horizontalLayout_2.addWidget(self.btnDeepScan)
        self.btnSchedulerScan = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSchedulerScan.sizePolicy().hasHeightForWidth())
        self.btnSchedulerScan.setSizePolicy(sizePolicy)
        self.btnSchedulerScan.setMinimumSize(QtCore.QSize(100, 150))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btnSchedulerScan.setFont(font)
        self.btnSchedulerScan.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSchedulerScan.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.btnSchedulerScan.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnSchedulerScan.setAutoFillBackground(False)
        self.btnSchedulerScan.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "font: 75 13pt \"Arial\";\n"
                                            "color: rgb(181, 61, 0);")
        self.btnSchedulerScan.setInputMethodHints(QtCore.Qt.ImhNone)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("views/icons/schedule.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSchedulerScan.setIcon(icon6)
        self.btnSchedulerScan.setIconSize(QtCore.QSize(60, 60))
        self.btnSchedulerScan.setCheckable(False)
        self.btnSchedulerScan.setAutoDefault(False)
        self.btnSchedulerScan.setObjectName("btnSchedulerScan")
        self.horizontalLayout_2.addWidget(self.btnSchedulerScan)
        self.btnDiskCleanup = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDiskCleanup.sizePolicy().hasHeightForWidth())
        self.btnDiskCleanup.setSizePolicy(sizePolicy)
        self.btnDiskCleanup.setMinimumSize(QtCore.QSize(100, 150))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btnDiskCleanup.setFont(font)
        self.btnDiskCleanup.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnDiskCleanup.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.btnDiskCleanup.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnDiskCleanup.setAutoFillBackground(False)
        self.btnDiskCleanup.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "font: 75 13pt \"Arial\";\n"
                                          "color: rgb(181, 61, 0);")
        self.btnDiskCleanup.setInputMethodHints(QtCore.Qt.ImhNone)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("views/icons/cleanup.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDiskCleanup.setIcon(icon7)
        self.btnDiskCleanup.setIconSize(QtCore.QSize(60, 60))
        self.btnDiskCleanup.setCheckable(False)
        self.btnDiskCleanup.setAutoDefault(False)
        self.btnDiskCleanup.setObjectName("btnDiskCleanup")
        self.horizontalLayout_2.addWidget(self.btnDiskCleanup)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 440, 841, 52))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.horizontalLayoutWidget_3.setFont(font)
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnHistory = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnHistory.sizePolicy().hasHeightForWidth())
        self.btnHistory.setSizePolicy(sizePolicy)
        self.btnHistory.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btnHistory.setFont(font)
        self.btnHistory.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnHistory.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "font: 75 11pt \"Arial\";\n"
                                      "color: rgb(181, 61, 0);")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("views/icons/history.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnHistory.setIcon(icon8)
        self.btnHistory.setIconSize(QtCore.QSize(40, 40))
        self.btnHistory.setObjectName("btnHistory")
        self.horizontalLayout_3.addWidget(self.btnHistory)
        self.btnPrivacy = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPrivacy.sizePolicy().hasHeightForWidth())
        self.btnPrivacy.setSizePolicy(sizePolicy)
        self.btnPrivacy.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btnPrivacy.setFont(font)
        self.btnPrivacy.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnPrivacy.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "font: 75 11pt \"Arial\";\n"
                                      "color: rgb(181, 61, 0);")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("views/icons/privacy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPrivacy.setIcon(icon9)
        self.btnPrivacy.setIconSize(QtCore.QSize(40, 40))
        self.btnPrivacy.setObjectName("btnPrivacy")
        self.horizontalLayout_3.addWidget(self.btnPrivacy)
        self.btnSupport = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSupport.sizePolicy().hasHeightForWidth())
        self.btnSupport.setSizePolicy(sizePolicy)
        self.btnSupport.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btnSupport.setFont(font)
        self.btnSupport.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSupport.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "font: 75 11pt \"Arial\";\n"
                                      "color: rgb(181, 61, 0);")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("views/icons/support.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSupport.setIcon(icon10)
        self.btnSupport.setIconSize(QtCore.QSize(40, 40))
        self.btnSupport.setObjectName("btnSupport")
        self.horizontalLayout_3.addWidget(self.btnSupport)
        DashboardLayout.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DashboardLayout)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 26))
        self.menubar.setObjectName("menubar")
        DashboardLayout.setMenuBar(self.menubar)

        self.retranslateUi(DashboardLayout)
        QtCore.QMetaObject.connectSlotsByName(DashboardLayout)

    def retranslateUi(self, DashboardLayout):
        _translate = QtCore.QCoreApplication.translate
        DashboardLayout.setWindowTitle(_translate("DashboardLayout", "VKU Antivirus"))
        self.lbl_decription.setText(_translate("DashboardLayout", "VKU Antivirus"))
        self.btnOptions.setText(_translate("DashboardLayout", "Options"))
        self.btnAccount.setText(_translate("DashboardLayout", "Account"))
        self.btnSettings.setText(_translate("DashboardLayout", "Settings"))
        self.btnQuickScan.setText(_translate("DashboardLayout", "Quick Scan"))
        self.btnDeepScan.setText(_translate("DashboardLayout", "Deep Scan"))
        self.btnSchedulerScan.setText(_translate("DashboardLayout", "Scheduler Scan"))
        self.btnDiskCleanup.setText(_translate("DashboardLayout", "Disk Cleanup"))
        self.btnHistory.setText(_translate("DashboardLayout", "History"))
        self.btnPrivacy.setText(_translate("DashboardLayout", "Privacy"))
        self.btnSupport.setText(_translate("DashboardLayout", "Support"))

