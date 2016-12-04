# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 440)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(800, 440))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.centralWidget.setFont(font)
        self.centralWidget.setObjectName("centralWidget")
        self.TabBar = QtWidgets.QTabWidget(self.centralWidget)
        self.TabBar.setGeometry(QtCore.QRect(0, 0, 800, 441))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TabBar.sizePolicy().hasHeightForWidth())
        self.TabBar.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(83, 81, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 81, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 81, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 99, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 81, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 81, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 81, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 99, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 81, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 81, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 81, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 153, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.TabBar.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.TabBar.setFont(font)
        self.TabBar.setAutoFillBackground(False)
        self.TabBar.setStyleSheet("background-color: rgb(83, 81, 90);\n"
"\n"
"")
        self.TabBar.setObjectName("TabBar")
        self.Home = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Home.sizePolicy().hasHeightForWidth())
        self.Home.setSizePolicy(sizePolicy)
        self.Home.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.Home.setStyleSheet("ui->Wdgt_Inbox->tabBar()->setCurrentIndex(0);\n"
"ui->Wdgt_Inbox->tabBar()->setStyleSheet(\"background-color:grey;\");\n"
"ui->Wdgt_Inbox->tabBar()->setStyleSheet(\"QWidget { background-color:grey; }\");\n"
"ui->Tab_Inbox->setStyleSheet(\"background-color:grey;\");")
        self.Home.setObjectName("Home")
        self.JumpProject = QtWidgets.QPushButton(self.Home)
        self.JumpProject.setGeometry(QtCore.QRect(30, 290, 361, 91))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.JumpProject.setFont(font)
        self.JumpProject.setStyleSheet("background-color: rgb(161, 164, 163);\n"
"border-bottom-left-radius: 7px;\n"
"color: rgb(55, 52, 48);\n"
"\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/new/prefix1/Icons/Plus36.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.JumpProject.setIcon(icon)
        self.JumpProject.setObjectName("JumpProject")
        self.label_3 = QtWidgets.QLabel(self.Home)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 731, 141))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(39)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("background-color: rgb(22, 27, 34);\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.Home)
        self.label_7.setGeometry(QtCore.QRect(30, 20, 731, 141))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border-top-right-radius: 7px;\n"
"border-top-left-radius: 7px;\n"
"background-color: rgb(22, 27, 34);\n"
"\n"
"\n"
"")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/new/prefix1/Icons/Pig80.png"))
        self.label_7.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.Home)
        self.label_8.setGeometry(QtCore.QRect(30, 20, 731, 271))
        self.label_8.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-width: 3px;\n"
"border-color: rgb(161, 164, 163);\n"
"border-top-right-radius: 7px;\n"
"border-top-left-radius: 7px;\n"
"border-style: solid;\n"
"\n"
"\n"
"")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.JumpManual = QtWidgets.QPushButton(self.Home)
        self.JumpManual.setGeometry(QtCore.QRect(390, 290, 371, 91))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.JumpManual.setFont(font)
        self.JumpManual.setStyleSheet("background-color: rgb(161, 164, 163);\n"
"border-bottom-right-radius: 7px;\n"
"color: rgb(55, 52, 48);\n"
"\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/new/prefix1/Icons/Hand36.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.JumpManual.setIcon(icon1)
        self.JumpManual.setObjectName("JumpManual")
        self.line = QtWidgets.QFrame(self.Home)
        self.line.setGeometry(QtCore.QRect(390, 290, 3, 60))
        self.line.setStyleSheet("border-style:solid;\n"
"border-width:1px;\n"
"border-color: rgb(172, 99, 22);\n"
"background-color: rgb(172, 99, 22);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.Home)
        self.line_2.setGeometry(QtCore.QRect(390, 300, 3, 61))
        self.line_2.setStyleSheet("border-style:solid;\n"
"border-width:1px;\n"
"border-color: rgb(172, 99, 22);\n"
"background-color: rgb(172, 99, 22);")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_9 = QtWidgets.QLabel(self.Home)
        self.label_9.setGeometry(QtCore.QRect(480, 230, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_9.setObjectName("label_9")
        self.JumpManual.raise_()
        self.JumpProject.raise_()
        self.label_7.raise_()
        self.label_3.raise_()
        self.label_8.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.label_9.raise_()
        self.TabBar.addTab(self.Home, "")
        self.Project = QtWidgets.QWidget()
        self.Project.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.Project.setObjectName("Project")
        self.LoadFile = QtWidgets.QPushButton(self.Project)
        self.LoadFile.setGeometry(QtCore.QRect(30, 350, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.LoadFile.setFont(font)
        self.LoadFile.setStyleSheet("background-color: rgb(172, 99, 22);\n"
"border-style:solid;\n"
"border-bottom-right-radius:3px;\n"
"border-bottom-left-radius:3px;\n"
"color:rgb(161, 164, 163);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/new/prefix1/Icons/Plus25_whitish.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LoadFile.setIcon(icon2)
        self.LoadFile.setObjectName("LoadFile")
        self.Start = QtWidgets.QPushButton(self.Project)
        self.Start.setGeometry(QtCore.QRect(270, 20, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.Start.setFont(font)
        self.Start.setStyleSheet("background-color: rgb(172, 99, 22);\n"
"border-style: solid;\n"
"border-radius: 4px;\n"
"color:rgb(161, 164, 163);")
        self.Start.setObjectName("Start")
        self.ProgressBar = QtWidgets.QProgressBar(self.Project)
        self.ProgressBar.setGeometry(QtCore.QRect(480, 20, 281, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(161, 164, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 32, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(161, 164, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(161, 164, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 32, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 32, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 99, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(161, 164, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 32, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(161, 164, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(161, 164, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 32, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 32, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 99, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(161, 164, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 32, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(161, 164, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(161, 164, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 32, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 32, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 153, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.ProgressBar.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.ProgressBar.setFont(font)
        self.ProgressBar.setStyleSheet("color: rgb(161, 164, 163);\n"
"background-color: rgb(27, 32, 39);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-color: rgb(172, 99, 22);\n"
"border-radius:5px;\n"
"")
        self.ProgressBar.setMaximum(100)
        self.ProgressBar.setProperty("value", 0)
        self.ProgressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.ProgressBar.setObjectName("ProgressBar")
        self.FileSelector = QtWidgets.QListWidget(self.Project)
        self.FileSelector.setGeometry(QtCore.QRect(30, 20, 211, 331))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FileSelector.sizePolicy().hasHeightForWidth())
        self.FileSelector.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.FileSelector.setFont(font)
        self.FileSelector.setStyleSheet("background-color: rgb(27, 32, 39);\n"
"border-top-left-radius: 3px;\n"
"border-top-right-radius: 3px;\n"
"border-style: solid;\n"
"border-color:rgb(172, 99, 22);\n"
"border-width:1px;\n"
"color: rgb(161, 164, 163);\n"
"")
        self.FileSelector.setObjectName("FileSelector")
        self.Pause = QtWidgets.QPushButton(self.Project)
        self.Pause.setGeometry(QtCore.QRect(270, 90, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.Pause.setFont(font)
        self.Pause.setStyleSheet("background-color: rgb(172, 99, 22);\n"
"border-style: solid;\n"
"border-radius: 4px;\n"
"color: rgb(161, 164, 163) ")
        self.Pause.setObjectName("Pause")
        self.Stop = QtWidgets.QPushButton(self.Project)
        self.Stop.setGeometry(QtCore.QRect(270, 160, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.Stop.setFont(font)
        self.Stop.setStyleSheet("background-color: rgb(172, 99, 22);\n"
"border-style: solid;\n"
"border-radius: 4px;\n"
"color: rgb(161, 164, 163);")
        self.Stop.setObjectName("Stop")
        self.FileDescription = QtWidgets.QLabel(self.Project)
        self.FileDescription.setGeometry(QtCore.QRect(270, 230, 491, 151))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.FileDescription.setFont(font)
        self.FileDescription.setStyleSheet("background-color: rgb(27, 32, 39);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"border-color:rgb(172, 99, 22)")
        self.FileDescription.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.FileDescription.setObjectName("FileDescription")
        self.TimeEstimate = QtWidgets.QLabel(self.Project)
        self.TimeEstimate.setGeometry(QtCore.QRect(480, 60, 271, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.TimeEstimate.setFont(font)
        self.TimeEstimate.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.TimeEstimate.setObjectName("TimeEstimate")
        self.speedDispProj = QtWidgets.QLabel(self.Project)
        self.speedDispProj.setGeometry(QtCore.QRect(580, 120, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.speedDispProj.setFont(font)
        self.speedDispProj.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.speedDispProj.setAlignment(QtCore.Qt.AlignCenter)
        self.speedDispProj.setObjectName("speedDispProj")
        self.speedUpProj = QtWidgets.QPushButton(self.Project)
        self.speedUpProj.setGeometry(QtCore.QRect(670, 110, 51, 51))
        self.speedUpProj.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-color:rgb(161, 164, 163);")
        self.speedUpProj.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/new/prefix1/Icons/Right50W.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.speedUpProj.setIcon(icon3)
        self.speedUpProj.setIconSize(QtCore.QSize(30, 30))
        self.speedUpProj.setObjectName("speedUpProj")
        self.label_56 = QtWidgets.QLabel(self.Project)
        self.label_56.setGeometry(QtCore.QRect(580, 100, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.label_56.setFont(font)
        self.label_56.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_56.setAlignment(QtCore.Qt.AlignCenter)
        self.label_56.setObjectName("label_56")
        self.speedDownProj = QtWidgets.QPushButton(self.Project)
        self.speedDownProj.setGeometry(QtCore.QRect(520, 110, 51, 51))
        self.speedDownProj.setStyleSheet("background-color: rgb(22, 27, 34);\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-color:rgb(161, 164, 163);")
        self.speedDownProj.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/new/prefix1/Icons/Left50W.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.speedDownProj.setIcon(icon4)
        self.speedDownProj.setIconSize(QtCore.QSize(30, 30))
        self.speedDownProj.setObjectName("speedDownProj")
        self.FileDescription_4 = QtWidgets.QLabel(self.Project)
        self.FileDescription_4.setGeometry(QtCore.QRect(500, 90, 241, 91))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.FileDescription_4.setFont(font)
        self.FileDescription_4.setStyleSheet("background-color: rgb(27, 32, 39);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"border-color:rgb(172, 99, 22)")
        self.FileDescription_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.FileDescription_4.setObjectName("FileDescription_4")
        self.FileDescription_4.raise_()
        self.LoadFile.raise_()
        self.Start.raise_()
        self.ProgressBar.raise_()
        self.Pause.raise_()
        self.Stop.raise_()
        self.FileSelector.raise_()
        self.FileDescription.raise_()
        self.TimeEstimate.raise_()
        self.speedDispProj.raise_()
        self.speedUpProj.raise_()
        self.label_56.raise_()
        self.speedDownProj.raise_()
        self.TabBar.addTab(self.Project, "")
        self.Manual = QtWidgets.QWidget()
        self.Manual.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.Manual.setObjectName("Manual")
        self.xPos = QtWidgets.QPushButton(self.Manual)
        self.xPos.setGeometry(QtCore.QRect(210, 120, 51, 51))
        self.xPos.setStyleSheet("background-color: rgb(22, 27, 34);\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-color:rgb(161, 164, 163);")
        self.xPos.setText("")
        self.xPos.setIcon(icon3)
        self.xPos.setIconSize(QtCore.QSize(30, 30))
        self.xPos.setObjectName("xPos")
        self.label_4 = QtWidgets.QLabel(self.Manual)
        self.label_4.setGeometry(QtCore.QRect(140, 120, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setMouseTracking(True)
        self.label_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.yNeg = QtWidgets.QPushButton(self.Manual)
        self.yNeg.setGeometry(QtCore.QRect(140, 190, 51, 51))
        self.yNeg.setStyleSheet("background-color: rgb(22, 27, 34);\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-color:rgb(161, 164, 163);")
        self.yNeg.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/new/prefix1/Icons/Down50W.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.yNeg.setIcon(icon5)
        self.yNeg.setIconSize(QtCore.QSize(30, 30))
        self.yNeg.setObjectName("yNeg")
        self.xNeg = QtWidgets.QPushButton(self.Manual)
        self.xNeg.setGeometry(QtCore.QRect(70, 120, 51, 51))
        self.xNeg.setStyleSheet("background-color: rgb(22, 27, 34);\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-color:rgb(161, 164, 163);")
        self.xNeg.setText("")
        self.xNeg.setIcon(icon4)
        self.xNeg.setIconSize(QtCore.QSize(30, 30))
        self.xNeg.setObjectName("xNeg")
        self.yPos = QtWidgets.QPushButton(self.Manual)
        self.yPos.setGeometry(QtCore.QRect(140, 50, 51, 51))
        self.yPos.setStyleSheet("background-color: rgb(22, 27, 34);\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-color:rgb(161, 164, 163);")
        self.yPos.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/new/prefix1/Icons/Up50W.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.yPos.setIcon(icon6)
        self.yPos.setIconSize(QtCore.QSize(30, 30))
        self.yPos.setObjectName("yPos")
        self.xHome = QtWidgets.QPushButton(self.Manual)
        self.xHome.setGeometry(QtCore.QRect(50, 310, 51, 51))
        self.xHome.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-color:rgb(161, 164, 163);\n"
"font: 14pt \"Arial Rounded MT Bold\";\n"
"color:rgb(22, 27, 34);")
        self.xHome.setIconSize(QtCore.QSize(25, 25))
        self.xHome.setObjectName("xHome")
        self.pushButton_13 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_13.setGeometry(QtCore.QRect(50, 310, 51, 51))
        self.pushButton_13.setStyleSheet("background-color: rgb(22, 27, 34);\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-color:rgb(161, 164, 163);")
        self.pushButton_13.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/new/prefix1/Icons/Home50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_13.setIcon(icon7)
        self.pushButton_13.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_13.setObjectName("pushButton_13")
        self.label_2 = QtWidgets.QLabel(self.Manual)
        self.label_2.setGeometry(QtCore.QRect(130, 110, 71, 71))
        self.label_2.setStyleSheet("background-color: rgb(22, 27, 34);\n"
"border-style: solid;\n"
"border-radius: 35px;\n"
"border-color: rgb(172, 99, 22);\n"
"border-width: 2px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_12 = QtWidgets.QLabel(self.Manual)
        self.label_12.setGeometry(QtCore.QRect(100, 80, 131, 131))
        self.label_12.setStyleSheet("background-color: rgb(22, 27, 34);\n"
"border-style: solid;\n"
"border-radius: 65px;\n"
"border-color: rgb(172, 99, 22);\n"
"border-width: 5px;")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label = QtWidgets.QLabel(self.Manual)
        self.label.setGeometry(QtCore.QRect(30, 20, 731, 251))
        font = QtGui.QFont()
        font.setFamily("Informal Roman")
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(22, 27, 34);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"border-color:rgb(172, 99, 22)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.Manual)
        self.label_5.setGeometry(QtCore.QRect(370, 120, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setMouseTracking(True)
        self.label_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.zPos = QtWidgets.QPushButton(self.Manual)
        self.zPos.setGeometry(QtCore.QRect(370, 50, 51, 51))
        self.zPos.setStyleSheet("background-color: rgb(22, 27, 34);\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-color:rgb(161, 164, 163);")
        self.zPos.setText("")
        self.zPos.setIcon(icon6)
        self.zPos.setIconSize(QtCore.QSize(30, 30))
        self.zPos.setObjectName("zPos")
        self.zNeg = QtWidgets.QPushButton(self.Manual)
        self.zNeg.setGeometry(QtCore.QRect(370, 190, 51, 51))
        self.zNeg.setStyleSheet("background-color: rgb(22, 27, 34);\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-color:rgb(161, 164, 163);")
        self.zNeg.setText("")
        self.zNeg.setIcon(icon5)
        self.zNeg.setIconSize(QtCore.QSize(30, 30))
        self.zNeg.setObjectName("zNeg")
        self.label_34 = QtWidgets.QLabel(self.Manual)
        self.label_34.setGeometry(QtCore.QRect(360, 110, 71, 71))
        self.label_34.setStyleSheet("background-color: rgb(22, 27, 34);\n"
"border-style: solid;\n"
"border-radius: 35px;\n"
"border-color: rgb(172, 99, 22);\n"
"border-width: 2px;")
        self.label_34.setText("")
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.Manual)
        self.label_35.setGeometry(QtCore.QRect(330, 80, 131, 131))
        self.label_35.setStyleSheet("background-color: rgb(22, 27, 34);\n"
"border-style: solid;\n"
"border-radius: 65px;\n"
"border-color: rgb(172, 99, 22);\n"
"border-width: 5px;")
        self.label_35.setText("")
        self.label_35.setObjectName("label_35")
        self.label_13 = QtWidgets.QLabel(self.Manual)
        self.label_13.setGeometry(QtCore.QRect(600, 120, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setMouseTracking(True)
        self.label_13.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.Manual)
        self.label_14.setGeometry(QtCore.QRect(590, 110, 71, 71))
        self.label_14.setStyleSheet("background-color: rgb(22, 27, 34);\n"
"border-style: solid;\n"
"border-radius: 35px;\n"
"border-color: rgb(172, 99, 22);\n"
"border-width: 2px;")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.Manual)
        self.label_15.setGeometry(QtCore.QRect(560, 80, 131, 131))
        self.label_15.setStyleSheet("background-color: rgb(22, 27, 34);\n"
"border-style: solid;\n"
"border-radius: 65px;\n"
"border-color: rgb(172, 99, 22);\n"
"border-width: 5px;")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.thetaCCW = QtWidgets.QPushButton(self.Manual)
        self.thetaCCW.setGeometry(QtCore.QRect(670, 120, 51, 51))
        self.thetaCCW.setStyleSheet("background-color: rgb(22, 27, 34);\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-color:rgb(161, 164, 163);")
        self.thetaCCW.setText("")
        self.thetaCCW.setIcon(icon6)
        self.thetaCCW.setIconSize(QtCore.QSize(30, 30))
        self.thetaCCW.setObjectName("thetaCCW")
        self.thetaCW = QtWidgets.QPushButton(self.Manual)
        self.thetaCW.setGeometry(QtCore.QRect(530, 120, 51, 51))
        self.thetaCW.setStyleSheet("background-color: rgb(22, 27, 34);\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-color:rgb(161, 164, 163);")
        self.thetaCW.setText("")
        self.thetaCW.setIcon(icon6)
        self.thetaCW.setIconSize(QtCore.QSize(30, 30))
        self.thetaCW.setObjectName("thetaCW")
        self.speedDownManual = QtWidgets.QPushButton(self.Manual)
        self.speedDownManual.setGeometry(QtCore.QRect(300, 280, 51, 51))
        self.speedDownManual.setStyleSheet("background-color: rgb(22, 27, 34);\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-color:rgb(161, 164, 163);")
        self.speedDownManual.setText("")
        self.speedDownManual.setIcon(icon4)
        self.speedDownManual.setIconSize(QtCore.QSize(30, 30))
        self.speedDownManual.setObjectName("speedDownManual")
        self.speedUpManual = QtWidgets.QPushButton(self.Manual)
        self.speedUpManual.setGeometry(QtCore.QRect(440, 280, 51, 51))
        self.speedUpManual.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-color:rgb(161, 164, 163);")
        self.speedUpManual.setText("")
        self.speedUpManual.setIcon(icon3)
        self.speedUpManual.setIconSize(QtCore.QSize(30, 30))
        self.speedUpManual.setObjectName("speedUpManual")
        self.label_11 = QtWidgets.QLabel(self.Manual)
        self.label_11.setGeometry(QtCore.QRect(360, 270, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.speedDispManual = QtWidgets.QLabel(self.Manual)
        self.speedDispManual.setGeometry(QtCore.QRect(360, 290, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.speedDispManual.setFont(font)
        self.speedDispManual.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.speedDispManual.setAlignment(QtCore.Qt.AlignCenter)
        self.speedDispManual.setObjectName("speedDispManual")
        self.label_31 = QtWidgets.QLabel(self.Manual)
        self.label_31.setGeometry(QtCore.QRect(30, 290, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Informal Roman")
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("background-color: rgb(22, 27, 34);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"border-color:rgb(172, 99, 22)")
        self.label_31.setText("")
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.Manual)
        self.label_32.setGeometry(QtCore.QRect(280, 270, 231, 81))
        font = QtGui.QFont()
        font.setFamily("Informal Roman")
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("background-color: rgb(22, 27, 34);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-bottom-left-radius: 4px;\n"
"border-bottom-right-radius: 4px;\n"
"border-left-color:rgb(172, 99, 22);\n"
"border-right-color:rgb(172, 99, 22);\n"
"border-bottom-color:rgb(172, 99, 22);\n"
"border-top-color:rgb(22, 27, 34);")
        self.label_32.setText("")
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.Manual)
        self.label_33.setGeometry(QtCore.QRect(530, 290, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Informal Roman")
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("background-color: rgb(22, 27, 34);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"border-color:rgb(172, 99, 22)")
        self.label_33.setText("")
        self.label_33.setObjectName("label_33")
        self.servoPower = QtWidgets.QPushButton(self.Manual)
        self.servoPower.setGeometry(QtCore.QRect(680, 310, 51, 51))
        self.servoPower.setStyleSheet("background-color: rgb(22, 27, 34);\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-color:rgb(161, 164, 163);")
        self.servoPower.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../../../Desktop/a1a4a3-stepper-motor-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.servoPower.setIcon(icon8)
        self.servoPower.setIconSize(QtCore.QSize(25, 25))
        self.servoPower.setObjectName("servoPower")
        self.yHome = QtWidgets.QPushButton(self.Manual)
        self.yHome.setGeometry(QtCore.QRect(120, 310, 51, 51))
        self.yHome.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-color:rgb(161, 164, 163);\n"
"font: 14pt \"Arial Rounded MT Bold\";\n"
"color:rgb(22, 27, 34);")
        self.yHome.setIconSize(QtCore.QSize(25, 25))
        self.yHome.setObjectName("yHome")
        self.pushButton_17 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_17.setGeometry(QtCore.QRect(120, 310, 51, 51))
        self.pushButton_17.setStyleSheet("background-color: rgb(22, 27, 34);\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-color:rgb(161, 164, 163);")
        self.pushButton_17.setText("")
        self.pushButton_17.setIcon(icon7)
        self.pushButton_17.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_17.setObjectName("pushButton_17")
        self.zHome = QtWidgets.QPushButton(self.Manual)
        self.zHome.setGeometry(QtCore.QRect(190, 310, 51, 51))
        self.zHome.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-color:rgb(161, 164, 163);\n"
"font: 14pt \"Arial Rounded MT Bold\";\n"
"color:rgb(22, 27, 34);")
        self.zHome.setIconSize(QtCore.QSize(25, 25))
        self.zHome.setObjectName("zHome")
        self.pushButton_19 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_19.setGeometry(QtCore.QRect(190, 310, 51, 51))
        self.pushButton_19.setStyleSheet("background-color: rgb(22, 27, 34);\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-color:rgb(161, 164, 163);")
        self.pushButton_19.setText("")
        self.pushButton_19.setIcon(icon7)
        self.pushButton_19.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_19.setObjectName("pushButton_19")
        self.thetaHome = QtWidgets.QPushButton(self.Manual)
        self.thetaHome.setGeometry(QtCore.QRect(550, 310, 51, 51))
        self.thetaHome.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-color:rgb(161, 164, 163);\n"
"font: 75 15pt \"Symbol\";\n"
"color:rgb(22, 27, 34);\n"
"")
        self.thetaHome.setIconSize(QtCore.QSize(25, 25))
        self.thetaHome.setObjectName("thetaHome")
        self.pushButton_21 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_21.setGeometry(QtCore.QRect(550, 310, 51, 51))
        self.pushButton_21.setStyleSheet("background-color: rgb(22, 27, 34);\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-color:rgb(161, 164, 163);")
        self.pushButton_21.setText("")
        self.pushButton_21.setIcon(icon7)
        self.pushButton_21.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_21.setObjectName("pushButton_21")
        self.allHome = QtWidgets.QPushButton(self.Manual)
        self.allHome.setGeometry(QtCore.QRect(620, 310, 51, 51))
        self.allHome.setStyleSheet("background-color: rgb(22, 27, 34);\n"
"border-style: solid;\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-color:rgb(161, 164, 163);")
        self.allHome.setText("")
        self.allHome.setIcon(icon7)
        self.allHome.setIconSize(QtCore.QSize(25, 25))
        self.allHome.setObjectName("allHome")
        self.label_33.raise_()
        self.servoPower.raise_()
        self.label.raise_()
        self.label_32.raise_()
        self.label_31.raise_()
        self.label_35.raise_()
        self.label_12.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.yNeg.raise_()
        self.xNeg.raise_()
        self.yPos.raise_()
        self.pushButton_13.raise_()
        self.xPos.raise_()
        self.zPos.raise_()
        self.zNeg.raise_()
        self.label_34.raise_()
        self.label_5.raise_()
        self.label_15.raise_()
        self.label_14.raise_()
        self.label_13.raise_()
        self.thetaCCW.raise_()
        self.thetaCW.raise_()
        self.speedDownManual.raise_()
        self.speedUpManual.raise_()
        self.label_11.raise_()
        self.speedDispManual.raise_()
        self.xHome.raise_()
        self.pushButton_17.raise_()
        self.pushButton_19.raise_()
        self.pushButton_21.raise_()
        self.yHome.raise_()
        self.zHome.raise_()
        self.thetaHome.raise_()
        self.allHome.raise_()
        self.TabBar.addTab(self.Manual, "")
        self.Error = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Error.sizePolicy().hasHeightForWidth())
        self.Error.setSizePolicy(sizePolicy)
        self.Error.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.Error.setObjectName("Error")
        self.errorDisp = QtWidgets.QLabel(self.Error)
        self.errorDisp.setGeometry(QtCore.QRect(30, 20, 731, 361))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.errorDisp.setFont(font)
        self.errorDisp.setStyleSheet("background-color: rgb(27, 32, 39);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"border-color:rgb(172, 99, 22)")
        self.errorDisp.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.errorDisp.setObjectName("errorDisp")
        self.TabBar.addTab(self.Error, "")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.TabBar.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.JumpProject.setText(_translate("MainWindow", " new project"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ac6316;\">Luteagraph</span></p></body></html>"))
        self.JumpManual.setText(_translate("MainWindow", " manual control"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; color:#53515a;\">V.1.0</span></p></body></html>"))
        self.TabBar.setTabText(self.TabBar.indexOf(self.Home), _translate("MainWindow", "Home"))
        self.LoadFile.setText(_translate("MainWindow", " new project"))
        self.Start.setText(_translate("MainWindow", "Start"))
        self.FileSelector.setSortingEnabled(True)
        self.Pause.setText(_translate("MainWindow", "Pause"))
        self.Stop.setText(_translate("MainWindow", "Stop"))
        self.FileDescription.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.TimeEstimate.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#a1a4a3;\">Estimated time to completion:</span></p></body></html>"))
        self.speedDispProj.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#a1a4a3;\">100%</span></p></body></html>"))
        self.label_56.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#a1a4a3;\">Speed:</span></p></body></html>"))
        self.FileDescription_4.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.TabBar.setTabText(self.TabBar.indexOf(self.Project), _translate("MainWindow", "Project"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#a1a4a3;\">X/Y</span></p></body></html>"))
        self.xHome.setText(_translate("MainWindow", "X"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#a1a4a3;\">Z</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#a1a4a3;\">&theta;</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#a1a4a3;\">Speed:</span></p></body></html>"))
        self.speedDispManual.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#a1a4a3;\">1 mm</span></p></body></html>"))
        self.yHome.setText(_translate("MainWindow", "Y"))
        self.zHome.setText(_translate("MainWindow", "Z"))
        self.thetaHome.setText(_translate("MainWindow", "q"))
        self.TabBar.setTabText(self.TabBar.indexOf(self.Manual), _translate("MainWindow", "Manual"))
        self.errorDisp.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#a1a4a3;\">There are currently no errors.</span></p></body></html>"))
        self.TabBar.setTabText(self.TabBar.indexOf(self.Error), _translate("MainWindow", "Error Dialogue"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

