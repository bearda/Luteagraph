import sys
import os
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from mainwindow import Ui_MainWindow
from shutil import copy2
import datetime
import spidev

class MyWindowClass(QtWidgets.QMainWindow, Ui_MainWindow):
    fileList = []
    metaDict = {}
    saveDir = r'C:\Users\samke\Desktop\Tester'
    bus = 0
    device = 0

    def __init__(self, parent=None, name=None):
        super(MyWindowClass, self).__init__(parent)
        self.setupUi(self)
        
        # Initialize SPI
	spi = spidev.SpiDev()
	spi.open(bus, device)

	#recieved = spi.xfer(to_send)
	#print(str(recieved))
        

        # Home page connections
        self.JumpProject.clicked.connect(self.jump2Project)
        self.JumpManual.clicked.connect(self.jump2Manual)

        # Project page connections
        self.LoadFile.clicked.connect(self.loadFile)
        self.FileSelector.itemClicked.connect(self.dispMeta)

        # Manual page connections
	self.xHome.clicked.connect(self.homeX)

        #Link up to loaded files
        #print(os.listdir(self.saveDir))

        #Create metadata file



    def jump2Project(self):
        self.TabBar.setCurrentIndex(1)

    def jump2Manual(self):
        self.TabBar.setCurrentIndex(2)

    def loadFile(self):
        file = QtWidgets.QFileDialog.getOpenFileName(parent=self.parent(), caption='Select a Gcode file to upload to the project list.')
        copy2(file[0], self.saveDir)
        fileName = str.split(file[0], '/')[-1]
        self.fileList.append(fileName)
        item = QtWidgets.QListWidgetItem(self.fileList[-1])
        self.FileSelector.addItem(item)

        dateUpload = datetime.datetime.now()
        if (dateUpload.hour > 11):
            period = ' PM'
            if (dateUpload.hour == 12):
                hour = '12'
            else:
                hour = str(dateUpload.hour - 11)
        else:
            hour = str(dateUpload.hour)
            period = ' AM'
        dateUpload = str(dateUpload.month) + '/' + str(dateUpload.day) + '/' + str(
            dateUpload.year) + ' ' + hour + ':' + str(dateUpload.minute) + period

        if fileName not in self.metaDict.keys():
            self.metaDict[fileName] = dateUpload

    def dispMeta(self, name):
        path = self.saveDir + '\\' + name.text()
        sizeBytes = os.path.getsize(path)
        dateModified = datetime.datetime.fromtimestamp(os.path.getmtime(path))

        if (dateModified.hour > 11):
            period = ' PM'
            if (dateModified.hour == 12):
                hour = '12'
            else:
                hour = str(dateModified.hour - 11)
        else:
            hour = str(dateModified.hour)
            period = ' AM'
        dateModified = str(dateModified.month) + '/' + str(dateModified.day) + '/' + str(
            dateModified.year) + ' ' + hour + ':' + str(dateModified.minute) + period



        if (sizeBytes > 1000000):
            sizeBytes = str(round(float(sizeBytes) / 1000000, 2)) + ' MB'
        elif (sizeBytes > 1000):
            sizeBytes = str(round(float(sizeBytes) / 1000, 2)) + ' KB'
        else:
            sizeBytes = str(sizeBytes) + ' bytes'

        print(name.text())
        print(self.metaDict.keys())
        pallete = QtGui.QPalette()
        pallete.setColor(QtGui.QPalette.Foreground, QtGui.QColor(161,164,163))
        self.FileDescription.setPalette(pallete)

        self.FileDescription.setText('File path: ' + path + '\n\n' +
                                     'File size: ' + sizeBytes + '\n\n' +
                                     'Date last modified: ' + dateModified + '\n\n' +
                                     'Date uploaded: ' + self.metaDict[name.text()])

    def homeX(self):
        data = [0x03, 0b10000000]
        spi.xfer(data)
	recieved = spi.readbytes(2)
        print(recieved)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myWindow = MyWindowClass()
    myWindow.show()
    sys.exit(app.exec_())
