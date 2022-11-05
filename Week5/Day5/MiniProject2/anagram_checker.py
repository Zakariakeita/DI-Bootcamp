class AnagramChecker:
    
    def __init__(self):
        file = "/Users/macbookpro/Desktop/DI-Bootcamp/Week5/Day5/MiniProject2/sowpods.txt"
        liste = []
        with open(file) as f:
            for line in f :
                liste.append(line[:-1])
        self.data=liste

    def is_valid_word(self,word):
        if(word in self.data):
            return True
        else:
            return False

    def get_anagrams(self,word):
        if(AnagramChecker.is_valid_word(self,word)==True):
            anagrams = []  
            for w in self.data:  
                if(sorted(word)== sorted(w)):
                    anagrams.append(w)
            return anagrams
        else:
            return False



