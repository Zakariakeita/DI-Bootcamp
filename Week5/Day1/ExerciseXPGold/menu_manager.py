class MenuManager():
	def __init__(self):
		self.dishes1=['Soup',10,'B',False]
		self.dishes2=['Hamburger',15,'A',True]
		self.dishes3=['Salad',18,'A',False]
		self.dishes4=['French Fries',5,'C',False]
		self.dishes5=['Beef bourguignon',25,'B',True]
		self.dishes=[self.dishes1,self.dishes2,self.dishes3,self.dishes4,self.dishes5]
		self.menu={}
		for i in range(5):
			self.menu[len(self.menu)]=self.dishes[len(self.menu)]
		print('actualy in menu : ')
		for i in self.menu:
			men=self.menu[i]
			print(men)
	
	def add_item(self,name, price, spice, gluten):
		ad=[name,price,spice,gluten]
		self.menu[len(self.menu)]=ad
		print('\n')
		print(f'The list after add of {name} = ')
		for i in self.menu:
			men=self.menu[i]
			print(men)

	def update_item(self,name, price, spice, gluten):
		e=0
		for i in self.menu:
			v=self.menu[i]
			if v[0]==name:
				v[1]=price
				v[2]=spice
				v[3]=gluten
				e=1
		if e==0:
			print('\n')
			print(' the dish is not in the menu')
		else:
			print('\n')
			print(f'The updated list (update of {name} price ={price} now) =')
			for i in self.menu:
				v=self.menu[i]
				print(v)
		
	def remove_item(self,name):
		e=0
		for i in self.menu:
			v=self.menu[i]
			if v[0]==name:
				self.menu[i]=''
				e=1
				break
		if e==0:
			print('\n')
			print(' the dish is not in the menu')
		else:
			print('\n')
			print(f'The apudated list after delete of {name} =')
			for i in self.menu:
				v=self.menu[i]
				print(v)

restaurant=MenuManager()
restaurant.add_item('Rice', 17,'A', True)
restaurant.update_item('Fishes', 18, 'B', False)
restaurant.remove_item('Salad')
