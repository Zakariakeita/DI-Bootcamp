import re
import anagram_checker
val=True
while val:
    print("\t MENU ")
    print("a: to write a word")
    print("b: to quit")
   
    choice = input("Enter a number")

    if choice == "a":
        word=input("Enter a word")
        if len(word.strip().split())==1:
            if(bool(re.match('^[a-zA-Z]+$', word))==True):
                print("Your word: {}".format(word))
                a=anagram_checker.AnagramChecker()
                if(a.is_valid_word(word)==True):
                    print("This is a valid english word")
                    print(" Anagram for your word is :{} ".format(a.get_anagrams(word)))
                else:
                    print(" this is not a valid english  word")
            else:
                print("Only alphabetic characters are allowed")
        else:
            print("Only a single word is allowed")
            
    elif choice == "b":
        print("good bye")
        val=False
        break
    else:
        print("Your choice is not correct")
        val=False
        break
