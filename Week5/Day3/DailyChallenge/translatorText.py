from translate import Translator
translator=Translator(to_lang="English",from_lang="French")

myDict={"Bonjour":translator.translate("Bonjour"), "Au revoir":translator.translate("Au revoir"), 
"Bienvenue":translator.translate("Bienvenue"), "A bientôt":translator.translate("A bientôt")}


print(myDict)

