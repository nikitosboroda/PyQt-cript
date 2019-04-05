""" Файл с различными типами шифрования """
from itertools import cycle
class Caesar:
	def __init__(self):
		self.dicL = {chr(x): x-97 for x in range(97, 123)} #little letter
		self.dicB = {chr(x): x-65 for x in range(65, 90)} #big letter

	def decode_txt(self, string, key):
		new_string = ''
		for i in string:
			if i not in self.dicL:
				if i not in self.dicB:
					new_string += i
					continue
				else:
					ch = self.dicB[i] - key
					if ch < 0:
						ch = 26 + ch
					new_string += self.get_key(self.dicB, ch)
			else:
				ch = self.dicL[i] - key
				if ch < 0:
					ch = 26 + ch
				new_string += self.get_key(self.dicL, ch)

		return new_string
		
	def encode_txt(self, string, key):
		new_str = ''
		for i in string:
			if i not in self.dicL:
				if i not in self.dicB:
					new_str += i
					continue
				else:
					ch = self.dicB[i] + key
					if ch > 25:
						ch = ch - 26
					new_str += self.get_key(self.dicB, ch)
			else:
				ch = self.dicL[i] + key
				if ch > 25:
					ch = ch - 26
				new_str += self.get_key(self.dicL, ch)

		return new_str

	def get_key(self, dic, val):
		for i in dic.items():
			if val in i:
				return i[0]
class Vigenere:
	def __init__(self):
		self.LEN = 127

	def encode_txt(self, value, key):
		return ''.join(map(lambda x: chr((ord(x[0]) + ord(x[1])) % self.LEN), zip(value, cycle(key))))

	def decode_txt(self, value, key):
		return ''.join(map(lambda x: chr((ord(x[0]) - ord(x[1]) + self.LEN) % self.LEN), zip(value, cycle(key))))