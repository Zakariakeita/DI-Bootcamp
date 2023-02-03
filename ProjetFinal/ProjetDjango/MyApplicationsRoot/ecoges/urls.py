from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('printpdfView/<int:id>', views.printpdfView, name='printpdfView'),

    #URL de la vue de l'admin
    path('dashboardA', views.dashboardA, name='dashboardA'),
    path('', views.sing_in, name='sing_in'),
    path('logOut', views.log_out, name='logout'),
    path('saveProfilA', views.saveProfilA, name='saveProfilA'),
    path('updateProfilA/<int:id>', views.updateProfilA, name='updateProfilA'),
    path('deleteProfilA/<int:id>', views.deleteProfilA, name='deleteProfilA'),

    #Url de la vue du directeur
    path('dashboardD', views.dashboardD, name='dashboardD'),
    path('saveAnneeScolaire', views.saveAnneeScolaire, name='saveAnneeScolaire'),
    path('updateAnneeScolaire/<int:id>', views.updateAnneeScolaire, name='updateAnneeScolaire'),
    path('deleteAnneeScolaire/<int:id>', views.deleteAnneeScolaire, name='deleteAnneeScolaire'),
    path('activateAnneeScolaire', views.activateAnneeScolaire, name='activateAnneeScolaire'),
    path('profilD', views.profilD, name='profilD'),
    path('saveProfilD', views.saveProfilD, name='saveProfilD'),
    path('updateProfilD/<int:id>', views.updateProfilD, name='updateProfilD'),
    path('deleteProfilD/<int:id>', views.deleteProfilD, name='deleteProfilD'),
    path('depense', views.depense, name='depense'),
    path('configurationD', views.configurationD, name='configurationD'),
    path('attribClasseMatiere/<int:id>', views.attribClasseMatiere, name='attribClasseMatiere'),
    path('attribClasseMatiereToEnseignant/<int:id>', views.attribClasseMatiereToEnseignant, name='attribClasseMatiereToEnseignant'),
    path('updateCoefficient/<int:id>/<int:id2>', views.updateCoefficient, name='updateCoefficient'),
    path('deleteEnseignantClasseMatiere/<int:id>/<int:id2>', views.deleteEnseignantClasseMatiere, name='deleteEnseignantClasseMatiere'),
    path('chercherClasseMatiere', views.chercherClasseMatiere, name='chercherClasseMatiere'),


    #URL de la vvue du secretaire
    path('dashboardS', views.dashboardS, name='dashboardS'),
    path('eleve', views.eleve, name='eleve'),
    path('updateEleve/<int:id>', views.updateEleve, name='updateEleve'),
    path('saveEleve', views.saveEleve, name='saveEleve'),
    path('deleteEleve/<int:id>', views.deleteEleve, name='deleteEleve'),
    path('contentEleve/<int:id>', views.contentEleve, name='contentEleve'),

    path('inscription', views.inscription, name='inscription'),
    path('inscriptionEleve/<int:id>', views.inscriptionEleve, name='inscriptionEleve'),
    path('updateEleveIns/<int:id>', views.updateEleveIns, name='updateEleveIns'),
    path('saveEleveIns', views.saveEleveIns, name='saveEleveIns'),
    path('deleteEleveIns/<int:id>', views.deleteEleveIns, name='deleteEleveIns'),
    
    path('classe', views.classe, name='classe'),
    path('saveClasse', views.saveClasse, name='saveClasse'),
    path('updateClasse/<int:id>', views.updateClasse, name='updateClasse'),
    path('deleteClasse/<int:id>', views.deleteClasse, name='deleteClasse'),
    
    path('chercherClasseEnseignant', views.chercherClasseEnseignant, name='chercherClasseEnseignant'),

    path('classeContent/<int:id>', views.classeContent, name='classeContent'),
    path('deleteEleveFromClasse/<int:id1>/<int:id>', views.deleteEleveFromClasse, name='deleteEleveFromClasse'),
    path('updateEleveFromClasse/<int:id1>/<int:id>', views.updateEleveFromClasse, name='updateEleveFromClasse'),
    path('classeContentEleve/<int:id>/<int:id1>', views.classeContentEleve, name='classeContentEleve'),
    path('inscriptionContentClasse/<int:id>', views.inscriptionContentClasse, name='inscriptionContentClasse'),

    path('matiere', views.matiere, name='matiere'),
    path('saveMatiere', views.saveMatiere, name='saveMatiere'),
    path('updateMatiere/<int:id>', views.updateMatiere, name='updateMatiere'),
    path('deleteMatiere/<int:id>', views.deleteMatiere, name='deleteMatiere'),
    path('chercherMatiereEnseignant', views.chercherMatiereEnseignant, name='chercherMatiereEnseignant'),


    path('enseignant', views.enseignant, name='enseignant'),
    path('saveEnseignant', views.saveEnseignant, name='saveEnseignant'),
    path('updateEnseignant/<int:id>', views.updateEnseignant, name='updateEnseignant'),
    path('deleteEnseignant/<int:id>', views.deleteEnseignant, name='deleteEnseignant'),
    path('createUser', views.createUser, name='createUser'),
    path('attrMatiere/<int:id>', views.attrMatiere, name='attrMatiere'),

    path('enseignantContent/<int:id>', views.enseignantContent, name='enseignantContent'),
    path('attrMatiereFromEnseignant/<int:id>', views.attrMatiereFromEnseignant, name='attrMatiereFromEnseignant'),
    path('updAttrMatiereFromEnseignant/<int:id>', views.updAttrMatiereFromEnseignant, name='updAttrMatiereFromEnseignant'),

    #URL de la vue de l'enseignant
    path('dashboardP', views.dashboardP, name='dashboardP'),
    path('trimestre1', views.trimestre1, name='trimestre1'),
    path('trimestre2', views.trimestre2, name='trimestre2'),
    path('trimestre3', views.trimestre3, name='trimestre3'),

    #genration de pdf
    #path('pdfEleveInClasse/<int:id>', views.pdfEleveInClasse, name='pdfEleveInClasse'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)