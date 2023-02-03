from django.contrib import admin
from .models import * #import the Person model

# Register your models here.
admin.site.register(User)
admin.site.register(Eleve)
admin.site.register(Matiere)
admin.site.register(Classe)
admin.site.register(AnneeScolaire)
admin.site.register(Inscription)