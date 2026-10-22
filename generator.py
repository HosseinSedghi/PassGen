from random import choice
# pip install clipboard
# from clipboard copy

CARACHTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
LENGHT = 30

class Generator:
	def __init__(self, characters=CARACHTERS, lenght=LENGHT):
		self.characters = characters
		self.lenght = lenght
		self.password = ''

	def generate(self):
		password =  ''.join(choice(self.characters) for i in range(self.lenght))
		self.password = password
		return password

	def copy_password(self):
		# return 200 = copied seccussful
		# return 501 = password not exist
		if self.password:
			# copy(self.password)
			return "200"
		else:
			return "501"

	def __str__(self):
		return f"lenght: {self.lenght}\ncharacters: {self.characters}"

if __name__ == "__main__":
	p = Generator()
	print(p.copy_password())
	print(p)
	print(p.generate())
	print(p.copy_password())