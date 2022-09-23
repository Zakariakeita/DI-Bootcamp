class Farm():
	def __init__(self,farm):	
		self.name=farm
		self.animals_list=[]
		self.num=[]
		print(self.name +"'s farm")
	def add_animal(self,name,nb=1):
		if name in self.animals_list:
			self.num[self.animals_list.index(name)]=self.num[self.animals_list.index(name)]+nb
		else:
			self.animals_list.append(name)
			self.num.append(nb)

	def get_info(self):
		for i in self.animals_list:
			print(i,' : ',self.num[self.animals_list.index(i)])
		print("\n \tE-I-E-I-0!")
		
		
		

macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.get_info()
