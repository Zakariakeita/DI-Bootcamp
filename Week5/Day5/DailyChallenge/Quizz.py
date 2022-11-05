#Part 1

""" What is a class?   A class is a code template for creating objects. Objects have member variables 
                       and have behaviour associated with them
"""

""" What is an instance? An Instance is an object who is created using the constructor of the class """

""" What is encapsulation? The encapsulation hides the implementation details of a class from other objects """

""" What is abstraction? The abstraction is simplifying complex reality by modeling classes appropriate to the problem """

""" What is inheritance?   Inheritance allows us to define a class that inherits all the methods and properties from another class """

""" What is multiple inheritance? Multiple inheritance is a feature of some object-oriented computer programming languages in which an object 
                                  or class can inherit features from more than one parent object or parent class.
"""

""" What is polymorphism? The polymorphism is the process of using an operator or function in different ways for different data input """

""" What is method resolution order or MRO? The Method Resolution Order (MRO) is the set of rules that construct the linearization.
                                            It denotes the way a programming language resolves a method or attribute
                                            In python, method resolution order defines the order in which the base classes are searched when executing a method
"""



#part2
import random
from unicodedata import name
class Card :

   def __init__(self, suit, val):
        self.suit = suit
        self.val = val

   def show(self) :
        print ("{} of {}".format(self.val , self.suit))

class Deck :

    def __init__(self):

        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"] :
            for v in range (1 , 14) :
                self.cards.append(Card(s , v))
    
    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self) :
        for i in range (len(self.cards)-1,0,-1):
            r = random.randint(0 , i)
            self.cards[i]  , self.cards[r] = self.cards[r] , self.cards[i]

    def drawCard(self):
        return self.cards.pop()

class Player :

    def __init__(self,name):
        self.name=name
        self.hand=[]

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()
        

deck=Deck()
deck.shuffle()

bob=Player("Bob")
bob.draw(deck)
bob.showHand()