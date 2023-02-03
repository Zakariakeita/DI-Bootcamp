Information : C'est un long projet ! Allez étape par étape. Ne vous pressez pas. Le but est de créer un code clair et bien structuré

N'oubliez pas de regarder la section Quelques Aides sous les Instructions



Ce Que Vous Allez Créer
Location de vélo et scooter

Nous allons créer un site Web simple pour gérer la location de vélos et de scooters pour une petite start-up de Tel Aviv. Ce sera l'interface entre les employés de l'entreprise pour créer et gérer les locations de vélos et de scooters.



Des Instructions:
Créez un nouvel environnement virtuel dans un nouveau répertoire de projet. Activez-le, installez Django et créez un projet appelé bike-store .

Créez une application appelée rent . Il gérera toutes les actions de location pour l'entreprise.

Des modèles:
Client
prénom
nom de famille
e-mail
numéro de téléphone
adresse
ville
pays

Véhicule
type de véhicule (clé étrangère du modèle de type de véhicule )
date créée
coût réel (combien ça coûte)
taille (clé étrangère du modèle de taille de véhicule )

Type de véhicule
Nom

Taille du véhicule
Nom

De location
date de location
date de retour
client (FK au client )
véhicule (FK à Véhicule )

Tarif de location
taux journalier
type de véhicule (FK à Type de véhicule )
taille du véhicule (FK à la taille du véhicule )

Remplir la table Customer avec de fausses données à l'aide de Faker

L'application doit avoir les URL suivantes :
/rent/rental/- afficher une liste de toutes les locations, non retournées en premier, puis classées par date croissante (la plus ancienne en premier)

/rent/rental/<pk>- afficher les informations sur la location donnée :
Détails du client
les détails du véhicule
détails de la location ("Retourné le :<date> " / "Pas encore restitué")

/rent/rental/add– fournir un formulaire pour saisir un identifiant client et un identifiant véhicule pour créer une location.
Si le client ou le véhicule n'existe pas, affichez un message d'erreur convivial.
Si le véhicule est actuellement en location, affichez un message d'erreur correspondant.

/rent/customer/<pk>- afficher le client correspondant à l'identifiant donné

/rent/customer/- afficher tous les clients, par ordre alphabétique

/rent/customer/add– fournir un formulaire pour ajouter un nouveau client

/rent/vehicle/- afficher tous les véhicules, regroupés dans leurs groupes ('vélo' et 'scooter')

/rent/vehicle/<pk>- montrer le véhicule spécifique
indiquez également s'il est actuellement loué

/rent/vehicle/add– fournir un formulaire pour ajouter un nouveau véhicule.
Voir ci-dessous "Interaction de page", pour vous guider avec les modèles



De L'aide
Créez quelques types de véhicules dans la base de données ('vélo', 'vélo électrique', 'scooter', 'jetpack', etc.)

Créez quelques tailles de véhicules - « petit », « moyen », « grand », « double », etc.

Créez quelques tarifs de location - combien facturer par jour pour un type et une taille de véhicule donnés, par ex. 4,99 par jour pour un petit vélo.

Créez 100 locations avec Faker. Utilisez des données aléatoires, mais faites attention aux points suivants :
la date de retour doit parfois êtrenull
la date de retour (si non nulle) doit être postérieure à la date de location
aucune de ces dates ne peut être dans le futur
si un véhicule est déjà loué et n'a pas été restitué, il ne doit pas être utilisé pour une nouvelle location.

Créez des pages pour toutes les URL répertoriées dans les consignes. Créez des vues conviviales pour toutes les pages et utilisez des formulaires si nécessaire.

Interaction avec les pages :
Liste des locations - cliquez sur une location et accédez à la page pour afficher cette location.

Détails de la location - cliquez sur le client pour accéder à la page client ; cliquez sur le véhicule pour accéder à la page du véhicule ; cliquez sur un bouton pour rendre le véhicule.

Ajouter une location – formulaire avec listes déroulantes pour sélectionner un client et un véhicule. (Nous espérons améliorer cette conception à un stade ultérieur). N'incluez pas les véhicules qui sont actuellement loués !

Détails du client - affichez également les locations passées et présentes - cliquez sur une location pour accéder à sa page de détails.

Ajouter un client - validation des données ! Assurez-vous que les valeurs données dans tous les champs sont correctes, que l'adresse e-mail est unique, etc.

Liste des véhicules – cliquez sur un véhicule pour voir ses détails. Faites un signe visuel pour montrer quels véhicules sont actuellement loués et lesquels sont disponibles.

Ajouter un véhicule - sélectionnez le type et la taille dans les listes déroulantes (sélectionnez les éléments)



