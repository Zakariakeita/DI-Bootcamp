import math  
class Circle:
    def __init__(self,rayon):
        self.rayon=rayon
    

    def __aire__(self):
        return math.pow(self.rayon,2)* math.pi

    def __rayon__(self):
        return self.rayon


c1=Circle(10)
c2=Circle(4)

print("Aire c1")
print(c1.__aire__())

print("Aire c2")
print(c2.__aire__())
print("*****")

print("Somme")
print(c1.__rayon__()+ c2.__rayon__())
print("*****")
if(c1.__rayon__() > c2.__rayon__()):
    print( "c1 is bigger")
elif(c1.__rayon__() < c2.__rayon__()):
    print( "c2 is bigger")

print("*****")

if(c1.__rayon__() == c2.__rayon__()):
    print( "c1 eq c2")
else:
    print( "c1 not eq c2")

l=[c1.__rayon__(),c2.__rayon__()]
print(sorted(l))