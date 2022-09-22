import random
# Exercise 1: 
print('Exercise 1: ')
res=[]
l1=['i','you','he','her','it','we','they']
l2=[1,2,3,4,5,6,7,8]
print('In l1 there are : ',end='')
for i in l1:
	print(i," ",end='')	
	res.append(i)
print('')
print('In l2 there are : ',end='')
for i in l2:
	print(i," ",end='')	
	res.append(i)
print('')
print('The contenation of l1 and l2 given :',end='')
for i in res:
	print(i," ",end='')	

# Exercise 2: 
print('Exercise 2: ')
for i in range(1500,2501):
	if((i%5)==0 or (i%7)==0):
		print(f'{i} is a multiples of 5 or 7')


# Exercise 3: 
print('Exercise 3: ')
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
name=input('enter your name : ')
if name in names:
	print(f"{name} is in the tab at index {names.index(name)} ")

# Exercise 4: 
print('Exercise 4: ')
li2=[]
for i in range(3):
	num=int(input(f'Enter the number {i+1} : '))
	li2.append(num)
print('the greatest Number input is :', max(li2))

# Exercise 5: 
print('Exercise 5: ')
s='abcdefghijklmnopqrstuvwxyz'
for i in s:
	if i=='a' or i=='e' or i=='i' or i=='o'  or i=='u' or i=='y':
		print(f'{i} is a vowel.')
	else:
		print(f'{i} is a consonant.')



# Exercise 6: 
print('Exercise 6: ')
words=[]
for i in range(7):
	num=input(f'Enter the word {i+1} : ')
	words.append(num)
letter=input(f'Enter a letter : ')
for i in words:
	print(i)
	if letter in i:
		print(f'{letter} appear in {words.index(i)} the words is {i} at index {i.index(letter)}')
	else:
		print('with the word and the letter')



# Exercise 7:
print('Exercise 7:')
var=[]
for i in range(1,1000001):
	var.append(i)

print(f'the min is {min(var)} and the max is {max(var)}')


#Exercise 8 :
print('Exercise 8 :')
numbers=input('enter a sequence of comma-separated numbers : ')
list1=numbers.split(",")
tuples=tuple(list1)
print(list1)
print(tuples)

# Exercise 9 : 
i=0;
lose=0
win=0
while (i==0):
	print('Exercise 9 : ')
	num=int(input('input a number from 1 to 9 (including) :'))
	num1=random.randint(1,9)
	if (num1==num):
		print('winner')
		win=win+1
	else :
		lose=lose+1
		print('better luck next time.')
	v=int(input('try again ?\t 1- yess 2--noo'))
	if(v==2):
		break
	else:
		print('continues')

print(f'you lose {lose} times and have win {win} times')










