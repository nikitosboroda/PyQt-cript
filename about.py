# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(291, 373)
        About.setMinimumSize(QtCore.QSize(291, 373))
        About.setMaximumSize(QtCore.QSize(291, 373))
        self.centralwidget = QtWidgets.QWidget(About)
        self.centralwidget.setObjectName("centralwidget")
        self.okBtn = QtWidgets.QPushButton(self.centralwidget)
        self.okBtn.setGeometry(QtCore.QRect(110, 290, 81, 41))
        self.okBtn.setObjectName("okBtn")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 10, 256, 271))
        self.textBrowser.setObjectName("textBrowser")
        About.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(About)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 291, 21))
        self.menubar.setObjectName("menubar")
        About.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(About)
        self.statusbar.setObjectName("statusbar")
        About.setStatusBar(self.statusbar)

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "About"))
        self.okBtn.setText(_translate("About", "OK"))
        self.textBrowser.setHtml(_translate("About", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#1c30de;\">Эта программа создана для </span><span style=\" font-size:8pt; font-style:italic; color:#1c30de;\">шифрования </span><span style=\" font-size:8pt; color:#1c30de;\">и </span><span style=\" font-size:8pt; font-style:italic; color:#1c30de;\">расшифровывания</span><span style=\" font-size:8pt; color:#1c30de;\"> текста, сообщений и др.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic; text-decoration: underline; color:#1c30de;\">Правила работы:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#1c30de;\">1) Выбрать тип шифрования</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#1c30de;\">2) Вставить текст с которым необходимо провести преобразования</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#1c30de;\">3) Вставить необходимый ключ</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#1c30de;\">4) Нажать кнопку запуска</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#1c30de;\">При возникновении ошибки, высвечивается текст с надписью ошибки</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#1c30de;\">При необходимости зашифрованный текст можно сохранить в файл с расширением .TXT</span></p></body></html>"))

