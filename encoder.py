# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'encoder.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(609, 536)
        MainWindow.setMinimumSize(QtCore.QSize(609, 536))
        MainWindow.setMaximumSize(QtCore.QSize(623, 557))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.insertText = QtWidgets.QTextEdit(self.centralwidget)
        self.insertText.setGeometry(QtCore.QRect(10, 90, 281, 341))
        self.insertText.setObjectName("insertText")
        self.setCipher = QtWidgets.QComboBox(self.centralwidget)
        self.setCipher.setGeometry(QtCore.QRect(10, 30, 131, 21))
        self.setCipher.setObjectName("setCipher")
        self.setCipher.addItem("")
        self.setCipher.addItem("")
        self.setCipher.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 131, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 171, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 450, 201, 16))
        self.label_3.setObjectName("label_3")
        self.lineCipher = QtWidgets.QLineEdit(self.centralwidget)
        self.lineCipher.setGeometry(QtCore.QRect(10, 470, 281, 20))
        self.lineCipher.setObjectName("lineCipher")
        self.readyText = QtWidgets.QTextEdit(self.centralwidget)
        self.readyText.setGeometry(QtCore.QRect(320, 90, 281, 341))
        self.readyText.setObjectName("readyText")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(320, 70, 61, 16))
        self.label_4.setObjectName("label_4")
        self.wordsNum = QtWidgets.QLCDNumber(self.centralwidget)
        self.wordsNum.setGeometry(QtCore.QRect(510, 20, 81, 31))
        self.wordsNum.setObjectName("wordsNum")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(440, 20, 71, 31))
        self.label_5.setObjectName("label_5")
        self.btnEncode = QtWidgets.QPushButton(self.centralwidget)
        self.btnEncode.setGeometry(QtCore.QRect(430, 460, 81, 31))
        self.btnEncode.setObjectName("btnEncode")
        self.errorLabel = QtWidgets.QLabel(self.centralwidget)
        self.errorLabel.setGeometry(QtCore.QRect(200, 10, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.errorLabel.setFont(font)
        self.errorLabel.setLineWidth(1)
        self.errorLabel.setText("")
        self.errorLabel.setObjectName("errorLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 609, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionOpen_file = QtWidgets.QAction(MainWindow)
        self.actionOpen_file.setObjectName("actionOpen_file")
        self.actionReset = QtWidgets.QAction(MainWindow)
        self.actionReset.setObjectName("actionReset")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout_program = QtWidgets.QAction(MainWindow)
        self.actionAbout_program.setObjectName("actionAbout_program")
        self.actionDecode_File = QtWidgets.QAction(MainWindow)
        self.actionDecode_File.setObjectName("actionDecode_File")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionDecode_File)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionOpen_file)
        self.menuFile.addAction(self.actionReset)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout_program)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple Encoder"))
        self.setCipher.setItemText(0, _translate("MainWindow", "Select Cipher"))
        self.setCipher.setItemText(1, _translate("MainWindow", "Caesar"))
        self.setCipher.setItemText(2, _translate("MainWindow", "Vigenere"))
        self.label.setText(_translate("MainWindow", "Select Cipher"))
        self.label_2.setText(_translate("MainWindow", "Enter text for encrypt"))
        self.label_3.setText(_translate("MainWindow", "Enter smth to encrypt"))
        self.label_4.setText(_translate("MainWindow", "Result"))
        self.label_5.setText(_translate("MainWindow", "Total words \n"
" encrypted"))
        self.btnEncode.setText(_translate("MainWindow", "ENCODE"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionSave_as.setText(_translate("MainWindow", "Save file as"))
        self.actionOpen_file.setText(_translate("MainWindow", "Open file"))
        self.actionReset.setText(_translate("MainWindow", "Reset"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAbout_program.setText(_translate("MainWindow", "About program"))
        self.actionDecode_File.setText(_translate("MainWindow", "Decode Text"))
