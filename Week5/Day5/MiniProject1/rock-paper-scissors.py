
from game import Game

def get_user_menu_choice():
    while True:
        print("\n\t:::Menu:::")
        print("\t(g) play a new game")
        print("\t(x) show score and quit")
        choice = input("_\t").lower()
        if choice == 'g' or choice == 'x':
            break
    return choice

def print_results(results):
    print("\t",results)

def main():
    results = {"draw":0,"loss":0,"win":0}
    while True:
        choice = get_user_menu_choice()
        if choice == 'g':
            result = Game.play()
            results[result] +=1
        if choice == 'x':
            print_results(results)
            break


main()
    