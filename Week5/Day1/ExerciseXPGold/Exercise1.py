class Circle:
	def __init__(self):
		self.radius=1.0
		
	
	def perimeter(self):
		Perimeter=2*3.14*self.radius
		print(f'perimeter={Perimeter}')

	def area(self):
		Area=3.14*self.radius*self.radius
		print(f'Area={Area}')

	def geometric(self):
		print(f'radius={self.radius}')
		
geo=Circle()
geo.perimeter()
geo.area()
geo.geometric()