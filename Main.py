import encoder
import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import qApp
import sys
import os
import Ciphers as cph
import about


class MainWin(QtWidgets.QMainWindow, encoder.Ui_MainWindow):
	def __init__(self):
		""" INIT function """
		super().__init__()
		self.setupUi(self)
		self.cipher = None
		self.errorLabel.setStyleSheet("QLabel {color:rgba(255, 30, 100, 255)}")
		self.btnEncode.clicked.connect(self.encode_text)
		self.setCipher.activated[str].connect(self.set_cipher)
		self.actionAbout_program.triggered.connect(self.open_about)
		
	def encode_text(self):
		""" Recive signal to encode a text in TextEdit """
		try:
			text = self.insertText.toPlainText()
			key = self.lineCipher.text()
			if self.cipher == None:
				self.errorLabel.setText("You should set a cipher")
				return
			if self.marker == "Caesar":
				if not key.isdigit():
					self.errorLabel.setText("Your key should be a number\n(1-25)")
					return
			#key = int(key)
				result = self.cipher.encode_txt(text, int(key))
			if self.marker == "Vigenere":
				result = self.cipher.encode_txt(text, str(key))
			self.wordsNum.display(len(text.split()))
			self.readyText.setPlainText(result)
		except Exception as e:
			print("ERRO--->: ", e)
				
	def set_cipher(self, text):
		""" Set cipher fo encode """
		if text == "Select Cipher":
			self.cipher = None
			return
		classes = {
		"Caesar": cph.Caesar, 
		"Vigenere": cph.Vigenere,
		}
		self.marker = text
		self.cipher = classes[text]()
	
	def open_about(self):
		self.win = AboutWindow()
		self.win.show()
		
	
class AboutWindow(QtWidgets.QMainWindow, about.Ui_About):
	def __init__(self):
		""" INIT function """
		super().__init__()
		self.setupUi(self)
		self.okBtn.clicked.connect(self.close_about)
	
	def close_about(self):
		self.close()
		
	
		
def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainWin()  # Создаём объект класса MainWin
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()