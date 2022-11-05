


# Hint: the Character class should be in charge of creating characters, the Game class should be in charge of how many times the Character gets instantiated and of exporting the data in json or txt
import random
import json

class Character():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.strength = self.rand_points()
        self.dexterity = self.rand_points()
        self.constitution = self.rand_points()
        self.intelligence = self.rand_points()
        self.wisdom =self.rand_points()
        self.charisma = self.rand_points()

    def rand_points(self):
        liste = [random.randint(1,6) for i in range(4)]
        return sum(liste) - min(liste)

    # def ability(self):
    #     self.strength = self.rand_points()
    #     self.dexterity = self.rand_points()
    #     self.constitution = self.rand_points()
    #     self.intelligence = self.rand_points()
    #     self.wisdom =self.rand_points()
    #     self.charisma = self.rand_points()

    

class Game():
    def start(self):
        all_players = {} # for json file
        all_players["players"] = []
        players = input("How many players are playing:\t_ ")
        try:
            num = int(players)
        except:
            print("Your entry not correct")
        for i in range(num):
            name = input(f"Chararcter number {i} name:\t_ ")
            age = input(f"Chararcter number {i} age:\t_ ")
            character = Character(name,age)
            file = f"/Users/macbookpro/Desktop/DI-Bootcamp/Week5/Day4/ExercisesXpNinja/{character.name}.txt"   
            with open(file,"w") as f:
                f.write(f"Name : {character.name}\n")
                f.write(f"Age : {character.age}\n")
                f.write(f"----\tStats  ----\n")
                f.write(f"Strength : {character.strength}\n")
                f.write(f"Dexterity : {character.dexterity}\n")
                f.write(f"Constitution : {character.constitution}\n")
                f.write(f"Intelligence : {character.intelligence}\n")
                f.write(f"Wisdom : {character.wisdom}\n")
                f.write(f"Charisma : {character.charisma}\n")
            dict = {
                "Name" : character.name,
                "Age" :character.age,
                "Strength" : character.strength,
                "Dexterity" : character.dexterity,
                "Constitution": character.constitution,
                "Intelligence" : character.intelligence,
                "Wisdom" : character.wisdom,
                "Charisma" : character.charisma
            }
            all_players["players"].append(dict)
        json_file = "/Users/macbookpro/Desktop/DI-Bootcamp/Week5/Day4/ExercisesXpNinja/players.json"
        with open(json_file,"w") as f:
            json.dump(all_players,f,indent = 3)
        print("Game initiated with success")

game = Game()
game.start()

            
