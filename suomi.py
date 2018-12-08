class Translate:
	def __init__(self, number):
		Translate.convert(self)
		self.string = str(number)
		self.decimals = False
		if "." in self.string or "," in self.string:
			self.decimals = True
			if "." in self.string:
				self.whole_int, self.dec_int = int(self.string.split("."))
			elif "," in self.string:
				self.whole_int, self.dec_int = int(self.string.split(","))
		else:
			self.whole_int = int(number)
		if len(str(self.whole_int)) > 15:
			print("number too big")
			return
		print(Translate.iteriter(self))

	def iteriter(self):
		self.text = ""
		while self.whole_int != 0:
			bigger = False
			correct_index = None
			previous_index = None
			for key, value in self.partitive.items():
				if len(str(self.whole_int)) >= key:
					correct_index = key
					break
				elif previous_index == None:
					previous_index = True
				elif previous_index != None:
					previous_index = correct_index
				correct_index = key
				if len(str(self.whole_int)) >= correct_index and len(str(self.whole_int)) < previous_index: 
					break
			if len(str(self.whole_int)) > 2:
				etu = str(self.whole_int)[:-correct_index+1]
			else:
				etu = str(self.whole_int)
				self.text += Translate.threedigit(self,etu,correct_index, under_three_digit=False)
				break
			self.text += Translate.threedigit(self,etu, correct_index)
			self.whole_int = int(str(self.whole_int)[len(etu):])

		return self.text


	def threedigit(self, etu, correct_index, under_three_digit=True):
		etu_str = ""
		if under_three_digit != False:
			ending = self.partitive[correct_index]
		else:
			ending = ""
		if len(etu) == 3:
			etu_str += Translate.hundred(self, etu, etu_str)
		if len(etu) == 2:
			etu_str += Translate.ten(self, etu, etu_str)		
		if len(etu) == 1:
			if str(etu) == "1":
				if under_three_digit == True:
					ending = self.nominative[correct_index]
					return ending
			etu_str += Translate.one(self, etu, etu_str)
			
		return etu_str + ending


	def hundred(self, etu, etu_str):
		if etu[0] == "1":
			etu_str += "sata"
		else:
			etu_str += self.oneto19[int(etu[0])] + "sataa"
		if etu[1] == "0" and etu[2] == "0":
			return etu_str
		if etu[1] != "0":
			etu_str = Translate.ten(self, etu[1:], etu_str)
		else:
			etu_str = Translate.one(self, etu[-1], etu_str)
		return etu_str


	def ten(self, etu, etu_str):
		try:
			etu_str += self.oneto19[int(etu)]
		except:
			if etu[1] == "0":
				etu_str += self.oneto19[int(etu[0])] + "kymmentä"
			else:
				etu_str += self.oneto19[int(etu[0])] + "kymmentä" + Translate.one(self, etu[1], etu_str)
		return etu_str

	def one(self, etu, etu_str):
		etu_str = self.oneto19[int(etu)]
		return etu_str




	def convert(self):
		self.partitive = {
		13: "biljoonaa",
		10: "miljardia",
		7: "miljoonaa",
		4: "tuhatta",
		3: "sataa",	
		}

		self.nominative = {
		13: "biljoona",
		10: "miljardi",
		7: "miljoona",
		4: "tuhat",
		3: "sata",	
		}

		self.oneto19 = {
		1: "yksi",
		2: "kaksi",
		3: "kolme",
		4: "neljä",
		5: "viisi",
		6: "kuusi",
		7: "seitsemän",
		8: "kahdeksan",
		9: "yhdeksän",
		10: "kymmenen",
		11: "yksitoista",
		12: "kaksitoista",
		13: "kolmetoista",
		14: "neljätoista",
		15: "viisitoista",
		16: "kuusitoista",
		17: "seitsemäntoista",
		18: "kahdeksantoista",
		19: "yhdeksäntoista"}

				

luku = 35036

Translate(luku)


