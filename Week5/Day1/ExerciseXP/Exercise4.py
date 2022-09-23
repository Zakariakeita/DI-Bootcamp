class Zoo:
	def __init__(self,zoo_name):
		self.animals=[]
		self.name=zoo_name

	
	def add_animal(self,new_animal):
		if new_animal not in self.animals:
			self.animals.append(new_animal)
		else:
			print(f"{new_animal} is already in the list")
			

	def get_animals(self):
		print('The animals of zoo : ')
		for i in self.animals:
			print(i,end=' ')		

	def sell_animal(self,animal_sold):
		if animal_sold in self.animals:
			self.animals.remove(animal_sold)
			print('The animals of zoo : ')
			for i in self.animals:
				print(i,end=' ')
		
	def sort_animals(self):
		sort=sorted(self.animals)
		dic={}
		res=[]
		x=[]
		for i in sort:
			if i[0] not in x:
				x.append(i[0])
		for i in x:
			p=[]
			for j in sort:
				if j[0]==i:
					p.append(j)
			res.append(p)
		for k,v in enumerate(res):
			dic[k]=v
		return dic

	def get_groups(self,dic):
		print(' ')
		print('list of animals by alphabet group  : ')
		print(dic)
			
ramat_gan_safari=Zoo('safari') 
print(f'welcome To Zoo  {ramat_gan_safari.name}')
num=int(input('How nany animal should we add to the zoo : '))
for i in range(num):
	add=input('Which animal should we add to the zoo : ')
	ramat_gan_safari.add_animal(add)
ramat_gan_safari.get_animals()
dic=ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups(dic)









