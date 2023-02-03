Ce Que Vous Allez Créer
Projet : IMDI
IMDB For Developers Institute


Des Instructions
PARTIE I
Créez un nouveau projet Django appelé FilmProject .

Créez deux applications :
films
comptes
Aujourd'hui, nous allons travailler sur l' application des films .


PARTIE IA : Films
Créez une URL avec la route suivante : /homepage, qui affiche un modèle appelé homepage.html .

Dans le templatesdossier, ajoutez un nouveau dossier appelé partials , et à l'intérieur ajoutez les deux fichiers HTML suivants :
base.html : qui contient le lien Bootstrap et le titre, et affiche un pied de page Bootstrap.
navbar.html : qui contient une barre de navigation Boostrap

Le fichier homepage.html doit être créé dans le templatesdossier. Ce fichier étend le modèle base.html et inclut le fichier navbar.html .
Astuce : consultez la documentation pour comprendre comment inclure des modèles


PARTIE IB : Films : Ajouter Un Film Et Un Réalisateur
Créez 4 nouveaux modèles :
Pays :
Nom

Catégorie :
Nom

Film:
Titre
release_date (par défaut la date d'aujourd'hui)
created_in_country : relation One to Many avec Country(la "nationalité du film")
available_in_countries : relation plusieurs à plusieurs avecCountry
catégorie : relation plusieurs à plusieurs avecCategory
réalisateur : Many to Many relation avecDirector

Directeur:
prénom
nom de famille

Créer les formulaires : AddFilmForm et AddDirectorForm

Créer les routes : addFilm et addDirector

Créer les vues : addFilm et addDirector

Dans le templatesdossier, créez un dossier appelé directeur et créez le fichier addDirector.html .

Dans le templatesdossier, créez un dossier appelé film et créez le fichier addFilm.html .

Les nouveaux films avec leur(s) réalisateur(s) doivent être rendus sur le template homepage.html . Vous pouvez utiliser la carte de composants de Bootstrap pour styliser la page.

Attention, la date de sortie doit être affichée dans un format « human friendly ».

Dans la barre de navigation, vous devez ajouter deux nouveaux liens vers les routes addFilm et addDirector .



