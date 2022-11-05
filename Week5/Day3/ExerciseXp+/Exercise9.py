# Exercise 9 : Faker Module
'''Instructions
Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
Create an empty list called users. Tip: It should be a list of dictionaries.
Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress, langage_code. Use faker to populate them with fake data.'''
from faker import Faker
faker = Faker('fr_FR.')
users = []

def add_users(list):
    dict = {
        'name':faker.name(),
        'adress':faker.address(),
        'langage_code':faker.language_code()
    }
    list.append(dict)
    return list

for i in range(10):
    add_users(users)
print(users)