class Dog:
	def __init__(self,name,height):
		self.name=name
		self.height=height
	def bark(self) :
		print(f"{self.name} goes woof!")
	def jump(self) :
		print(f"{self.name} jumps {self.height*2} cm high!")

davids_dog=Dog('Rex',50)
print(f'David dog name is {davids_dog.dog_name} and height is {davids_dog.dog_height}')
davids_dog.bark()
davids_dog.jump()
sarahs_dog=Dog('Teacup',20)
print(f'Sarahs dog name is {sarahs_dog.dog_name} and height is {sarahs_dog.dog_height}')
sarahs_dog.bark()
sarahs_dog.jump()

if sarahs_dog.height > davids_dog.height:
	print(f"{sarahs_dog.name} is bigger")
else:
	print(f"{davids_dog.name} is bigger")




