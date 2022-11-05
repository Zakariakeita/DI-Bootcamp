# 🌟 Exercise 2: Random Module
# Instructions
# Create a function that accepts a number between 1 and 100, then rolls a random number between 1 and 100,
# if it’s the same number, display a success message to the user, else don’t.
from random import randint
def user_number():
    num=0
    while(num>100 or num < 1):
        num  = input("Enter a number between 1 and 100: ")
        try:
            num = int(num)
        except:
            num = 0
    return num

randi = randint(1,100)
print(randi)
if(user_number() == randi):
    print("Success")
else:
    print("Your input does not match ! ")

