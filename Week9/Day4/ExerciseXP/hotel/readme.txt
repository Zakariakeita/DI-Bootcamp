Ce Projet Peut Se Faire Seul Ou En Groupe (Maximum 2 Personnes) !! Trouvez Un Partenaire Avec Qui Travailler.
Si Vous Travaillez En Groupe, Veuillez Suivre Les Instructions Ci-Dessous Car C'est Ainsi Que Cela Se Fait Dans Le Monde Réel.


Ce Que Nous Apprendrons
Vues Django, modèles, authentification, formulaires


Conseils
Lisez attentivement toutes les instructions

Commencez par réfléchir à la structure, prenez votre temps, vous n'avez pas besoin de coder tout de suite

Utilisez Trello pour gérer vos tâches en équipe. Créez un nouveau tableau sur Trello, partagez-le avec les membres de votre équipe et ajoutez vos tâches au tableau. Lorsque vous commencez à travailler sur une tâche, déplacez-la dans la colonne "En cours". Une fois que vous avez terminé, déplacez-le sur "Terminé".

Partagez votre code en équipe sur un dépôt github . N'oubliez pas que chaque tâche doit être développée dans sa propre branche git. Lorsque vous vous engagez dans votre branche locale, poussez également vers la branche distante. Une fois que vous avez terminé votre tâche, fusionnez votre branche avec master, puis appuyez sur master. Assurez-vous d'informer votre équipe lorsque vous avez terminé votre travail, afin qu'ils puissent fusionner votre travail quand ils le souhaitent.


Projet – Partie 1
Aujourd'hui, nous allons créer un site Web pour Torquay ("Tor-kee") Towers, un hôtel situé dans la campagne anglaise.
Le site aura deux interfaces (en plus de l'interface d'administration intégrée) :

une pour les visiteurs,
et un pour le personnel de l'hôtel.
Interface Visiteurs
Afficher des informations sur l'hôtel (emplacement, images, description, ce qu'il y a dans les environs, etc.)
Voir les disponibilités (dates de disponibilité des chambres)
Réserver un séjour à l'hôtel
Remplissez un formulaire demandant plus d'informations
Laisser un avis sur l'hôtel


Interface Du Personnel
Voir les réservations et les disponibilités
Ajouter, modifier et annuler des réservations
Lire les messages des clients demandant plus d'informations
Supprimer les avis (Nous ne voulons que des invités avec une touche de classe…)


Tâches
Créer un référentiel GitHub pour le projet (privé)
Pour les groupes
Ajoutez des autorisations pour tous les membres de l'équipe pour valider/écrire dans le référentiel.
Chaque membre de l'équipe doit le cloner sur son ordinateur local.

Construire le squelette de l'application Django
Incluez requirements.txt, .gitignore et le fuseau horaire correct dans les paramètres du projet.
Incluez les migrations pertinentes dans vos commits.

Créer un squelette d'application "visiteurs" .
Cela gérera l'interface des visiteurs, décrite ci-dessus.
Enregistrez l'application et son urlconfig dans le projet.
Incluez les migrations pertinentes dans vos commits.

Visiteurs : créer une page d'informations (dans l'application des visiteurs, créez une vue et un modèle pour la tâche ci-dessous)
Créez une page attrayante avec des paragraphes de texte intéressants et des images pertinentes. Assurez-vous d'utiliser le bon style CSS, etc.
Ajoutez des liens proéminents vers la page de réservation et la page des avis (ajoutez un lien factice (avec un nom mais la destination doit être #) - ceux-ci seront remplacés plus tard par le lien approprié).

Ajout de la barre de navigation :
Ajoutez une barre de navigation à votre modèle de base afin qu'elle soit visible sur toutes les pages du site.
Il contiendra un lien vers la page d'accueil à gauche, et les informations de connexion/déconnexion à droite (votre nom d'utilisateur et « Déconnexion » si vous êtes connecté, sinon un bouton « Connexion »).

Visiteurs : Créer des pages de connexion et de déconnexion
Vous aurez besoin d'urls, de fonctions d'affichage et de modèles…
Incluez les migrations pertinentes dans vos commits.
Mettez également à jour la barre de navigation pour inclure ces modifications.

Concevez des modèles pour représenter les chambres vacantes et les réservations d'hôtel .
Je vous recommande de le faire en tant que session de stratégie d'équipe, en prenant des notes mais sans écrire de code pour le moment.

Quelles informations devons-nous stocker ? Doit-on stocker les disponibilités, ou les réservations, ou les deux ?

Combien de chambres l'hôtel a-t-il ? Combien de personnes peuvent séjourner dans chaque chambre ?

Quel est le prix par chambre ? Ou par personne ?

Doit-il y avoir une durée minimum/maximum par séjour ?

Planifiez soigneusement les types de données et les structures. De combien de tables avez-vous besoin ? Quelles colonnes chaque tableau doit-il avoir ?

Écrivez également des algorithmes pour décider :
si un visiteur peut réserver un séjour (pour X personnes dans Y chambres, arrivée le jour C et départ le jour J).
comment montrer les postes vacants à l'utilisateur sur la page (dates, jours, chambres, personnes… ?)

Ces algorithmes seront codés ultérieurement.

Visiteurs : Construisez les modèles de la tâche précédente
Incluez les migrations pertinentes dans vos commits.
Assurez-vous que toutes les données sont visibles sur le site d'administration.

Visiteurs : créez une fonction d'affichage pour afficher les postes vacants appelée réservation .
À ce stade, nous avons seulement besoin d'obtenir les jours disponibles pour la réservation lors de l'obtention des informations de votre base de données.
Utilisez l'algorithme que vous avez développé précédemment.

Visiteurs : créer la page de réservation
concentrez-vous sur la bonne apparence de la page.
Affichez les options pertinentes, en fonction des disponibilités de l'hôtel.

Visiteurs : ajouter à la vue Réservation
Écrivez le code de vue pour gérer l'entrée d'une réservation, cela doit être ajouté à la vue qui récupère tous les postes vacants.
Validez les données ! Ne pas autoriser un visiteur à réserver avec des données invalides (séjour trop long/court, chambres déjà réservées, dates non libres, etc.)
"Câblez" ceci jusqu'à la page de réservation.
Assurez-vous que les données de réservation sont visibles sur le site d'administration.

Visiteurs : mettre en œuvre la page de demande d'informations.
Utilisez un formulaire pour obtenir les coordonnées et un SMS gratuit du visiteur.
Stockez les données dans la base de données, en utilisant l'ORM.
Assurez-vous que les données sont visibles sur le site d'administration.

