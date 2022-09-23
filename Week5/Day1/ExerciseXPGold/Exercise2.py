
class MyList:
	def __init__(self,letter):
		self.letter=letter
	def reverseList(self):
		print(f'the reversed list= {reversed(self.letter)}')
		
	def sortList(self):
		print(f'the sorted list= {sorted(self.letter)}')
		
	
list=MyList(['banana','orange','mangoes','tomatoes','potatoes','name','cool','yeh'])
print(f'the reversed list ={list.reverseList()}')
print(f'the sorted list ={list.sortList()}')

