from datetime import datetime
from tokenize import blank_re
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser




# Create your models here.
#Model of extend my User
class User(AbstractUser):
    profil = models.ImageField(default='default.png', upload_to='profil') # photo par exple
    supprimer=models.BooleanField(default=False)
    role=models.CharField(max_length=20, default="Admin")
    dateSuppression=models.DateTimeField(null=True)
    
    

    

class Eleve(models.Model):
    matricule = models.IntegerField(primary_key=True)
    profil= models.ImageField(default='default.png', upload_to='profil')
    nom= models.CharField(max_length=70)
    prenom= models.CharField(max_length=90)
    dateNaissance = models.DateField()
    lieuNaissance=models.CharField(max_length=90)
    genre=models.CharField(max_length=10)
    nationalite=models.CharField(max_length=20)
    adresse=models.CharField(max_length=40)
    nomTuteur=models.CharField(max_length=70)
    prenomTuteur=models.CharField(max_length=90)
    contactTuteur=models.CharField(max_length=18)
    dateCreation=models.DateTimeField()
    supprimer=models.BooleanField(default=False)
    dateSuppression=models.DateTimeField(null=True)

    
class Matiere(models.Model):
    idMatiere = models.AutoField(primary_key=True)
    intituleMatiere= models.CharField(max_length=200)
    supprimer=models.BooleanField(default=False)
    dateSuppression=models.DateTimeField(null=True)
    dateCreation=models.DateTimeField()

    
class Classe(models.Model):
    idClasse = models.AutoField(primary_key=True)
    intituleClasse= models.CharField(max_length=100)
    supprimer=models.BooleanField(default=False)
    dateSuppression=models.DateTimeField(null=True)
    dateCreation=models.DateTimeField()


class AnneeScolaire(models.Model):
    idAnneeScolaire = models.AutoField(primary_key=True)
    intituleAnneeScolaire= models.CharField(max_length=50)
    etat=models.BooleanField(default=False)
    supprimer=models.BooleanField(default=False)
    dateSuppression=models.DateTimeField(null=True)
    dateCreation=models.DateTimeField()


class Inscription(models.Model):
    idInscription = models.AutoField(primary_key=True)
    matricule= models.ForeignKey(Eleve,on_delete=models.CASCADE)
    idClasse=models.ForeignKey(Classe,on_delete=models.CASCADE)
    dateInscription=models.DateTimeField()
    idAnneeScolaire=models.ForeignKey(AnneeScolaire,on_delete=models.CASCADE)
    supprimer=models.BooleanField(default=False)
    dateSuppression=models.DateTimeField(null=True)


class Enseignant(models.Model):
    
    matricule = models.CharField(max_length=70)
    dateNaissance = models.DateField()
    lieuNaissance=models.CharField(max_length=90)
    genre=models.CharField(max_length=10)
    nationalite=models.CharField(max_length=20)
    statut=models.CharField(max_length=90)
    telephone=models.CharField(max_length=18)
    adresse=models.CharField(max_length=40)
    nomPrenomPAB=models.CharField(max_length=100)
    contactPAB=models.CharField(max_length=18)
    idUser=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)



class EnseignantMatiere(models.Model):
    idEnseignantMatiere = models.AutoField(primary_key=True)
    enseignant= models.ForeignKey(Enseignant,on_delete=models.CASCADE)
    matiere=models.ForeignKey(Matiere,on_delete=models.CASCADE)
    dateAttribution=models.DateTimeField()
    supprimer=models.BooleanField(default=False)
    dateSuppression=models.DateTimeField(null=True)

class EnseignantClasseMatiere(models.Model):
    idEnseignantClasseMatiere = models.AutoField(primary_key=True)
    enseignant= models.ForeignKey(Enseignant,on_delete=models.CASCADE)
    matiere=models.ForeignKey(Matiere,on_delete=models.CASCADE)
    classe=models.ForeignKey(Classe,on_delete=models.CASCADE)
    coefficient= models.IntegerField(default=1)
    dateAttribution=models.DateTimeField()
    anneeScolaire=models.ForeignKey(AnneeScolaire,on_delete=models.CASCADE)
    supprimer=models.BooleanField(default=False)
    dateSuppression=models.DateTimeField(null=True)