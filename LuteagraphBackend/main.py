import sys
import os
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from mainwindow import Ui_MainWindow
from shutil import copy2
import datetime
import spidev
from time import sleep
import parser


class MyWindowClass(QtWidgets.QMainWindow, Ui_MainWindow):
    fileList = []
    metaDict = {}
    saveDir = r'/home/cashe/Luteagraph/LuteagraphBackend/Gfiles'
    metaFile = r'/home/cashe/Luteagraph/LuteagraphBackend/metadata.txt'
    bus = 0
    device = 0
    readDelay = 0.1
    cmdDelay = 0.02
    jogIndex = 2
    jogSpeeds = [0.1, 0.5, 1, 5, 10, 50]
    projIndex = 9
    projSpeeds = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
    binRef = [0b000, 0b001, 0b010, 0b011, 0b100, 0b101, 0b110, 0b111]
    errors = 0
    started = False
    pause = False
    gCodeList = []

    # Commands
    jog = 0x02
    home = 0x03
    diagnostic = [0x04, 0x00]
    servo = 0x05
    gcode = 0x55
    heartbeat = 0x66


    def __init__(self, parent=None,):
        super(MyWindowClass, self).__init__(parent)
        self.setupUi(self)
        
        # Initialize SPI
        self.spi = spidev.SpiDev()
        self.spi.open(self.bus, self.device)
        self.spi.max_speed_hz = 50000
        self.spi.mode = 0b00

        #Initialize parser
        self.parse = parser.gcodeParser()

        # Home page connections
        self.JumpProject.clicked.connect(self.jump2Project)
        self.JumpManual.clicked.connect(self.jump2Manual)

        # Project page connections
        self.LoadFile.clicked.connect(self.loadFile)
        self.deleteFile.clicked.connect(self.removeFile)
        self.FileSelector.itemClicked.connect(self.dispMeta)
        self.speedUpProj.clicked.connect(self.projectAccelerate)
        self.speedDownProj.clicked.connect(self.projectDecelerate)
        self.Start.clicked.connect(self.projectStart)
        self.Pause.clicked.connect(self.projectPause)
        self.Stop.clicked.connect(self.projectStop)

        # Project page initializations
        self.Pause.setEnabled(False)
        self.Stop.setEnabled(False)

        # Manual page connections
        self.xHome.clicked.connect(self.homeX)
        self.yHome.clicked.connect(self.homeY)
        self.zHome.clicked.connect(self.homeZ)
        self.thetaHome.clicked.connect(self.zeroTheta)
        self.allHome.clicked.connect(self.homeAll)
        self.servoPower.clicked.connect(self.toggleServos)
        self.speedDownManual.clicked.connect(self.manualDecelerate)
        self.speedUpManual.clicked.connect(self.manualAccelerate)
        self.xNeg.clicked.connect(self.jogXNeg)
        self.xPos.clicked.connect(self.jogXPos)
        self.yNeg.clicked.connect(self.jogYNeg)
        self.yPos.clicked.connect(self.jogYPos)
        self.zNeg.clicked.connect(self.jogZNeg)
        self.zPos.clicked.connect(self.jogZPos)
        self.thetaCCW.clicked.connect(self.jogThetaCCW)
        self.thetaCW.clicked.connect(self.jogThetaCW)

        #Link up to loaded files
        self.linkLoaded()        

    def writeMeta(self):
        with open(self.metaFile, 'w') as f:
            f.write(str(self.metaDict))
    
    def readMeta(self):
        with open(self.metaFile, 'r') as f:
            try:
                temp = f.read()
                self.metaDict = eval(temp)
            except: 
                pass

    def jump2Project(self):
        self.TabBar.setCurrentIndex(1)

    def jump2Manual(self):
        self.TabBar.setCurrentIndex(2)

    def linkLoaded(self):
        self.fileList = os.listdir(self.saveDir)
        for elem in self.fileList:
            item = QtWidgets.QListWidgetItem(elem)
            self.FileSelector.addItem(item)
        self.readMeta()

    def loadFile(self):
        file = QtWidgets.QFileDialog.getOpenFileName(parent=self.parent(), caption='Select a Gcode file to upload to the project list.')
        try:
            copy2(file[0], self.saveDir)
            fileName = str.split(file[0], '/')[-1]
            self.fileList.append(fileName)
            item = QtWidgets.QListWidgetItem(self.fileList[-1])
            self.FileSelector.addItem(item)

            #Calculate time of upload
            dateUpload = datetime.datetime.now()
            if dateUpload.hour > 11:
                period = ' PM'
                if dateUpload.hour == 12:
                    hour = '12'
                else:
                    hour = str(dateUpload.hour - 11)
            else:
                hour = str(dateUpload.hour)
                period = ' AM'
            if dateUpload.minute < 10:
                minute = '0' + str(dateUpload.minute)
            else:
                minute = str(dateUpload.minute)
                
            dateUpload = str(dateUpload.month) + '/' + str(dateUpload.day) + '/' + str(
                dateUpload.year) + ' ' + hour + ':' + minute + period

            if fileName not in self.metaDict.keys():
                self.metaDict[fileName] = dateUpload
                self.writeMeta()
        except:
            pass

    def removeFile(self):
        item = self.FileSelector.selectedItems()[0]
        index =  self.FileSelector.currentRow()
        self.FileSelector.takeItem(index)
        if item.text() in self.fileList:
            self.fileList.remove(item.text())
        if item.text() in self.metaDict:
            del self.metaDict[item.text()]
            self.writeMeta()
        os.unlink(self.saveDir + '/' + item.text())
        index = None
        item = None 
        self.FileDescription.setText('')
        
    def dispMeta(self, name):
        path = self.saveDir + '/' + name.text()
        sizeBytes = os.path.getsize(path)
        dateModified = datetime.datetime.fromtimestamp(os.path.getmtime(path))

        if dateModified.hour > 11:
            period = ' PM'
            if (dateModified.hour == 12):
                hour = '12'
            else:
                hour = str(dateModified.hour - 11)
        else:
            hour = str(dateModified.hour)
            period = ' AM'
        if dateModified.minute < 10:
            minute = '0' + str(dateModified.minute)
        else:
            minute = str(dateModified.minute)    

        dateModified = str(dateModified.month) + '/' + str(dateModified.day) + '/' + str(
            dateModified.year) + ' ' + hour + ':' + minute + period

        if sizeBytes > 1000000:
            sizeBytes = str(round(float(sizeBytes) / 1000000, 2)) + ' MB'
        elif (sizeBytes > 1000):
            sizeBytes = str(round(float(sizeBytes) / 1000, 2)) + ' KB'
        else:
            sizeBytes = str(sizeBytes) + ' bytes'

        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Foreground, QtGui.QColor(161,164,163))
        self.FileDescription.setPalette(palette)
        try:
            self.FileDescription.setText('File path: ' + path + '\n\n' +
                                     'File size: ' + sizeBytes + '\n\n' +
                                     'Date last modified: ' + dateModified + '\n\n' +
                                     'Date uploaded: ' + self.metaDict[name.text()])
        except:
           self.FileDescription.setText('File path: ' + path + '\n\n' +
                                     'File size: ' + sizeBytes + '\n\n' +
                                     'Date last modified: ' + dateModified + '\n\n' +
                                     'Date uploaded: N/A')

    def throwError(self, text):
        pallete = QtGui.QPalette()
        pallete.setColor(QtGui.QPalette.Foreground, QtGui.QColor(161, 164, 163))
        self.errorDisp.setPalette(pallete)
        if self.errors == 0:
            self.errorDisp.clear()
        temp = self.errorDisp.text()

        timeOfError = datetime.datetime.now()
        if timeOfError.hour > 11:
            period = ' PM'
            if timeOfError.hour == 12:
                hour = '12'
            else:
                hour = str(timeOfError.hour - 11)
        else:
            hour = str(timeOfError.hour)
            period = ' AM'
        timeOfError = hour + ':' + str(timeOfError.minute) + period + ' - '

        if temp == '':
            self.errorDisp.setText(timeOfError + text)
        else:
            self.errorDisp.setText(temp + '\n' + timeOfError + text)
        self.errors = self.errors + 1

    def waitForComplete(self, cmdType, numBytes, timeOut):
        count = 0
        while(count < timeOut):
            sleep(self.readDelay)
            received = self.spi.readbytes(numBytes)
            print('ins: '+str(received))
            if received[0] == self.heartbeat:
                count = 0
                print("Heartbeat detected")
            elif received[0] == cmdType:
                return received
            count = count + 1
        self.throwError("Heartbeat lost during cmdcode:" + str(cmdType) + " operation.")
        return -1

    def disableAllButtons(self):
        self.xHome.setEnabled(0)
        self.yHome.setEnabled(0)
        self.zHome.setEnabled(0)
        self.thetaHome.setEnabled(0)
        self.allHome.setEnabled(0)

    def homeX(self):
        self.xHome.setEnabled(0)
        res = self.spi.xfer([self.home, 0b10000000])
        print('Received during tranmission: ' + str(res))
        sleep(self.cmdDelay)
        received = self.waitForComplete(self.home, 2,4)
        print(str(received))
        if received == [self.home, 0x00]:
            pass
        elif received == [self.home, 0x01]:
            self.throwError("Received X home error.")
        else:
            self.throwError("Received nonsense response when attempting to home the X axis.")
        self.xHome.setEnabled(1)

    def homeY(self):
        self.spi.xfer([self.home, 0b01000000])
        sleep(self.cmdDelay)
        received = self.waitForComplete(self.home, 2, 4)
        print(str(received))
        if received == [self.home, 0x00]:
            pass
        elif received == [self.home, 0x01]:
            self.throwError("Received Y home error.")
        else:
            self.throwError("Received nonsense response when attempting to home the Y axis.")

    def homeZ(self):
        self.spi.xfer([self.home, 0b00100000])
        sleep(self.cmdDelay)
        received = self.waitForComplete(self.home, 2, 4)
        print(str(received))
        if received == [self.home, 0x00]:
            pass
        elif received == [self.home, 0x01]:
            self.throwError("Received Z home error.")
        else:
            self.throwError("Received nonsense response when attempting to home the Z axis.")

    def zeroTheta(self):
        #yes = 0x00004000
        ##no = 0x00010000
        #zeroMsg = QtWidgets.QMessageBox()
        #zeroMsg.setText("You are about to set the current Theta axis position as the zero position. Before continuing, ensure that the tool is PARALLEL to the side walls of the machine. Do you wish to proceed with zeroing Theta?")
        #zeroMsg.addButton(QtWidgets.QMessageBox.Yes)
        #zeroMsg.addButton(QtWidgets.QMessageBox.No)
        #received = zeroMsg.exec_()

        #if received == yes:
            #self.spi.xfer([self.home, 0b00010000])
        res = self.spi.xfer(self.diagnostic)
        print('Received during transmission: ' + str(res))
        recieved = self.waitForComplete(self.diagnostic[0], 20, 50)
        print(str(recieved))

    def homeAll(self):
        #self.homeX()
        #self.homeY()
        #self.homeZ()
        self.spi.xfer([self.home, 0b11100000])
        sleep(self.cmdDelay)
        received = self.waitForComplete(self.home, 2, 4)
        print(str(received))
        if received == [self.home, 0x00]:
            pass
        elif received == [self.home, 0x01]:
            self.throwError("Received Z home error.")
        else:
            self.throwError("Received nonsense response when attempting to home the Z axis.")

    def toggleServos(self):
        self.spi.xfer(self.diagnostic)
        sleep(self.readDelay)
        received = self.spi.readbytes(20)

        if received[18] > 0b00001111: #if one is on
            received = self.spi.xfer([self.servo, 0x00]) #turn all off
            power = 0
        else:
            received = self.spi.xfer([self.servo, 0b11110000]) #turn all on
            power = 1

        if received == [self.servoPower, 0x00]:
            pass
        elif received == [self.servoPower, 0x01] and power:
            self.throwError("Received error when attempting to turn on all servos.")
        elif received == [self.servoPower, 0x01] and not power:
            self.throwError("Received error when attempting to turn off all servos.")
        elif power:
            self.throwError("Received nonsense response when attempting to turn on all servos.")
        else:
            self.throwError("Received nonsense response when attempting to turn off all servos.")

    def manualAccelerate(self):
        if self.jogIndex < len(self.jogSpeeds) - 1:
            self.jogIndex = self.jogIndex + 1

        pallete = QtGui.QPalette()
        pallete.setColor(QtGui.QPalette.Foreground, QtGui.QColor(161, 164, 163))
        self.speedDispManual.setPalette(pallete)
        self.speedDispManual.setFont(QtGui.QFont('Arial Rounded MT Bold', 14))
        self.speedDispManual.setText(str(self.jogSpeeds[self.jogIndex]) + ' mm')

    def manualDecelerate(self):
        if self.jogIndex > 0:
            self.jogIndex = self.jogIndex - 1

        pallete = QtGui.QPalette()
        pallete.setColor(QtGui.QPalette.Foreground, QtGui.QColor(161, 164, 163))
        self.speedDispManual.setPalette(pallete)
        self.speedDispManual.setFont(QtGui.QFont('Arial Rounded MT Bold', 14))
        self.speedDispManual.setText(str(self.jogSpeeds[self.jogIndex]) + ' mm')

    def jogXNeg(self):
        self.spi.xfer([self.jog, 0b10000000 | self.binRef[self.jogIndex]])
        sleep(self.readDelay)
        received = self.spi.readbytes(2)
        if received == [self.jog, 0x00]:
            pass
        elif received == [self.jog, 0x01]:
            self.throwError("Overtravel in negative X direction due to jog. Halted by limit switch.")
        elif received == [self.jog, 0x03]:
            self.throwError("Invalid jog motor assignment when attempting to jog X axis in negative direction.")
        elif received == [self.jog, 0x04]:
            self.throwError("Error when attempting to jog X axis in negative direction.")
        else:
            self.throwError("Received nonsense response when attempting to jog the X axis in the negative direction.")

    def jogXPos(self):
        self.spi.xfer([self.jog, 0b10001000 | self.binRef[self.jogIndex]])
        sleep(self.readDelay)
        received = self.spi.readbytes(2)
        if received == [self.jog, 0x00]:
            pass
        elif received == [self.jog, 0x02]:
            self.throwError("Overtravel in positive X direction due to jog. Halted by programmatic limit.")
        elif received == [self.jog, 0x03]:
            self.throwError("Invalid jog motor assignment when attempting to jog X axis in positive direction.")
        elif received == [self.jog, 0x04]:
            self.throwError("Error when attempting to jog X axis in positive direction.")
        else:
            self.throwError("Received nonsense response when attempting to jog the X axis in the positive direction.")

    def jogYNeg(self):
        self.spi.xfer([self.jog, 0b01000000 | self.binRef[self.jogIndex]])
        sleep(self.readDelay)
        received = self.spi.readbytes(2)
        if received == [self.jog, 0x00]:
            pass
        elif received == [self.jog, 0x01]:
            self.throwError("Overtravel in negative Y direction due to jog. Halted by limit switch.")
        elif received == [self.jog, 0x03]:
            self.throwError("Invalid jog motor assignment when attempting to jog Y axis in negative direction.")
        elif received == [self.jog, 0x04]:
            self.throwError("Error when attempting to jog Y axis in negative direction.")
        else:
            self.throwError("Received nonsense response when attempting to jog the Y axis in the negative direction.")

    def jogYPos(self):
        self.spi.xfer([self.jog, 0b01001000 | self.binRef[self.jogIndex]])
        sleep(self.readDelay)
        received = self.spi.readbytes(2)
        if received == [self.jog, 0x00]:
            pass
        elif received == [self.jog, 0x02]:
            self.throwError("Overtravel in positive Y direction due to jog. Halted by programmatic limit.")
        elif received == [self.jog, 0x03]:
            self.throwError("Invalid jog motor assignment when attempting to jog Y axis in positive direction.")
        elif received == [self.jog, 0x04]:
            self.throwError("Error when attempting to jog Y axis in positive direction.")
        else:
            self.throwError("Received nonsense response when attempting to jog the Y axis in the positive direction.")

    def jogZNeg(self):
        self.spi.xfer([self.jog, 0b00100000 | self.binRef[self.jogIndex]])
        sleep(self.readDelay)
        received = self.spi.readbytes(2)
        if received == [self.jog, 0x00]:
            pass
        elif received == [self.jog, 0x01]:
            self.throwError("Overtravel in negative Z direction due to jog. Halted by limit switch.")
        elif received == [self.jog, 0x03]:
            self.throwError("Invalid jog motor assignment when attempting to jog Z axis in negative direction.")
        elif received == [self.jog, 0x04]:
            self.throwError("Error when attempting to jog Z axis in negative direction.")
        else:
            self.throwError("Received nonsense response when attempting to jog the Z axis in the negative direction.")

    def jogZPos(self):
        self.spi.xfer([self.jog, 0b00101000 | self.binRef[self.jogIndex]])
        sleep(self.readDelay)
        received = self.spi.readbytes(2)
        if received == [self.jog, 0x00]:
            pass
    
        elif received == [self.jog, 0x02]:
            self.throwError("Overtravel in positive Y direction due to jog. Halted by programmatic limit.")
        elif received == [self.jog, 0x03]:
            self.throwError("Invalid jog motor assignment when attempting to jog Y axis in positive direction.")
        elif received == [self.jog, 0x04]:
            self.throwError("Error when attempting to jog Y axis in positive direction.")
        else:
            self.throwError("Received nonsense response when attempting to jog the Y axis in the positive direction.")

    def jogThetaCCW(self):
        self.spi.xfer([self.jog, 0b00010000 | self.binRef[self.jogIndex]])
        sleep(self.readDelay)
        received = self.spi.readbytes(2)
        if received == [self.jog, 0x00]:
            pass
        elif received == [self.jog, 0x03]:
            self.throwError("Invalid jog motor assignment when attempting to jog the Theta axis in the counter-clockwise direction.")
        elif received == [self.jog, 0x04]:
            self.throwError("Error when attempting to jog the Theta axis in the counter-clockwise direction.")
        else:
            self.throwError("Received nonsense response when attempting to jog the Theta axis in the counter-clockwise direction.")

    def jogThetaCW(self):
        self.spi.xfer([self.jog, 0b00011000 | self.binRef[self.jogIndex]])
        sleep(self.readDelay)
        received = self.spi.readbytes(2)
        if received == [self.jog, 0x00]:
            pass
        elif received == [self.jog, 0x03]:
            self.throwError("Invalid jog motor assignment when attempting to jog the Theta axis in the clockwise direction.")
        elif received == [self.jog, 0x04]:
            self.throwError("Error when attempting to jog the Theta axis in the clockwise direction.")
        else:
            self.throwError("Received nonsense response when attempting to jog the Theta axis in the clockwise direction.")

    def projectAccelerate(self):
        if self.projIndex < len(self.projSpeeds) - 1:
            self.projIndex = self.projIndex + 1

        pallete = QtGui.QPalette()
        pallete.setColor(QtGui.QPalette.Foreground, QtGui.QColor(161, 164, 163))
        self.speedDispProj.setPalette(pallete)
        self.speedDispProj.setFont(QtGui.QFont('Arial Rounded MT Bold', 14))
        self.speedDispProj.setText(str(self.projSpeeds[self.projIndex]) + '%')

    def projectDecelerate(self):
        if self.projIndex > 0:
            self.projIndex = self.projIndex - 1

        pallete = QtGui.QPalette()
        pallete.setColor(QtGui.QPalette.Foreground, QtGui.QColor(161, 164, 163))
        self.speedDispProj.setPalette(pallete)
        self.speedDispProj.setFont(QtGui.QFont('Arial Rounded MT Bold', 14))
        self.speedDispProj.setText(str(self.projSpeeds[self.projIndex]) + '%')

    def projectStart(self):
        self.started = True
        self.paused = False
        self.Pause.setEnabled(True)
        self.Stop.setEnabled(True)
        self.Start.setEnabled(False)
        self.runLoop()
    
    def projectPause(self):
        self.paused = not self.paused

    def projectStop(self):
        self.started = False
        self.Pause.setEnabled(False)
        self.Stop.setEnabled(False)
        self.Start.setEnabled(True)

    def runLoop(self):
        line = 0
        txBuffer = '' 
        item = self.FileSelector.selectedItems()
        
        if len(item) > 0:
            item = item[0]
            self.gCodeList = self.parse.fileParse(self.saveDir + '/' + item.text()) 
            while(self.started):  
                if self.paused:
                    print("PAUSE PRESSED")
                else:
                    print("not paused")
                    #load transmission buffer and increment to new point in file
                   
                    while line < len(self.gCodeList) and len(txBuffer) + len(self.gCodeList[line]) < 256: # max of 255 
                        txBuffer = txBuffer + self.gCodeList[line]
                        line = line + 1

                    #transmit command and size
                    print(str(self.gcode) + ', ' + str(len(txBuffer)) + '\n')
                    #transmit gcode dump
                    print(txBuffer)
                    #clear tx buffer
                    txBuffer = ''
                    if not line < len(self.gCodeList):
                        self.started = 0
                QtGui.QGuiApplication.processEvents()
        else:
            print("length not greater than 0")
            print(item)
        self.Pause.setEnabled(False)
        self.Stop.setEnabled(False)
        self.Start.setEnabled(True)


if __name__ == '__main__': 
    app = QtWidgets.QApplication(sys.argv)
    myWindow = MyWindowClass()
    myWindow.show()
    sys.exit(app.exec_())
