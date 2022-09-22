#Exercise 1 :
print("Hello word\n"*4)

#Exercise 2 :
result = (99^3) * 8
print(result)

#Exercise 3 :
#5 < 3   ---> False
#3 == 3  ---> True
#3 == "3" ---> Error
#"3" > 3  ---> Error
#"Hello" == "hello" ---> False

#Exercise 4 :

computer_brand = "Macbook"
print(f"I have a {computer_brand} computer")

# Exercise 5 : 

name = "KEITA Zakaria"
age = 24
shoe_size = 45
info = "I am {} and have {} years old. I like programation. Every time I start one of those activity i done at least my shoe size minute one it, I mean {} ".format(name,age,shoe_size)
print(info)

# Exercise 6 : 

a =15
b=8
if a > b :
    print("Hello world")

#Exercise 7 :

value = int(input("Enter your number"))
if value%2 == 0 :
    print("{} is odd".format(value))
else:
    print("{} is even".format(value))

#Exercise 8 : 

myname="Zakaria"
yourname=input('enter your name')
if yourname==myname:
	print('I come from futur to say you that....I am your father;see We have the same name')
else:
	print('don\'t care about me . I don\'t know who you are  ')

#  Exercise 9 : 
inches =float(input("Your height in inches:\t"))
cm = inches * 2.45
if (cm > 145):
    print("You are tall enough to ride")
else:
    print("You need to grow some more to ride")
