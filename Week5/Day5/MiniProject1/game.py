
import random

class Game():
    def get_user_item(self):
        selection = True
        while selection :
            user = input("Select (R)ock (P)aper or (C)isor:  ").lower()
            if  user == "r" or user == "c" or user == "p":
                selection = False
        return user

    def get_computer_item(self):
        return random.choice(['r','p','c'])

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return 'draw'
        elif user_item == 'r' and computer_item == 'p':
            return 'loss'
        elif user_item == 'p' and computer_item == 'c':
            return 'loss'
        return 'win'
    @staticmethod
    def play():
        user = Game().get_user_item()
        computer = Game().get_computer_item()
        result = Game().get_game_result(user,computer)
        if result == 'draw':
            decision = 'You drew'
        elif result == 'loss':
            decision = 'You lose'
        else:
            decision = 'You won'
        print(f"You selected {user}. The computer selected {computer}. "+decision)
        return result

