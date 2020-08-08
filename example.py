# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit
import random
from datetime import datetime
import pyttsx3
#import jack
engine = pyttsx3.init()

now = datetime.now()
useMic = False
useSpeakers = False
engine.setProperty('rate', 150)
"""
client = jack.Client('MyGreatClient')
in1 = client.inports.register('input_1')
out1 = client.outports.register('output_1')
"""

file = open('insultee.txt', 'r')
myList = list(file)
for i in range(len(myList)):
    myList[i] = myList[i].rstrip('\n')
    myList[i] = myList[i].split(sep = ', ')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(273, 366)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.checkBox.setObjectName("checkBox")
        self.checkBox.stateChanged.connect(self.clickBoxMic)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 50, 251, 81))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.insult)

        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 30, 101, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.stateChanged.connect(self.clickBoxSpeakers)

        self.textbox = QLineEdit(self.centralwidget)
        self.textbox.setGeometry(QtCore.QRect(10, 140, 251, 91))
        self.textbox.setObjectName("textBox")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 240, 251, 81))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.custom)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 273, 21))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox.setText(_translate("MainWindow", "Use Mic"))
        self.pushButton.setText(_translate("MainWindow", "Generate Insult"))
        self.checkBox_2.setText(_translate("MainWindow", "Use Speakers"))
        self.pushButton_2.setText(_translate("MainWindow", "Custom Message"))
    def clickBoxMic(self, state):
        global useMic
        if state == QtCore.Qt.Checked:
            
            useMic = True
        else:
            useMic = False

    def clickBoxSpeakers(self, state):
        global useSpeakers
        if state == QtCore.Qt.Checked:
            useSpeakers = True
        else:
            useSpeakers = False

    def insult(self):
        print("clicked", useMic, useSpeakers)
        text = ""
        temp = myList[random.randint(0,(len(myList)-1))]
        text = temp[0] + " " + temp[random.randint(1,len(temp)-1)]
        
        print(text)
        if useSpeakers == True:
            self.pushButton.setEnabled(False)
            self.pushButton_2.setEnabled(False)

            engine.say(text)
            engine.runAndWait()

            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(True)

    def custom(self):
        textValue = self.textbox.text()
        print(textValue)
        self.pushButton.setEnabled(False)
        self.pushButton.setEnabled(False)

        engine.say(textValue)
        engine.runAndWait()

        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

