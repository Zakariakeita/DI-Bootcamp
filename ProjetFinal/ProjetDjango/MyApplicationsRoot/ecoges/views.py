from datetime import datetime
import email
from email import message
from multiprocessing import connection, context
from nis import match
from re import I, template
from tokenize import Number
from turtle import width
from urllib import request
from django.shortcuts import render,redirect
from django.forms.models import model_to_dict
from django.db import connection
from ecoges.models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
import random
from django.http import HttpResponse,FileResponse
from .decorator import *
from .outilsPdf import *
import io
from django.views.generic import View

"""
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch,cm
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter,A4
from reportlab.platypus import * """



nationalites=['Burkinabè','Malien', 'Nigérian','Nigérien','Ivoirien']
roles=['Directeur','Secretaire','Caissier','Enseignant']

"""
def pdfEleveInClasse(request,id):
    
    #creation d'un buffer
    buf=io.BytesIO()
    #creation d'un canvas
    c=canvas.Canvas(buf, pagesize=letter,bottomup=0)
    width,height= A4
    #creation d'un text object
    textob=c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica",14)
    #Ajout de ligne au text
    lines=[]
    myobjects=Inscription.objects.filter(matricule__supprimer=False,idClasse__supprimer=False,idAnneeScolaire__supprimer=False,supprimer=False,idAnneeScolaire__etat=True,idClasse=id).order_by("matricule")


    for myobject in myobjects:
        lines.append((str(myobject.matricule.matricule),myobject.matricule.nom,myobject.matricule.prenom,str(myobject.matricule.dateNaissance),myobject.matricule.genre,myobject.matricule.adresse))
   
    table=Table(lines,colWidths=[30 for i in range(1,7)], rowHeights=[30 for i in range(1,4)])
    #s=getSampleSttyleSheet()

    #for line in lines:
    #    textob.textLine(line)

    #data=[["A","B","C","D"],["A","B","C","D"],["A","B","C","D"],["A","B","C","D"]]
    #table=Table(data)
    style=TableStyle([
    ('INNERGRID',(0,0),(-1,-1),0.25,colors.black),('ALIGN',(0,0),(-1,-1),'CENTER'),('VALIGN',(0,0),(-1,-1),'MIDDLE')
    ])
    table.setStyle(style)
    table.wrapOn(c,width,height)
    table.drawOn(c,0 * cm, 5 * cm)
    #fin
    #c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0) 
    ##
    
    return FileResponse(buf,as_attachment=True,filename='eleves.pdf')
"""
class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = {
             'today': datetime.date.today(), 
             'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        pdf = render_to_pdf('ecoges/templates/pdf/mypdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

def printpdfView(request,id):
    class EleveClasse:
        def __init__(self,matricule,profil,nom,prenom,dateNaissance,lieuNaissance,genre,nationalite,adresse,nomTuteur,prenomTuteur,contactTuteur,idClasse,intituleClasse):
            self.matricule=matricule
            self.profil=profil
            self.nom=nom
            self.prenom=prenom
            self.dateNaissance=dateNaissance
            self.lieuNaissance= lieuNaissance
            self.genre= genre
            self.nationalite= nationalite
            self.adresse= adresse
            self.nomTuteur= nomTuteur
            self.prenomTuteur= prenomTuteur
            self.contactTuteur= contactTuteur
            self.idClasse= idClasse
            self.intituleClasse= intituleClasse

    cursor=connection.cursor()
    cursor.execute(''' SELECT ecoges_eleve.matricule,ecoges_eleve.profil,ecoges_eleve.nom, ecoges_eleve.prenom, ecoges_eleve."dateNaissance", ecoges_eleve."lieuNaissance", ecoges_eleve.genre, ecoges_eleve.nationalite, ecoges_eleve.adresse, ecoges_eleve."nomTuteur", ecoges_eleve."prenomTuteur", ecoges_eleve."contactTuteur",ecoges_classe."idClasse",ecoges_classe."intituleClasse"
        FROM ecoges_inscription , ecoges_classe, ecoges_eleve, ecoges_anneescolaire
        WHERE ecoges_eleve.matricule=ecoges_inscription.matricule_id
        AND ecoges_inscription."idClasse_id"=ecoges_classe."idClasse"
        AND ecoges_anneescolaire."idAnneeScolaire"=ecoges_inscription."idAnneeScolaire_id"
        And ecoges_anneescolaire.etat='True'
        And ecoges_anneescolaire.supprimer='False'
        AND ecoges_classe.supprimer='False'
        AND ecoges_inscription.supprimer='False'
        And ecoges_eleve.supprimer='False'
        And ecoges_classe."idClasse"=%s 
        ORDER BY ecoges_eleve.matricule ASC''',[id])

    listEleves=cursor.fetchall()
    listEleve=[]
    for i in listEleves:
        listEleve.append(EleveClasse(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13]))
        
   

    cursor.execute(''' SELECT ecoges_eleve.matricule,ecoges_eleve.profil,ecoges_eleve.nom, ecoges_eleve.prenom
        FROM ecoges_eleve
        WHERE  ecoges_eleve.supprimer='False'
        AND ecoges_eleve.matricule NOT IN (SELECT ecoges_inscription.matricule_id from ecoges_inscription,ecoges_anneescolaire,ecoges_eleve where ecoges_anneescolaire."idAnneeScolaire"=ecoges_inscription."idAnneeScolaire_id" and ecoges_eleve.matricule=ecoges_inscription.matricule_id and ecoges_inscription.supprimer='False' AND ecoges_anneescolaire.etat='True' and ecoges_eleve.supprimer='False' )
        ORDER BY ecoges_eleve.matricule''')
    valeur=cursor.fetchall()

    lists=[]
    eleve=Eleve
    for i in valeur:
        lists.append(eleve(matricule=i[0],profil=i[1],nom=i[2],prenom=i[3]))
   
    #listEleve=listEleves
    
    classe=Classe.objects.get(idClasse=id)
    context={
    'listEleve':listEleve,
    'lists':lists,
    'classeid':id,
    'classeintitule':classe.intituleClasse,
    'nationalites':nationalites,
    'user':request.user,
    'activeAnneeScolaire':AnneeScolaire.objects.filter(etat=True,supprimer=False).first()}
    return render(request,'ecoges/templates/pdf/mypdf1.html',context)
# View of admin

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleAdmin(login_url='sing_in')
def dashboardA(request):
    users=User.objects.all().filter(supprimer=False).exclude(Q(role='Admin')|Q(is_superuser=True))
    context={
    'users':users,
    'user':request.user,
    'activeAnneeScolaire':AnneeScolaire.objects.filter(etat=True,supprimer=False).first(),
    'roles':roles
    }
    return render(request,'ecoges/templates/Admin-view/dashboard.html',context)


@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleAdmin(login_url='sing_in')
def saveProfilA(request):
    if request.method == 'POST':
        #génération de mot de passe
        lowerCase="abcdefghijklmnopqrstuvwxyz"
        upperCase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        number="1234567890"
        combinaison=lowerCase+upperCase+number
        passwordLength=8
        yourPassword="".join(random.sample(combinaison,passwordLength))
        if 'profil' in request.FILES:
            profil=request.FILES['profil']
            nom=request.POST['nom'].upper()
            prenom=request.POST['prenom'].title()
            email=request.POST['email']
            role=request.POST['role']
           
            user=User.objects.filter(email=email,supprimer=False).first()
            if user is not None:
                print("user exit")
                return redirect('dashboardA')
            else:
                user1=User.objects.filter(first_name=prenom, last_name=nom,supprimer=False).first()
                if user1 is not None:
                    print("user exit")
                    return redirect('dashboardA')
                else:
                    #concatenation du mot de passe
                    tab=(((nom+" "+prenom).lower()).split(" "))
                    username=""
                    for i in range(len(tab)):
                        if(i != (len(tab)-1)):
                            username=username + tab[i]+ "_"
                        else:
                            username=username + tab[i]

                    myUser= User(first_name=prenom, last_name=nom,username=username,password=yourPassword, email=email,profil=profil,role=role, date_joined=datetime.now())
                    myUser.set_password(yourPassword)
                    #envoie de message par mail
                    yourName=((myUser.first_name).upper() +" " +(myUser.last_name).upper())
                    yourEmail=myUser.email
                    message="Bonjour "+" "+yourName+", \n\nNous vous confirmons l\'ouverture de votre compte sur ECO-GES. \n\nVeuillez utiliser les identifiants suivants pour vous connecter à votre compte : \n \nEmail : "+yourEmail+"\nMot de passe : "+yourPassword +" \n\nCordialement Merci\n\nCopyrigth 2022 ECO-GES (CEG de Siankoro). All rights reserved."
                    try:
                        send_mail(
                                    'Notification de ECO-GES',
                                    message ,
                                    'settings.EMAIL_HOST_USER',
                                    [yourEmail],
                                    fail_silently=False
                                 )
                        print("###########"+ yourPassword +"###############")
                        myUser.save()
                        return redirect('dashboardA')

                    except:
                        print("###########"+ yourPassword +"###############")
                        return redirect('dashboardA')
   
        else:
            
            nom=request.POST['nom'].upper()
            prenom=request.POST['prenom'].title()
            email=request.POST['email']
            role=request.POST['role']

            user=User.objects.filter(email=email,supprimer=False).first()
            if user is not None:
                print("user exit")
                return redirect('dashboardA')
            else:
                user1=User.objects.filter(first_name=prenom, last_name=nom, supprimer=False).first()
                if user1 is not None:
                    print("user exit")
                    return redirect('dashboardA')
                else:
                    #concatenation du mot de passe
                    tab=(((nom+" "+prenom).lower()).split(" "))
                    username=""
                    for i in range(len(tab)):
                        if(i != (len(tab)-1)):
                            username=username + tab[i]+ "_"
                        else:
                            username=username + tab[i]

                    myUser= User(first_name=prenom, last_name=nom,username=username,password=yourPassword, email=email,role=role, date_joined=datetime.now())
                    myUser.set_password(yourPassword)
                    #envoie de message par mail
                    yourName=((myUser.first_name).upper() +" " +(myUser.last_name).upper())
                    yourEmail=myUser.email
                    message="Bonjour "+" "+yourName+", \n\nNous vous confirmons l\'ouverture de votre compte sur ECO-GES. \n\nVeuillez utiliser les identifiants suivants pour vous connecter à votre compte : \n \nEmail : "+yourEmail+"\nMot de passe : "+yourPassword +" \n\nCordialement Merci\n\nCopyrigth 2022 ECO-GES (CEG de Siankoro). All rights reserved."
                    try:
                        send_mail(
                                    'Notification de ECO-GES',
                                    message ,
                                    'settings.EMAIL_HOST_USER',
                                    [yourEmail],
                                    fail_silently=False
                                 )
                        print("###########"+ yourPassword +"###############")
                        myUser.save()
                        return redirect('dashboardA')
                        
                    except:
                        print("###########"+ yourPassword +"###############")
                        return redirect('dashboardA')
   
     
    return redirect ('dashboardA')


@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleAdmin(login_url='sing_in')
def updateProfilA(request,id):
    if request.method == 'POST':
        myUser=User.objects.get(id=id) 
        if 'profil' in request.FILES:
            profil=request.FILES['profil']
        else:
            profil=myUser.profil
        nom=request.POST['nom'].upper()
        prenom=request.POST['prenom'].title()
        email=request.POST['email']
        user=User.objects.filter(id=id,supprimer=False).first()
        if user is not None:
            if(user.email==email):
                #concatenation du mot de passe
                tab=(((nom+" "+prenom).lower()).split(" "))
                username=""
                for i in range(len(tab)):
                    if(i != (len(tab)-1)):
                        username=username + tab[i]+ "_"
                    else:
                        username=username + tab[i]

                us=User.objects.filter(username=username,supprimer=False).first()
                if (myUser.username != username and (us is not None)):
                    return redirect('dashboardA')
                else:
                    myUser.profil=profil
                    myUser.first_name=prenom
                    myUser.username=username
                    myUser.last_name=nom
                    myUser.email=email
                    myUser.role=myUser.role
                    myUser.date_joined=myUser.date_joined
                    myUser.password=myUser.password

                    myUser.save()
                    return redirect('dashboardA')
            else:
                user1=User.objects.filter(email=email,supprimer=False).first()
                if user1 is not None:
                    print("ereur il existe")
                    return redirect('dashboardA')
                else:
                    #concatenation du mot de passe
                    tab=(((nom+" "+prenom).lower()).split(" "))
                    username=""
                    for i in range(len(tab)):
                        if(i != (len(tab)-1)):
                            username=username + tab[i]+ "_"
                        else:
                            username=username + tab[i]

                    us=User.objects.filter(username=username,supprimer=False).first()
                    if (myUser.username != username and (us is not None)):
                        return redirect('dashboardA')
                    else:
                        myUser.profil=profil
                        myUser.first_name=prenom
                        myUser.username=username
                        myUser.last_name=nom
                        myUser.email=email
                        myUser.role=myUser.role
                        myUser.date_joined=myUser.date_joined
                        myUser.password=myUser.password
                        myUser.save()                   
                        return redirect('dashboardA')
                
        else:
            print("user n'esxite pas")
            return redirect('dashboardA')
            
        
@login_required(login_url='sing_in') 
@cache_control(no_cache=True, must_revalidate=True, no_store=True) 
@roleAdmin(login_url='sing_in')     
def deleteProfilA(request,id):
    user=User.objects.filter(id=id).update(supprimer=True,dateSuppression=datetime.now())
    return redirect('dashboardA')






def createUser(request):
    myUser = User(profil=request.POST['profil'], nom=request.POST['nom'], prenom=request.POST['prenom'], 
    email=request.POST['email'], role=request.POST['role'])
    myUser.save()
    return redirect('dashboardA')


# ************View of secretary *************** #

#View dashbord.html of secretary
@login_required(login_url='sing_in')
@roleSecretaire(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dashboardS(request):
    cursor=connection.cursor()
    cursor.execute(''' SELECT count(ecoges_eleve.matricule)
        FROM ecoges_inscription , ecoges_classe, ecoges_eleve, ecoges_anneescolaire
        WHERE ecoges_eleve.matricule=ecoges_inscription.matricule_id
        AND ecoges_inscription."idClasse_id"=ecoges_classe."idClasse"
        AND ecoges_anneescolaire."idAnneeScolaire"=ecoges_inscription."idAnneeScolaire_id"
        And ecoges_anneescolaire.etat='True'
        And ecoges_anneescolaire.supprimer='False'
        AND ecoges_classe.supprimer='False'
        AND ecoges_inscription.supprimer='False'
        And ecoges_eleve.supprimer='False'
        AND  ecoges_eleve.genre='Masculin' ''')
    masculin=cursor.fetchone()

    cursor.execute(''' SELECT count(ecoges_eleve.matricule)
        FROM ecoges_inscription , ecoges_classe, ecoges_eleve, ecoges_anneescolaire
        WHERE ecoges_eleve.matricule=ecoges_inscription.matricule_id
        AND ecoges_inscription."idClasse_id"=ecoges_classe."idClasse"
        AND ecoges_anneescolaire."idAnneeScolaire"=ecoges_inscription."idAnneeScolaire_id"
        And ecoges_anneescolaire.etat='True'
        And ecoges_anneescolaire.supprimer='False'
        AND ecoges_classe.supprimer='False'
        AND ecoges_inscription.supprimer='False'
        And ecoges_eleve.supprimer='False'
        AND  ecoges_eleve.genre='Feminin' ''')
    feminin=cursor.fetchone()

    cursor.execute(''' SELECT count(ecoges_eleve.matricule)
        FROM ecoges_inscription , ecoges_classe, ecoges_eleve, ecoges_anneescolaire
        WHERE ecoges_eleve.matricule=ecoges_inscription.matricule_id
        AND ecoges_inscription."idClasse_id"=ecoges_classe."idClasse"
        AND ecoges_anneescolaire."idAnneeScolaire"=ecoges_inscription."idAnneeScolaire_id"
        And ecoges_anneescolaire.etat='True'
        And ecoges_anneescolaire.supprimer='False'
        AND ecoges_classe.supprimer='False'
        AND ecoges_inscription.supprimer='False'
        And ecoges_eleve.supprimer='False'
         ''')
    total=cursor.fetchone()

    context={'user':request.user,
    'masculin':masculin[0],'feminin':feminin[0],'total':total[0],'enseignant':Enseignant.objects.filter(idUser__supprimer=False).count(),
    'activeAnneeScolaire':AnneeScolaire.objects.filter(etat=True,supprimer=False).first()}
    return render(request,'ecoges/templates/Secretary-view/dashboard.html',context)


#view inscription.html
@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleSecretaire(login_url='sing_in')
def inscription(request):
    eleves=Eleve.objects.all().filter(supprimer=False).order_by("matricule")
    classe=Classe.objects.all().filter(supprimer=False)
    context={
        'eleves':eleves,
        'nationalites': nationalites,
         'classes':classe,
         'user':request.user,
         'activeAnneeScolaire':AnneeScolaire.objects.filter(etat=True,supprimer=False).first()
    }
    return render(request,'ecoges/templates/Secretary-view/inscription.html',context)

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleSecretaire(login_url='sing_in')
def inscriptionEleve(request,id):
    if request.method =='POST':
        matricule=Eleve.objects.get(matricule=id)
        idClasse=Classe.objects.get(idClasse=request.POST['classe'])
        anneeScolaire=AnneeScolaire.objects.get(etat=True)
        ins=Inscription.objects.filter(matricule=matricule,idClasse=idClasse,idAnneeScolaire=anneeScolaire,supprimer=False).count()
        if ins==0:
            inscription=Inscription(matricule=matricule,idClasse=idClasse,dateInscription=datetime.now(),idAnneeScolaire=anneeScolaire)
            inscription.save()
        
    return redirect('inscription')

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleSecretaire(login_url='sing_in')
def saveEleveIns(request):
    if request.method =='POST':
        if 'profil' in request.FILES:
            profil=request.FILES['profil']
            nom=request.POST['nom'].upper()
            prenom=request.POST['prenom'].title()
            dateNaissance=request.POST['dateNaissance']
            lieuNaissance=request.POST['lieuNaissance'].title()
            genre=request.POST['genre']
            nationalite=request.POST['nationalite']
            adresse=request.POST['adresse'].title()
            nomTuteur=request.POST['nomTuteur'].upper()
            prenomTuteur=request.POST['prenomTuteur'].title()
            contactTuteur=request.POST['contactTuteur']
            
            cursor=connection.cursor()
            cursor.execute('''SELECT matricule FROM ecoges_Eleve WHERE matricule= (select Max(matricule) from ecoges_Eleve)''')
            mat=cursor.fetchone()
          
            myMat=AnneeScolaire.objects.filter(etat=True,supprimer=False).first()
            if myMat is not None:
                if(mat==None):
                    matricule=int(myMat.intituleAnneeScolaire[0:4] +"001")
                    dateCreation=datetime.now()
                    eleve=Eleve(matricule=matricule,profil=profil,nom=nom,prenom=prenom,dateNaissance=dateNaissance,lieuNaissance=lieuNaissance,genre=genre,nationalite=nationalite,adresse=adresse,nomTuteur=nomTuteur,prenomTuteur=prenomTuteur,contactTuteur=contactTuteur,dateCreation=dateCreation)
                else:
                    dateCreation=datetime.now()
                    if (str(mat[0])[0:4])==str(myMat.intituleAnneeScolaire[0:4]) :
                        eleve=Eleve(matricule=(int(mat[0])+1),profil=profil,nom=nom,prenom=prenom,dateNaissance=dateNaissance,lieuNaissance=lieuNaissance,genre=genre,nationalite=nationalite,adresse=adresse,nomTuteur=nomTuteur,prenomTuteur=prenomTuteur,contactTuteur=contactTuteur,dateCreation=dateCreation)
                    else:
                        matricule=int(myMat.intituleAnneeScolaire[0:4] +"001")
                        eleve=Eleve(matricule=matricule,profil=profil,nom=nom,prenom=prenom,dateNaissance=dateNaissance,lieuNaissance=lieuNaissance,genre=genre,nationalite=nationalite,adresse=adresse,nomTuteur=nomTuteur,prenomTuteur=prenomTuteur,contactTuteur=contactTuteur,dateCreation=dateCreation)
                
                eleve.save()
                return redirect('inscription')

            else:
                return redirect('inscription')
        else:   
            nom=request.POST['nom'].upper()
            prenom=request.POST['prenom'].title()
            dateNaissance=request.POST['dateNaissance']
            lieuNaissance=request.POST['lieuNaissance'].title()
            genre=request.POST['genre']
            nationalite=request.POST['nationalite']
            adresse=request.POST['adresse'].title()
            nomTuteur=request.POST['nomTuteur'].upper()
            prenomTuteur=request.POST['prenomTuteur'].title()
            contactTuteur=request.POST['contactTuteur']
            
            cursor=connection.cursor()
            cursor.execute('''SELECT matricule FROM ecoges_Eleve WHERE matricule= (select Max(matricule) from ecoges_Eleve)''')
            mat=cursor.fetchone()

            myMat=AnneeScolaire.objects.filter(etat=True,supprimer=False).first()
            if myMat is not None:
                if(mat==None):
                    matricule=int(myMat.intituleAnneeScolaire[0:4] +"001")
                    dateCreation=datetime.now()
                    eleve=Eleve(matricule=matricule,nom=nom,prenom=prenom,dateNaissance=dateNaissance,lieuNaissance=lieuNaissance,genre=genre,nationalite=nationalite,adresse=adresse,nomTuteur=nomTuteur,prenomTuteur=prenomTuteur,contactTuteur=contactTuteur,dateCreation=dateCreation)
                else:
                    dateCreation=datetime.now()
                    if (str(mat[0])[0:4])==str(myMat.intituleAnneeScolaire[0:4]) :
                        eleve=Eleve(matricule=(int(mat[0])+1),nom=nom,prenom=prenom,dateNaissance=dateNaissance,lieuNaissance=lieuNaissance,genre=genre,nationalite=nationalite,adresse=adresse,nomTuteur=nomTuteur,prenomTuteur=prenomTuteur,contactTuteur=contactTuteur,dateCreation=dateCreation)
                    else:
                        matricule=int(myMat.intituleAnneeScolaire[0:4] +"001")
                        eleve=Eleve(matricule=matricule,nom=nom,prenom=prenom,dateNaissance=dateNaissance,lieuNaissance=lieuNaissance,genre=genre,nationalite=nationalite,adresse=adresse,nomTuteur=nomTuteur,prenomTuteur=prenomTuteur,contactTuteur=contactTuteur,dateCreation=dateCreation)
                
                eleve.save()
                return redirect('inscription')

            else:
                return redirect('inscription')
        
           
    
@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleSecretaire(login_url='sing_in')
def  updateEleveIns(request,id):
    eleve=Eleve.objects.get(matricule=id)
    if request.method =='POST':
        if 'profil' in request.FILES:
            eleve.profil=request.FILES['profil']
        else:
            eleve.profil=eleve.profil
            
        eleve.matricule=id
        eleve.nom=request.POST['nom'].upper()
        eleve.prenom=request.POST['prenom'].title() 
        eleve.dateNaissance=request.POST['dateNaissance']
        eleve.lieuNaissance=request.POST['lieuNaissance'].title()
        eleve.genre=request.POST['genre']
        eleve.nationalite=request.POST['nationalite']
        eleve.adresse=request.POST['adresse'].title()
        eleve.nomTuteur=request.POST['nomTuteur'].upper()
        eleve.prenomTuteur=request.POST['prenomTuteur'].title()
        eleve.contactTuteur=request.POST['contactTuteur']
        eleve.dateCreation=eleve.dateCreation
        
        eleve.save()
    return redirect('inscription')

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleSecretaire(login_url='sing_in')
def deleteEleveIns(request,id):
    Eleve.objects.filter(matricule=id).update(supprimer=True,dateSuppression=datetime.now())
    return redirect('inscription')


#view eleve.html
@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteurSecretaire(login_url='sing_in')
def eleve(request):
    eleves=Eleve.objects.all().filter(supprimer=False).order_by("matricule")
    context={
        'eleves':eleves,
        'nationalites':nationalites,
        'user':request.user,
        'activeAnneeScolaire':AnneeScolaire.objects.filter(etat=True,supprimer=False).first()
    }
    return render(request,'ecoges/templates/Secretary-view/eleve.html',context)

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteurSecretaire(login_url='sing_in')
def saveEleve(request):
    
    if request.method =='POST':
        if 'profil' in request.FILES:
            profil=request.FILES['profil']
            nom=request.POST['nom'].upper()
            prenom=request.POST['prenom'].title()
            dateNaissance=request.POST['dateNaissance']
            lieuNaissance=request.POST['lieuNaissance'].title()
            genre=request.POST['genre']
            nationalite=request.POST['nationalite']
            adresse=request.POST['adresse'].title()
            nomTuteur=request.POST['nomTuteur'].upper()
            prenomTuteur=request.POST['prenomTuteur'].title()
            contactTuteur=request.POST['contactTuteur']
            
            cursor=connection.cursor()
            cursor.execute('''SELECT matricule FROM ecoges_Eleve WHERE matricule= (select Max(matricule) from ecoges_Eleve)''')
            mat=cursor.fetchone()
          
            myMat=AnneeScolaire.objects.filter(etat=True,supprimer=False).first()
            if myMat is not None:
                if(mat==None):
                    matricule=int(myMat.intituleAnneeScolaire[0:4] +"001")
                    dateCreation=datetime.now()
                    eleve=Eleve(matricule=matricule,profil=profil,nom=nom,prenom=prenom,dateNaissance=dateNaissance,lieuNaissance=lieuNaissance,genre=genre,nationalite=nationalite,adresse=adresse,nomTuteur=nomTuteur,prenomTuteur=prenomTuteur,contactTuteur=contactTuteur,dateCreation=dateCreation)
                else:
                    dateCreation=datetime.now()
                    if (str(mat[0])[0:4])==str(myMat.intituleAnneeScolaire[0:4]) :
                        eleve=Eleve(matricule=(int(mat[0])+1),profil=profil,nom=nom,prenom=prenom,dateNaissance=dateNaissance,lieuNaissance=lieuNaissance,genre=genre,nationalite=nationalite,adresse=adresse,nomTuteur=nomTuteur,prenomTuteur=prenomTuteur,contactTuteur=contactTuteur,dateCreation=dateCreation)
                    else:
                        matricule=int(myMat.intituleAnneeScolaire[0:4] +"001")
                        eleve=Eleve(matricule=matricule,profil=profil,nom=nom,prenom=prenom,dateNaissance=dateNaissance,lieuNaissance=lieuNaissance,genre=genre,nationalite=nationalite,adresse=adresse,nomTuteur=nomTuteur,prenomTuteur=prenomTuteur,contactTuteur=contactTuteur,dateCreation=dateCreation)
                
                eleve.save()
                return redirect('eleve')

            else:
                return redirect('eleve')
        else:   
            nom=request.POST['nom'].upper()
            prenom=request.POST['prenom'].title()
            dateNaissance=request.POST['dateNaissance']
            lieuNaissance=request.POST['lieuNaissance'].title()
            genre=request.POST['genre']
            nationalite=request.POST['nationalite']
            adresse=request.POST['adresse'].title()
            nomTuteur=request.POST['nomTuteur'].upper()
            prenomTuteur=request.POST['prenomTuteur'].title()
            contactTuteur=request.POST['contactTuteur']
            
            cursor=connection.cursor()
            cursor.execute('''SELECT matricule FROM ecoges_Eleve WHERE matricule= (select Max(matricule) from ecoges_Eleve)''')
            mat=cursor.fetchone()

            myMat=AnneeScolaire.objects.filter(etat=True,supprimer=False).first()
            if myMat is not None:
                if(mat==None):
                    matricule=int(myMat.intituleAnneeScolaire[0:4] +"001")
                    dateCreation=datetime.now()
                    eleve=Eleve(matricule=matricule,nom=nom,prenom=prenom,dateNaissance=dateNaissance,lieuNaissance=lieuNaissance,genre=genre,nationalite=nationalite,adresse=adresse,nomTuteur=nomTuteur,prenomTuteur=prenomTuteur,contactTuteur=contactTuteur,dateCreation=dateCreation)
                else:
                    dateCreation=datetime.now()
                    if (str(mat[0])[0:4])==str(myMat.intituleAnneeScolaire[0:4]) :
                        eleve=Eleve(matricule=(int(mat[0])+1),nom=nom,prenom=prenom,dateNaissance=dateNaissance,lieuNaissance=lieuNaissance,genre=genre,nationalite=nationalite,adresse=adresse,nomTuteur=nomTuteur,prenomTuteur=prenomTuteur,contactTuteur=contactTuteur,dateCreation=dateCreation)
                    else:
                        matricule=int(myMat.intituleAnneeScolaire[0:4] +"001")
                        eleve=Eleve(matricule=matricule,nom=nom,prenom=prenom,dateNaissance=dateNaissance,lieuNaissance=lieuNaissance,genre=genre,nationalite=nationalite,adresse=adresse,nomTuteur=nomTuteur,prenomTuteur=prenomTuteur,contactTuteur=contactTuteur,dateCreation=dateCreation)
                
                eleve.save()
                return redirect('eleve')

            else:
                return redirect('eleve')
     
@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def edit(request):
    eleves=Eleve.objects.all().filter(supprimer=False).order_by("matricule")
    context={
        'eleves':eleves,
        'nationalites':nationalites
    }
    return redirect('eleve')

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteurSecretaire(login_url='sing_in')
def  updateEleve(request,id):
    eleve=Eleve.objects.get(matricule=id)
    if request.method =='POST':
        if 'profil' in request.FILES:
            eleve.profil=request.FILES['profil']
        else:
            eleve.profil=eleve.profil

        eleve.matricule=id
        eleve.nom=request.POST['nom'].upper()
        eleve.prenom=request.POST['prenom'].title()
        eleve.dateNaissance=request.POST['dateNaissance']
        eleve.lieuNaissance=request.POST['lieuNaissance'].title()
        eleve.genre=request.POST['genre']
        eleve.nationalite=request.POST['nationalite']
        eleve.adresse=request.POST['adresse'].title()
        eleve.nomTuteur=request.POST['nomTuteur'].upper()
        eleve.prenomTuteur=request.POST['prenomTuteur'].title()
        eleve.contactTuteur=request.POST['contactTuteur']
        eleve.dateCreation=eleve.dateCreation
        
        eleve.save()
    return redirect('eleve')

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteurSecretaire(login_url='sing_in')
def deleteEleve(request,id):
    Eleve.objects.filter(matricule=id).update(supprimer=True,dateSuppression=datetime.now())
    return redirect('eleve')

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteurSecretaire(login_url='sing_in')
def contentEleve(request,id):
    eleve=Eleve.objects.get(matricule=id)
    context={
        'eleve':eleve,
        'user':request.user,
        'activeAnneeScolaire':AnneeScolaire.objects.filter(etat=True,supprimer=False).first()
    }
    
    return render(request,'ecoges/templates/Secretary-view/contentEleve.html',context)


#view classe.html
@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteurSecretaire(login_url='sing_in')
def classe(request):
    class ContentClasse:
        def __init__(self,idClasse,intituleClasse,masculin,feminin,total):
            self.idClasse=idClasse
            self.intituleClasse=intituleClasse
            self.masculin=masculin
            self.feminin=feminin
            self.total= total
   
    classe=Classe.objects.all().filter(supprimer=False) 
    listClasseContent=[]
    
    cursor=connection.cursor()
    for i in classe:
        cursor.execute('''	SELECT count(ecoges_eleve.matricule)
        FROM ecoges_inscription , ecoges_classe, ecoges_eleve, ecoges_anneescolaire
        WHERE ecoges_eleve.matricule=ecoges_inscription.matricule_id
        AND ecoges_inscription."idClasse_id"=ecoges_classe."idClasse"
        AND ecoges_anneescolaire."idAnneeScolaire"=ecoges_inscription."idAnneeScolaire_id"
        And ecoges_anneescolaire.etat='True'
        And ecoges_anneescolaire.supprimer='False'
        AND ecoges_classe.supprimer='False'
        AND ecoges_inscription.supprimer='False'
        And ecoges_eleve.supprimer='False'
        And ecoges_classe."idClasse"=%s
        And ecoges_eleve.genre='Masculin' ''',[i.idClasse])
        masculin=cursor.fetchone()

        cursor.execute('''	SELECT count(ecoges_eleve.matricule)
        FROM ecoges_inscription , ecoges_classe, ecoges_eleve, ecoges_anneescolaire
        WHERE ecoges_eleve.matricule=ecoges_inscription.matricule_id
        AND ecoges_inscription."idClasse_id"=ecoges_classe."idClasse"
        AND ecoges_anneescolaire."idAnneeScolaire"=ecoges_inscription."idAnneeScolaire_id"
        And ecoges_anneescolaire.etat='True'
        And ecoges_anneescolaire.supprimer='False'
        AND ecoges_classe.supprimer='False'
        AND ecoges_inscription.supprimer='False'
        And ecoges_eleve.supprimer='False'
        And ecoges_classe."idClasse"=%s
        And ecoges_eleve.genre='Feminin' ''',[i.idClasse])
        feminin=cursor.fetchone()

        cursor.execute('''	SELECT count(ecoges_eleve.matricule)
        FROM ecoges_inscription , ecoges_classe, ecoges_eleve, ecoges_anneescolaire
        WHERE ecoges_eleve.matricule=ecoges_inscription.matricule_id
        AND ecoges_inscription."idClasse_id"=ecoges_classe."idClasse"
        AND ecoges_anneescolaire."idAnneeScolaire"=ecoges_inscription."idAnneeScolaire_id"
        And ecoges_anneescolaire.etat='True'
        And ecoges_anneescolaire.supprimer='False'
        AND ecoges_classe.supprimer='False'
        AND ecoges_inscription.supprimer='False'
        And ecoges_eleve.supprimer='False'
        And ecoges_classe."idClasse"=%s ''',[i.idClasse])
        total=cursor.fetchone()
      
        listClasseContent.append(ContentClasse(i.idClasse,i.intituleClasse,masculin[0],feminin[0],total[0]))
  
    
    context={
             'listClasseContent':listClasseContent,
             'user':request.user,
             'activeAnneeScolaire':AnneeScolaire.objects.filter(etat=True,supprimer=False).first(),
             'classe':Classe.objects.filter(supprimer=False)
            }
    return render(request,'ecoges/templates/Secretary-view/classe.html',context)

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteurSecretaire(login_url='sing_in')
def saveClasse(request):
    if request.method =='POST':
        intituleClasse=request.POST['intituleClasse'].title()
        dateCreation=datetime.now()
        classe=Classe(intituleClasse=intituleClasse,dateCreation=dateCreation)
        classe.save()
    return redirect('classe')

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteurSecretaire(login_url='sing_in')
def  updateClasse(request,id):
    classe=Classe.objects.get(idClasse=id)
    if request.method =='POST':
        classe.idClasse=id
        classe.intituleClasse=request.POST['intituleClasse'].title()
        classe.dateCreation=classe.dateCreation
        classe.save()
    return redirect('classe')

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteurSecretaire(login_url='sing_in')
def deleteClasse(request,id):
    Classe.objects.filter(idClasse=id).update(supprimer=True,dateSuppression=datetime.now())
    return redirect('classe')

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteurSecretaire(login_url='sing_in')
def classeContent(request,id):
    class EleveClasse:
        def __init__(self,matricule,profil,nom,prenom,dateNaissance,lieuNaissance,genre,nationalite,adresse,nomTuteur,prenomTuteur,contactTuteur,idClasse,intituleClasse):
            self.matricule=matricule
            self.profil=profil
            self.nom=nom
            self.prenom=prenom
            self.dateNaissance=dateNaissance
            self.lieuNaissance= lieuNaissance
            self.genre= genre
            self.nationalite= nationalite
            self.adresse= adresse
            self.nomTuteur= nomTuteur
            self.prenomTuteur= prenomTuteur
            self.contactTuteur= contactTuteur
            self.idClasse= idClasse
            self.intituleClasse= intituleClasse

    cursor=connection.cursor()
    cursor.execute(''' SELECT ecoges_eleve.matricule,ecoges_eleve.profil,ecoges_eleve.nom, ecoges_eleve.prenom, ecoges_eleve."dateNaissance", ecoges_eleve."lieuNaissance", ecoges_eleve.genre, ecoges_eleve.nationalite, ecoges_eleve.adresse, ecoges_eleve."nomTuteur", ecoges_eleve."prenomTuteur", ecoges_eleve."contactTuteur",ecoges_classe."idClasse",ecoges_classe."intituleClasse"
        FROM ecoges_inscription , ecoges_classe, ecoges_eleve, ecoges_anneescolaire
        WHERE ecoges_eleve.matricule=ecoges_inscription.matricule_id
        AND ecoges_inscription."idClasse_id"=ecoges_classe."idClasse"
        AND ecoges_anneescolaire."idAnneeScolaire"=ecoges_inscription."idAnneeScolaire_id"
        And ecoges_anneescolaire.etat='True'
        And ecoges_anneescolaire.supprimer='False'
        AND ecoges_classe.supprimer='False'
        AND ecoges_inscription.supprimer='False'
        And ecoges_eleve.supprimer='False'
        And ecoges_classe."idClasse"=%s 
        ORDER BY ecoges_eleve.matricule ASC''',[id])

    listEleves=cursor.fetchall()
    listEleve=[]
    for i in listEleves:
        listEleve.append(EleveClasse(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13]))
        
   

    cursor.execute(''' SELECT ecoges_eleve.matricule,ecoges_eleve.profil,ecoges_eleve.nom, ecoges_eleve.prenom
        FROM ecoges_eleve
        WHERE  ecoges_eleve.supprimer='False'
        AND ecoges_eleve.matricule NOT IN (SELECT ecoges_inscription.matricule_id from ecoges_inscription,ecoges_anneescolaire,ecoges_eleve where ecoges_anneescolaire."idAnneeScolaire"=ecoges_inscription."idAnneeScolaire_id" and ecoges_eleve.matricule=ecoges_inscription.matricule_id and ecoges_inscription.supprimer='False' AND ecoges_anneescolaire.etat='True' and ecoges_eleve.supprimer='False' )
        ORDER BY ecoges_eleve.matricule''')
    valeur=cursor.fetchall()

    lists=[]
    eleve=Eleve
    for i in valeur:
        lists.append(eleve(matricule=i[0],profil=i[1],nom=i[2],prenom=i[3]))
   
    #listEleve=listEleves
    
    classe=Classe.objects.get(idClasse=id)
    context={
    'listEleve':listEleve,
    'lists':lists,
    'classeid':id,
    'classeintitule':classe.intituleClasse,
    'nationalites':nationalites,
    'user':request.user,
    'activeAnneeScolaire':AnneeScolaire.objects.filter(etat=True,supprimer=False).first()}
    return render(request,'ecoges/templates/Secretary-view/classeContent.html',context)

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteurSecretaire(login_url='sing_in')
def updateEleveFromClasse(request,id1,id):
    
    eleve=Eleve.objects.get(matricule=id1)
    
    if request.method =='POST':
        if 'profil' in request.FILES:
            eleve.profil=request.FILES['profil']
        else:
            eleve.profil=eleve.profil

        eleve.matricule=id1
        eleve.nom=request.POST['nom'].upper()
        eleve.prenom=request.POST['prenom'].title()
        eleve.dateNaissance=request.POST['dateNaissance']
        eleve.lieuNaissance=request.POST['lieuNaissance'].title()
        eleve.genre=request.POST['genre']
        eleve.nationalite=request.POST['nationalite']
        eleve.adresse=request.POST['adresse'].title()
        eleve.nomTuteur=request.POST['nomTuteur'].upper()
        eleve.prenomTuteur=request.POST['prenomTuteur'].title()
        eleve.contactTuteur=request.POST['contactTuteur']
        eleve.dateCreation=eleve.dateCreation
        
        eleve.save()
       
    return redirect('classeContent',id=id)

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteurSecretaire(login_url='sing_in')
def deleteEleveFromClasse(request,id1,id):
    Inscription.objects.filter(matricule=id1,idClasse=id).update(supprimer=True,dateSuppression=datetime.now())
    return redirect('classeContent',id=id)

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteurSecretaire(login_url='sing_in')
def classeContentEleve(request,id,id1):
    eleve=Eleve.objects.get(matricule=id)
    classe=Classe.objects.get(idClasse=id1)
    context={'eleve':eleve,
    'user':request.user,'activeAnneeScolaire':AnneeScolaire.objects.filter(etat=True,supprimer=False).first(),
    'classe':classe}
   
    return render(request,'ecoges/templates/Secretary-view/classeContentEleve.html',context)

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteurSecretaire(login_url='sing_in')
def inscriptionContentClasse(request,id):
    if request.method =='POST':
        matricule=Eleve.objects.get(matricule=request.POST['matricule'])
        idClasse=Classe.objects.get(idClasse=id)
    
    anneeScolaire=AnneeScolaire.objects.get(etat=True)
    ins=Inscription.objects.filter(matricule=matricule,idClasse=idClasse,idAnneeScolaire=anneeScolaire,supprimer=False).count()
    if ins==0:
        inscription=Inscription(matricule=matricule,idClasse=idClasse,dateInscription=datetime.now(),idAnneeScolaire=anneeScolaire)
        inscription.save()
    
    return redirect('classeContent',id=id)

#View matiere.html
@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteurSecretaire(login_url='sing_in')
def matiere(request):
    matiere=Matiere.objects.all().filter(supprimer=False).order_by("intituleMatiere")
    context={'matieres':matiere,
    'user':request.user,'activeAnneeScolaire':AnneeScolaire.objects.filter(etat=True,supprimer=False).first()}
    return render(request,'ecoges/templates/Secretary-view/matiere.html',context)

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteurSecretaire(login_url='sing_in')
def saveMatiere(request):
    if request.method =='POST':
        intituleMatiere=request.POST['intituleMatiere'].title()
        an=Matiere.objects.filter(intituleMatiere=intituleMatiere).first()

        if an is None:
            matiere=Matiere(intituleMatiere=intituleMatiere,dateCreation=datetime.now())
            matiere.save()
        else:
            print("Existe")
         
    return redirect('matiere')

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteurSecretaire(login_url='sing_in')
def  updateMatiere(request,id):
    matiere=Matiere.objects.get(idMatiere=id)
    if request.method =='POST':
        matiere.idMatiere=id
        matiere.intituleMatiere=request.POST['intituleMatiere'].title()
        matiere.dateCreation=matiere.dateCreation
        matiere.save()
    return redirect('matiere')


@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteurSecretaire(login_url='sing_in')
def deleteMatiere(request,id):
    Matiere.objects.filter(idMatiere=id).update(supprimer=True,dateSuppression=datetime.now())
    return redirect('matiere')


#View enseignant.html
@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteurSecretaire(login_url='sing_in')
def enseignant(request):
    enseignants=Enseignant.objects.filter(idUser__supprimer=False)
    matieres=Matiere.objects.filter(supprimer=False).order_by('intituleMatiere')
        

    context={'nationalites':nationalites,
    'enseignants':enseignants,
    'user':request.user,
    'activeAnneeScolaire':AnneeScolaire.objects.filter(etat=True,supprimer=False).first(),
    'matieres': matieres,
    }
    return render(request,'ecoges/templates/Secretary-view/enseignant.html',context)

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteurSecretaire(login_url='sing_in')
def saveEnseignant(request):
    if request.method == 'POST':
        #génération de mot de passe
        lowerCase="abcdefghijklmnopqrstuvwxyz"
        upperCase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        number="1234567890"
        combinaison=lowerCase+upperCase+number
        passwordLength=8
        yourPassword="".join(random.sample(combinaison,passwordLength))
        if 'profil' in request.FILES:
            profil=request.FILES['profil']
            nom=request.POST['nom'].upper()
            matricule=request.POST['matricule']
            prenom=request.POST['prenom'].title()
            email=request.POST['email']
            role='Enseignant'
            dateNaissance=request.POST['dateNaissance']
            lieuNaissance=request.POST['lieuNaissance'].title()
            genre=request.POST['genre']
            nationalite=request.POST['nationalite']
            adresse=request.POST['adresse'].title()
            nomPrenomPAB=request.POST['nomPrenomPAB'].upper()
            contactPAB=request.POST['contactPAB']
            statut=request.POST['statut']
            telephone=request.POST['telephone']

            user=User.objects.filter(email=email,supprimer=False).first()
            if user is not None:
                print("user exit")
                return redirect('enseignant')
            else:
                user1=User.objects.filter(first_name=prenom, last_name=nom,supprimer=False).first()
                if user1 is not None:
                    print("user exit")
                    return redirect('enseignant')
                else:
                    #concatenation du mot de passe
                    tab=(((nom+" "+prenom).lower()).split(" "))
                    username=""
                    for i in range(len(tab)):
                        if(i != (len(tab)-1)):
                            username=username + tab[i]+ "_"
                        else:
                            username=username + tab[i]

                    myUser= User(first_name=prenom, last_name=nom,username=username,password=yourPassword, email=email,profil=profil,role=role, date_joined=datetime.now())
                    myUser.set_password(yourPassword)
                    #envoie de message par mail
                    yourName=((myUser.first_name).upper() +" " +(myUser.last_name).upper())
                    yourEmail=myUser.email
                    message="Bonjour "+" "+yourName+", \n\nNous vous confirmons l\'ouverture de votre compte \' Enseignant \' sur ECO-GES. \n\nVeuillez utiliser les identifiants suivants pour vous connecter à votre compte : \n \nEmail : "+yourEmail+"\nMot de passe : "+yourPassword +" \n\nCordialement Merci\n\nCopyrigth 2022 ECO-GES (CEG de Siankoro). All rights reserved."
                    try:
                        send_mail(
                                    'Notification de ECO-GES',
                                    message ,
                                    'settings.EMAIL_HOST_USER',
                                    [yourEmail],
                                    fail_silently=False
                                 )
                        print("###########"+ yourPassword +"###############")
                        myUser.save()
                        enseignant=Enseignant(matricule=matricule,statut=statut,telephone=telephone,adresse=adresse,nomPrenomPAB=nomPrenomPAB,contactPAB=contactPAB,dateNaissance=dateNaissance, lieuNaissance=lieuNaissance,genre=genre,nationalite=nationalite, idUser=myUser)

                        enseignant.save()
                        return redirect('enseignant')

                    except:
                        print("###########"+ yourPassword +"###############")
                        return redirect('enseignant')
   
        else:
            
            nom=request.POST['nom'].upper()
            prenom=request.POST['prenom'].title()
            matricule=request.POST['matricule']
            email=request.POST['email']
            role='Enseignant'
            dateNaissance=request.POST['dateNaissance']
            lieuNaissance=request.POST['lieuNaissance'].title()
            genre=request.POST['genre']
            nationalite=request.POST['nationalite']
            adresse=request.POST['adresse'].title()
            nomPrenomPAB=request.POST['nomPrenomPAB'].upper()
            contactPAB=request.POST['contactPAB']
            statut=request.POST['statut']
            telephone=request.POST['telephone']

            user=User.objects.filter(email=email,supprimer=False).first()
            if user is not None:
                print("user exit")
                return redirect('enseignant')
            else:
                user1=User.objects.filter(first_name=prenom, last_name=nom, supprimer=False).first()
                if user1 is not None:
                    print("user exit")
                    return redirect('enseignant')
                else:
                    #concatenation du mot de passe
                    tab=(((nom+" "+prenom).lower()).split(" "))
                    username=""
                    for i in range(len(tab)):
                        if(i != (len(tab)-1)):
                            username=username + tab[i]+ "_"
                        else:
                            username=username + tab[i]

                    myUser= User(first_name=prenom, last_name=nom,username=username,password=yourPassword, email=email,role=role, date_joined=datetime.now())
                    myUser.set_password(yourPassword)
                    #envoie de message par mail
                    yourName=((myUser.first_name).upper() +" " +(myUser.last_name).upper())
                    yourEmail=myUser.email
                    message="Bonjour "+" "+yourName+", \n\nNous vous confirmons l\'ouverture de votre compte \' Enseignant \' sur ECO-GES. \n\nVeuillez utiliser les identifiants suivants pour vous connecter à votre compte : \n \nEmail : "+yourEmail+"\nMot de passe : "+yourPassword +" \n\nCordialement Merci\n\nCopyrigth 2022 ECO-GES (CEG de Siankoro). All rights reserved."
                    try:
                        send_mail(
                                    'Notification de ECO-GES',
                                    message ,
                                    'settings.EMAIL_HOST_USER',
                                    [yourEmail],
                                    fail_silently=False
                                 )
                        print("###########"+ yourPassword +"###############")
                        myUser.save()
                        enseignant=Enseignant(matricule=matricule,statut=statut,telephone=telephone,adresse=adresse,nomPrenomPAB=nomPrenomPAB,contactPAB=contactPAB,dateNaissance=dateNaissance, lieuNaissance=lieuNaissance,genre=genre,nationalite=nationalite, idUser=myUser)
                        enseignant.save()
                        return redirect('enseignant')
                        
                    except:
                        print("###########"+ yourPassword +"###############")
                        return redirect('enseignant')
   
    return redirect('enseignant')

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteurSecretaire(login_url='sing_in')
def updateEnseignant(request,id):
    if request.method == 'POST':
        myUser=User.objects.get(id=id) 
        if 'profil' in request.FILES:
            profil=request.FILES['profil']
        else:
            profil=myUser.profil
        nom=request.POST['nom'].upper()
        prenom=request.POST['prenom'].title()
        email=request.POST['email']
        matricule=request.POST['matricule']
        dateNaissance=request.POST['dateNaissance']
        lieuNaissance=request.POST['lieuNaissance'].title()
        genre=request.POST['genre']
        nationalite=request.POST['nationalite']
        adresse=request.POST['adresse'].title()
        nomPrenomPAB=request.POST['nomPrenomPAB'].upper()
        contactPAB=request.POST['contactPAB']
        statut=request.POST['statut']
        telephone=request.POST['telephone']

        user=User.objects.filter(id=id,supprimer=False).first()
        if user is not None:
            myEnseignant=Enseignant.objects.get(idUser=myUser.id)
            #ON verifie si l'email a été modifier ou pas
            if(user.email==email):
                #concatenation du username
                tab=(((nom+" "+prenom).lower()).split(" "))
                username=""
                for i in range(len(tab)):
                    if(i != (len(tab)-1)):
                        username=username + tab[i]+ "_"
                    else:
                        username=username + tab[i]
                #on verifie si le username former n'existe pas déja
                us=User.objects.filter(username=username,supprimer=False).first()
                if (myUser.username != username and (us is not None)):
                    return redirect('enseignant')
                else:
                    #enregistrement du profil enseignant dans la table user
                    myUser.profil=profil
                    myUser.first_name=prenom
                    myUser.username=username
                    myUser.last_name=nom
                    myUser.email=email
                    myUser.role=myUser.role
                    myUser.date_joined=myUser.date_joined
                    myUser.password=myUser.password

                    myUser.save()
                    # enregistrement de l'enseignant dans la table enseignant
                    myEnseignant.dateNaissance=dateNaissance
                    myEnseignant.matricule=matricule
                    myEnseignant.lieuNaissance=lieuNaissance
                    myEnseignant.adresse=adresse
                    myEnseignant.telephone=telephone
                    myEnseignant.statut=statut
                    myEnseignant.genre=genre
                    myEnseignant.nationalite=nationalite
                    myEnseignant.nomPrenomPAB=nomPrenomPAB
                    myEnseignant.contactPAB=contactPAB
                    myEnseignant.idUser=myUser

                    myEnseignant.save()
                    return redirect('enseignant')

            else:
                user1=User.objects.filter(email=email,supprimer=False).first()
                if user1 is not None:
                    print("ereur il existe")
                    return redirect('enseignant')
                else:
                    #concatenation du username
                    tab=(((nom+" "+prenom).lower()).split(" "))
                    username=""
                    for i in range(len(tab)):
                        if(i != (len(tab)-1)):
                            username=username + tab[i]+ "_"
                        else:
                            username=username + tab[i]
                            
                    us=User.objects.filter(username=username,supprimer=False).first()
                    #on verifie voir si notre nouveau username à été modifier ou pas et si il existe un objet ayant ce username
                    if (myUser.username != username and (us is not None)):
                        return redirect('enseignant')
                    else:
                        myUser.profil=profil
                        myUser.first_name=prenom
                        myUser.username=username
                        myUser.last_name=nom
                        myUser.email=email
                        myUser.role=myUser.role
                        myUser.date_joined=myUser.date_joined
                        myUser.password=myUser.password

                        myUser.save()
                        # enregistrement de l'enseignant dans la table enseignant
                        myEnseignant.dateNaissance=dateNaissance
                        myEnseignant.matricule=matricule
                        myEnseignant.lieuNaissance=lieuNaissance
                        myEnseignant.adresse=adresse
                        myEnseignant.telephone=telephone
                        myEnseignant.statut=statut
                        myEnseignant.genre=genre
                        myEnseignant.nationalite=nationalite
                        myEnseignant.nomPrenomPAB=nomPrenomPAB
                        myEnseignant.contactPAB=contactPAB
                        myEnseignant.idUser=myUser

                        myEnseignant.save()                 
                        return redirect('enseignant')
                
        else:
            print("user n'esxite pas")
            return redirect('enseignant')
       
    return redirect('enseignant')

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteurSecretaire(login_url='sing_in')
def deleteEnseignant(request,id):
    User.objects.filter(id=id).update(supprimer=True,dateSuppression=datetime.now())
    return redirect('enseignant')

#attribution des matière à un enseignant
@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteurSecretaire(login_url='sing_in')
def attrMatiere(request,id):
    if request.method == 'POST':
        if request.POST.get('mesMatieres'):
            matieres=request.POST.get('mesMatieres')
            #Nous voulons supprimer la dernière espace vide de la chaine renvoyer
            matieres= (matieres[0:len(str(matieres))-1]).split(",")
            enseignant=Enseignant.objects.get(idUser=id)
            #Nous enregistrons chaque matière avec l'enseignant
            for i in range(len(matieres)):
                print(matieres[i])
                matiere=Matiere.objects.get(idMatiere=matieres[i])
                existe=EnseignantMatiere.objects.filter(enseignant=enseignant,matiere=matiere).first()
                if existe is None:
                    enseignantMatiere=EnseignantMatiere(enseignant=enseignant,matiere=matiere,dateAttribution=datetime.now())
                    enseignantMatiere.save()
    return redirect('enseignant')



#affichage de la page qui contient les infos personnels de l'enseignant
@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteurSecretaire(login_url='sing_in')
def enseignantContent(request,id):
    matieres=Matiere.objects.filter(supprimer=False).order_by('intituleMatiere')
    enseignant=Enseignant.objects.get(idUser=id)
    mesMatieres=EnseignantMatiere.objects.all().filter(enseignant=enseignant,supprimer=False)   
    listMatiere=[]
   
   
    for i in mesMatieres:
        listMatiere.append(i.matiere.idMatiere)

    context={'enseignant':enseignant,
    'matieres':matieres, 'mesMatiere':mesMatieres,
    'listMatiere':listMatiere,'user':request.user,
    'activeAnneeScolaire':AnneeScolaire.objects.filter(etat=True,supprimer=False).first(),}
    return render(request,'ecoges/templates/Secretary-view/contentEnseignant.html',context)

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteurSecretaire(login_url='sing_in')
def attrMatiereFromEnseignant(request, id):
    if request.method == 'POST':
        if request.POST.get('mesMatieres'):
            matieres=request.POST.get('mesMatieres')
            #Nous voulons supprimer la dernière espace vide de la chaine renvoyer
            matieres= (matieres[0:len(str(matieres))-1]).split(",")
            enseignant=Enseignant.objects.get(idUser=id)
            #Nous enregistrons chaque matière avec l'enseignant
            for i in range(len(matieres)):
                matiere=Matiere.objects.get(idMatiere=matieres[i])
                existe=EnseignantMatiere.objects.filter(enseignant=enseignant,matiere=matiere,supprimer=False).first()
                if existe is None:
                    enseignantMatiere=EnseignantMatiere(enseignant=enseignant,matiere=matiere,dateAttribution=datetime.now())
                    enseignantMatiere.save()

    return redirect('enseignantContent',id=id)

#Modification de l'attribution de la matière à l'enseignant
@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteurSecretaire(login_url='sing_in')
def updAttrMatiereFromEnseignant(request,id):
    if request.method == 'POST':
        if request.POST.get('mesMatieres'):
            matieres=request.POST.get('mesMatieres')
            #Nous voulons supprimer la dernière espace vide de la chaine renvoyer
            matieres= (matieres[0:len(str(matieres))-1]).split(",")

            enseignant=Enseignant.objects.get(idUser=id)
            #Nous supprimons d'abord les ancienne données avant d'ajouter de nouveaux
            EnseignantMatiere.objects.filter(enseignant=enseignant).update(supprimer=True,dateSuppression=datetime.now())

            #Nous enregistrons chaque matière avec l'enseignant
            for i in range(len(matieres)):
                matiere=Matiere.objects.get(idMatiere=matieres[i])

                existe=EnseignantMatiere.objects.filter(enseignant=enseignant,matiere=matiere,supprimer=False).first()
                if existe is None:
                    enseignantMatiere=EnseignantMatiere(enseignant=enseignant,matiere=matiere,dateAttribution=datetime.now())
                    enseignantMatiere.save()
        else:
            enseignant=Enseignant.objects.get(idUser=id)
            EnseignantMatiere.objects.filter(enseignant=enseignant).update(supprimer=True,dateSuppression=datetime.now())
 
    return redirect('enseignantContent',id=id)
 
# *************View of Director**************#
# fonction pour voir le contenu de classe et matière attribuer à un ensegnant
@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteur(login_url='sing_in')
def attribClasseMatiere(request,id):
    enseignant=Enseignant.objects.get(idUser=id)
    classe=Classe.objects.all().filter(supprimer=False)
    mesMatieres=EnseignantMatiere.objects.all().filter(enseignant=enseignant,supprimer=False) 
    anneeScolaire=AnneeScolaire.objects.filter(etat=True,supprimer=False).first()
    mesClasseMatieres=EnseignantClasseMatiere.objects.filter(enseignant=enseignant,supprimer=False,anneeScolaire=anneeScolaire)
    context={'user':request.user,
    'activeAnneeScolaire':anneeScolaire,
    'enseignant':enseignant,
    'classe':classe,
    'mesMatieres':mesMatieres,
    'mesClasseMatieres':mesClasseMatieres}
    return render(request,'ecoges/templates/Director-view/attribClasseMatiere.html',context)

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteur(login_url='sing_in')
def attribClasseMatiereToEnseignant(request,id):
    if request.method == 'POST':
        idClasse=request.POST['idClasse']
        idMatiere=request.POST['idMatiere']
        coefficient=request.POST['coefficient']
        classe=Classe.objects.get(idClasse=idClasse)
        matiere=Matiere.objects.get(idMatiere=idMatiere)
        enseignant=Enseignant.objects.get(idUser=id)
        anneeScolaire=AnneeScolaire.objects.filter(etat=True,supprimer=False).first()
        #Verifiactions si la classe et la matière n'existe pas déja
        existe=EnseignantClasseMatiere.objects.filter(enseignant=enseignant,matiere=matiere,classe=classe,supprimer=False).first()
        if existe is None:
            enseignantClasseMatiere=EnseignantClasseMatiere(enseignant=enseignant,matiere=matiere,classe=classe,anneeScolaire=anneeScolaire,coefficient=coefficient,dateAttribution=datetime.now())
            enseignantClasseMatiere.save()
    return redirect('attribClasseMatiere',id=id)

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteur(login_url='sing_in')
def updateCoefficient(request,id,id2):
    if request.method == 'POST':
        coef=request.POST['coefficient']
        EnseignantClasseMatiere.objects.filter(idEnseignantClasseMatiere=id2).update(coefficient=coef)
    return redirect('attribClasseMatiere',id=id)

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteur(login_url='sing_in')
def deleteEnseignantClasseMatiere(request, id,id2):
    EnseignantClasseMatiere.objects.filter(idEnseignantClasseMatiere=id2).update(supprimer=True,dateSuppression=datetime.now())
    return redirect('attribClasseMatiere',id=id)

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteur(login_url='sing_in')
def dashboardD(request):
    cursor=connection.cursor()
    cursor.execute(''' SELECT count(ecoges_eleve.matricule)
        FROM ecoges_inscription , ecoges_classe, ecoges_eleve, ecoges_anneescolaire
        WHERE ecoges_eleve.matricule=ecoges_inscription.matricule_id
        AND ecoges_inscription."idClasse_id"=ecoges_classe."idClasse"
        AND ecoges_anneescolaire."idAnneeScolaire"=ecoges_inscription."idAnneeScolaire_id"
        And ecoges_anneescolaire.etat='True'
        And ecoges_anneescolaire.supprimer='False'
        AND ecoges_classe.supprimer='False'
        AND ecoges_inscription.supprimer='False'
        And ecoges_eleve.supprimer='False'
        AND  ecoges_eleve.genre='Masculin' ''')
    masculin=cursor.fetchone()

    cursor.execute(''' SELECT count(ecoges_eleve.matricule)
        FROM ecoges_inscription , ecoges_classe, ecoges_eleve, ecoges_anneescolaire
        WHERE ecoges_eleve.matricule=ecoges_inscription.matricule_id
        AND ecoges_inscription."idClasse_id"=ecoges_classe."idClasse"
        AND ecoges_anneescolaire."idAnneeScolaire"=ecoges_inscription."idAnneeScolaire_id"
        And ecoges_anneescolaire.etat='True'
        And ecoges_anneescolaire.supprimer='False'
        AND ecoges_classe.supprimer='False'
        AND ecoges_inscription.supprimer='False'
        And ecoges_eleve.supprimer='False'
        AND  ecoges_eleve.genre='Feminin' ''')
    feminin=cursor.fetchone()

    cursor.execute(''' SELECT count(ecoges_eleve.matricule)
        FROM ecoges_inscription , ecoges_classe, ecoges_eleve, ecoges_anneescolaire
        WHERE ecoges_eleve.matricule=ecoges_inscription.matricule_id
        AND ecoges_inscription."idClasse_id"=ecoges_classe."idClasse"
        AND ecoges_anneescolaire."idAnneeScolaire"=ecoges_inscription."idAnneeScolaire_id"
        And ecoges_anneescolaire.etat='True'
        And ecoges_anneescolaire.supprimer='False'
        AND ecoges_classe.supprimer='False'
        AND ecoges_inscription.supprimer='False'
        And ecoges_eleve.supprimer='False'
         ''')
    total=cursor.fetchone()
    context={'user':request.user,
    'masculin':masculin[0],'feminin':feminin[0],'total':total[0],'enseignant':Enseignant.objects.filter(idUser__supprimer=False).count(),
    'activeAnneeScolaire':AnneeScolaire.objects.filter(etat=True,supprimer=False).first()}
    return render(request,'ecoges/templates/Director-view/dashboard.html',context)
   

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteur(login_url='sing_in')
def saveProfilD(request):
    if request.method == 'POST':
        #génération de mot de passe
        lowerCase="abcdefghijklmnopqrstuvwxyz"
        upperCase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        number="1234567890"
        combinaison=lowerCase+upperCase+number
        passwordLength=8
        yourPassword="".join(random.sample(combinaison,passwordLength))
        if 'profil' in request.FILES:
            profil=request.FILES['profil']
            nom=request.POST['nom'].upper()
            prenom=request.POST['prenom'].title()
            email=request.POST['email']
            role=request.POST['role']
           
            user=User.objects.filter(email=email,supprimer=False).first()
            if user is not None:
                print("user exit")
                return redirect('profilD')
            else:
                user1=User.objects.filter(first_name=prenom, last_name=nom,supprimer=False).first()
                if user1 is not None:
                    print("user exit")
                    return redirect('profilD')
                else:
                    #concatenation du mot de passe
                    tab=(((nom+" "+prenom).lower()).split(" "))
                    username=""
                    for i in range(len(tab)):
                        if(i != (len(tab)-1)):
                            username=username + tab[i]+ "_"
                        else:
                            username=username + tab[i]

                    myUser= User(first_name=prenom, last_name=nom,username=username,password=yourPassword, email=email,profil=profil,role=role, date_joined=datetime.now())
                    myUser.set_password(yourPassword)
                    #envoie de message par mail
                    yourName=((myUser.first_name).upper() +" " +(myUser.last_name).upper())
                    yourEmail=myUser.email
                    message="Bonjour "+" "+yourName+", \n\nNous vous confirmons l\'ouverture de votre compte sur ECO-GES. \n\nVeuillez utiliser les identifiants suivants pour vous connecter à votre compte : \n \nEmail : "+yourEmail+"\nMot de passe : "+yourPassword +" \n\nCordialement Merci\n\nCopyrigth 2022 ECO-GES (CEG de Siankoro). All rights reserved."
                    try:
                        send_mail(
                                    'Notification de ECO-GES',
                                    message ,
                                    'settings.EMAIL_HOST_USER',
                                    [yourEmail],
                                    fail_silently=False
                                 )
                        print("###########"+ yourPassword +"###############")
                        myUser.save()
                        return redirect('profilD')

                    except:
                        print("###########"+ yourPassword +"###############")
                        return redirect('profilD')
   
        else:
            
            nom=request.POST['nom'].upper()
            prenom=request.POST['prenom'].title()
            email=request.POST['email']
            role=request.POST['role']

            user=User.objects.filter(email=email,supprimer=False).first()
            if user is not None:
                print("user exit")
                return redirect('profilD')
            else:
                user1=User.objects.filter(first_name=prenom, last_name=nom, supprimer=False).first()
                if user1 is not None:
                    print("user exit")
                    return redirect('profilD')
                else:
                    #concatenation du mot de passe
                    tab=(((nom+" "+prenom).lower()).split(" "))
                    username=""
                    for i in range(len(tab)):
                        if(i != (len(tab)-1)):
                            username=username + tab[i]+ "_"
                        else:
                            username=username + tab[i]

                    myUser= User(first_name=prenom, last_name=nom,username=username,password=yourPassword, email=email,role=role, date_joined=datetime.now())
                    myUser.set_password(yourPassword)
                    #envoie de message par mail
                    yourName=((myUser.first_name).upper() +" " +(myUser.last_name).upper())
                    yourEmail=myUser.email
                    message="Bonjour "+" "+yourName+", \n\nNous vous confirmons l\'ouverture de votre compte sur ECO-GES. \n\nVeuillez utiliser les identifiants suivants pour vous connecter à votre compte : \n \nEmail : "+yourEmail+"\nMot de passe : "+yourPassword +" \n\nCordialement Merci\n\nCopyrigth 2022 ECO-GES (CEG de Siankoro). All rights reserved."
                    try:
                        send_mail(
                                    'Notification de ECO-GES',
                                    message ,
                                    'settings.EMAIL_HOST_USER',
                                    [yourEmail],
                                    fail_silently=False
                                 )
                        print("###########"+ yourPassword +"###############")
                        myUser.save()
                        return redirect('profilD')
                        
                    except:
                        print("###########"+ yourPassword +"###############")
                        return redirect('profilD')
   
     
    return redirect ('profilD')

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteur(login_url='sing_in')
def profilD(request):
    users=User.objects.all().filter(supprimer=False).exclude(Q(role='Admin')|Q(is_superuser=True))
    context={
    'users':users,
    'user':request.user,
    'activeAnneeScolaire':AnneeScolaire.objects.filter(etat=True,supprimer=False).first(),
    'roles':roles}

    return render(request,'ecoges/templates/Director-view/profil.html',context)

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteur(login_url='sing_in')
def updateProfilD(request,id):
    if request.method == 'POST':
        myUser=User.objects.get(id=id) 
        if 'profil' in request.FILES:
            profil=request.FILES['profil']
        else:
            profil=myUser.profil
        nom=request.POST['nom'].upper()
        prenom=request.POST['prenom'].title()
        email=request.POST['email']
        user=User.objects.filter(id=id,supprimer=False).first()
        if user is not None:
            if(user.email==email):
                #concatenation du mot de passe
                tab=(((nom+" "+prenom).lower()).split(" "))
                username=""
                for i in range(len(tab)):
                    if(i != (len(tab)-1)):
                        username=username + tab[i]+ "_"
                    else:
                        username=username + tab[i]

                us=User.objects.filter(username=username,supprimer=False).first()
                if (myUser.username != username and (us is not None)):
                    return redirect('profilD')
                else:
                    myUser.profil=profil
                    myUser.first_name=prenom
                    myUser.username=username
                    myUser.last_name=nom
                    myUser.email=email
                    myUser.role=myUser.role
                    myUser.date_joined=myUser.date_joined
                    myUser.password=myUser.password

                    myUser.save()
                    return redirect('profilD')
            else:
                user1=User.objects.filter(email=email,supprimer=False).first()
                if user1 is not None:
                    print("ereur il existe")
                    return redirect('profilD')
                else:
                    #concatenation du mot de passe
                    tab=(((nom+" "+prenom).lower()).split(" "))
                    username=""
                    for i in range(len(tab)):
                        if(i != (len(tab)-1)):
                            username=username + tab[i]+ "_"
                        else:
                            username=username + tab[i]
                            
                    us=User.objects.filter(username=username,supprimer=False).first()
                    if (myUser.username != username and (us is not None)):
                        return redirect('profilD')
                    else:
                        myUser.profil=profil
                        myUser.first_name=prenom
                        myUser.username=username
                        myUser.last_name=nom
                        myUser.email=email
                        myUser.role=myUser.role
                        myUser.date_joined=myUser.date_joined
                        myUser.password=myUser.password
                        myUser.save()                   
                        return redirect('profilD')
                
        else:
            print("user n'esxite pas")
            return redirect('profilD')
            
        
@login_required(login_url='sing_in') 
@cache_control(no_cache=True, must_revalidate=True, no_store=True) 
@roleDirecteur(login_url='sing_in')     
def deleteProfilD(request,id):
    User.objects.filter(id=id).update(supprimer=True,dateSuppression=datetime.now())
    return redirect('profilD')

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleCaissierDirecteur(login_url='sing_in')
def depense(request):
    context={'user':request.user,'activeAnneeScolaire':AnneeScolaire.objects.filter(etat=True,supprimer=False).first()}
    return render(request,'ecoges/templates/Director-view/depense.html',context)

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteur(login_url='sing_in')
def configurationD(request):
    anneeScolaire=AnneeScolaire.objects.all().filter(supprimer=False).order_by("intituleAnneeScolaire")
    classe=Classe.objects.filter(supprimer=False)
    
    context={'anneeScolaire':anneeScolaire,
        'user':request.user,
        'activeAnneeScolaire':AnneeScolaire.objects.filter(etat=True,supprimer=False).first(),
        'enseignants':Enseignant.objects.filter(idUser__supprimer=False),
        'classe':classe
        }
    
    return render(request,'ecoges/templates/Director-view/configuration.html',context)

#fonction pour afficher les matière par classe
@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteur(login_url='sing_in')
def chercherClasseMatiere(request):
    if request.method == 'POST':
        anneeScolaire=AnneeScolaire.objects.filter(etat=True,supprimer=False).first()
        classe=Classe.objects.get(idClasse=request.POST['classe'])
        ens=EnseignantClasseMatiere.objects.filter(classe=classe,anneeScolaire=anneeScolaire,supprimer=False)
        
        mydict={}
        #on récupère chaque couple matière et coefficient qu'on met dans un dictionnaire
        for i in ens:
            mydict[i.matiere.intituleMatiere]=i.coefficient
        
        request.session['mesMatieres'] ={'mesMatieres':mydict}
        request.session['choix'] =classe.idClasse
      
    return redirect('configurationD')

def chercherClasseEnseignant(request):
    if request.method == 'POST':
        anneeScolaire=AnneeScolaire.objects.filter(etat=True,supprimer=False).first()
        classe=Classe.objects.get(idClasse=request.POST['classe'])
        ens=EnseignantClasseMatiere.objects.all().filter(classe=classe,anneeScolaire=anneeScolaire,supprimer=False)
        
        mydict={}
        #on récupère chaque couple matière et coefficient qu'on met dans un dictionnaire 
        for i in ens:
            mydict[i.enseignant.idUser.last_name + " "+ i.enseignant.idUser.first_name + ("*"*i.idEnseignantClasseMatiere)]=i.matiere.intituleMatiere
        request.session['mesEnseignant1'] ={'mesEnseignant1':mydict}
        request.session['choix1'] =classe.idClasse
    return redirect('classe')


def chercherMatiereEnseignant(request):
    if request.method == 'POST':
        matiere=Matiere.objects.get(idMatiere=request.POST['matiere'])
        ens=EnseignantMatiere.objects.all().filter(matiere=matiere,supprimer=False)
        
        mydict={}
        #on récupère chaque couple matière et coefficient qu'on met dans un dictionnaire 
        for i in ens:
            mydict[i.enseignant.idUser.last_name + " "+ i.enseignant.idUser.first_name + ("*"*i.idEnseignantMatiere)]=[i.enseignant.statut ,i.enseignant.telephone]
            print(len(i.enseignant.idUser.last_name + " "+ i.enseignant.idUser.first_name ))
        request.session['mesEnseignant2'] ={'mesEnseignant2':mydict}
        request.session['choix2'] =matiere.idMatiere
    return redirect('matiere')

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteur(login_url='sing_in')
def saveAnneeScolaire(request):
    if request.method == 'POST':
        intituleAnneeScolaire=request.POST['intituleAnneeScolaire']
        an=AnneeScolaire.objects.filter(intituleAnneeScolaire=intituleAnneeScolaire).first()

        if an is None:
            anneeScolaire=AnneeScolaire(intituleAnneeScolaire=intituleAnneeScolaire,dateCreation=datetime.now())
            anneeScolaire.save()
        else:
            print("Existe")
    return redirect('configurationD')

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteur(login_url='sing_in')
def updateAnneeScolaire(request,id):
    
    if request.method == 'POST':
        anneeScolaire=AnneeScolaire.objects.filter(idAnneeScolaire=id).update(intituleAnneeScolaire=request.POST['intituleAnneeScolaire'])
    return redirect('configurationD')

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteur(login_url='sing_in')
def deleteAnneeScolaire(request,id):
    AnneeScolaire.objects.filter(idAnneeScolaire=id).update(supprimer=True,dateSuppression=datetime.now())
    return redirect('configurationD')

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleDirecteur(login_url='sing_in')
def activateAnneeScolaire(request):
    if request.method =='POST':
        AnneeScolaire.objects.all().update(etat=False)
        AnneeScolaire.objects.filter(idAnneeScolaire=request.POST['idAnneeScolaire']).update(etat=True)
    return redirect('configurationD')


#**************View of Teacher****************#
@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleEnseignant(login_url='sing_in')
def dashboardP(request):
    cursor=connection.cursor()
    cursor.execute(''' SELECT count(ecoges_eleve.matricule)
        FROM ecoges_inscription , ecoges_classe, ecoges_eleve, ecoges_anneescolaire
        WHERE ecoges_eleve.matricule=ecoges_inscription.matricule_id
        AND ecoges_inscription."idClasse_id"=ecoges_classe."idClasse"
        AND ecoges_anneescolaire."idAnneeScolaire"=ecoges_inscription."idAnneeScolaire_id"
        And ecoges_anneescolaire.etat='True'
        And ecoges_anneescolaire.supprimer='False'
        AND ecoges_classe.supprimer='False'
        AND ecoges_inscription.supprimer='False'
        And ecoges_eleve.supprimer='False'
        AND  ecoges_eleve.genre='Masculin' ''')
    masculin=cursor.fetchone()

    cursor.execute(''' SELECT count(ecoges_eleve.matricule)
        FROM ecoges_inscription , ecoges_classe, ecoges_eleve, ecoges_anneescolaire
        WHERE ecoges_eleve.matricule=ecoges_inscription.matricule_id
        AND ecoges_inscription."idClasse_id"=ecoges_classe."idClasse"
        AND ecoges_anneescolaire."idAnneeScolaire"=ecoges_inscription."idAnneeScolaire_id"
        And ecoges_anneescolaire.etat='True'
        And ecoges_anneescolaire.supprimer='False'
        AND ecoges_classe.supprimer='False'
        AND ecoges_inscription.supprimer='False'
        And ecoges_eleve.supprimer='False'
        AND  ecoges_eleve.genre='Feminin' ''')
    feminin=cursor.fetchone()

    cursor.execute(''' SELECT count(ecoges_eleve.matricule)
        FROM ecoges_inscription , ecoges_classe, ecoges_eleve, ecoges_anneescolaire
        WHERE ecoges_eleve.matricule=ecoges_inscription.matricule_id
        AND ecoges_inscription."idClasse_id"=ecoges_classe."idClasse"
        AND ecoges_anneescolaire."idAnneeScolaire"=ecoges_inscription."idAnneeScolaire_id"
        And ecoges_anneescolaire.etat='True'
        And ecoges_anneescolaire.supprimer='False'
        AND ecoges_classe.supprimer='False'
        AND ecoges_inscription.supprimer='False'
        And ecoges_eleve.supprimer='False'
         ''')
    total=cursor.fetchone()
    context={'user':request.user,
    'masculin':masculin[0],'feminin':feminin[0],'total':total[0],
    'activeAnneeScolaire':AnneeScolaire.objects.filter(etat=True,supprimer=False).first()}
    return render(request,'ecoges/templates/Teacher-view/dashboard.html',context)

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleEnseignant(login_url='sing_in')
def trimestre1(request):
    context={'user':request.user,'activeAnneeScolaire':AnneeScolaire.objects.filter(etat=True,supprimer=False).first()}
    return render(request,'ecoges/templates/Teacher-view/trimestre1.html',context)

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleEnseignant(login_url='sing_in')
def trimestre2(request):
    context={'user':request.user,'activeAnneeScolaire':AnneeScolaire.objects.filter(etat=True,supprimer=False).first()}
    return render(request,'ecoges/templates/Teacher-view/trimestre2.html',context)

@login_required(login_url='sing_in')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@roleEnseignant(login_url='sing_in')
def trimestre3(request):
    context={'user':request.user,'activeAnneeScolaire':AnneeScolaire.objects.filter(etat=True,supprimer=False).first()}
    return render(request,'ecoges/templates/Teacher-view/trimestre3.html',context)



def sing_in(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.filter(email=email).first()
        if user is not None:
            #print( user.username +" "+ user.email)
            
            authUser=authenticate(username=user.username,password=password)
            print(authUser)
            if authUser is not None:
                print("trouveer")
                login(request,authUser)
                if request.user.role =='Directeur':
                    return redirect('dashboardD')
                elif request.user.role == 'Secretaire':
                    return redirect('dashboardS')
                elif request.user.role == 'Admin':
                    return redirect('dashboardA')
            else:
                print("mot de passe incorect")
                return redirect('sing_in')
        else:
            print("user existe pas")
            return redirect('sing_in')
    return render(request ,'ecoges/templates/registration/logIn.html',{})


def log_out(request):
    logout(request)
    return redirect('sing_in')


def createAdmin():
    user=User.objects.filter(is_superuser=True,is_staff=True)
    if user is None:
        user=User(first_name="ecoges",last_name="ecoges",username="Admin",is_superuser=True,is_staff=True,email="ecogesadmin@gmail.com", password="senateur", date_joined=datetime.now())
        user.save()
    

createAdmin()