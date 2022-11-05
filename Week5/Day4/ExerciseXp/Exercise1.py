
import random 

file_name = "/Users/macbookpro/Desktop/DI-Bootcamp/Week5/Day4/ExerciseXp/word_list.txt"

def get_words_from_file(file):
    liste = []
    with open(file) as f:
        for line in f :
            liste.append(line[:-1])
    return liste

def get_random_sentence(length):
    liste = get_words_from_file(file_name)
    sentence = ' '.join(random.choice(liste).lower() for i in range(length))
    return sentence

# print(get_random_sentence(5))

def main():
    print('Le programme affiche une phrase de facon aléatoire.\nPour se faire vous devez indiquer le nombre de mots que doit contenir la phrase')
    user = input("\n:::::\tEntrer le nombre de mots (entre 2 et 20)\t:::::: ")
    try:
        n = int(user)
    except:
        print("Votre saisie est incorrect")
    if (n<20 and n>2):
        print(get_random_sentence(n))


main()