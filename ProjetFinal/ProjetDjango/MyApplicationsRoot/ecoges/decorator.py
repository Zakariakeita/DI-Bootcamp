from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
def roleDirecteur(login_url=None):
    return user_passes_test(lambda u: u.role in ('Directeur','Admin'),login_url=login_url)

def roleSecretaire(login_url=None):
    return user_passes_test(lambda u:u.role in ('Secretaire','Admin'),login_url=login_url)


def roleDirecteurSecretaire(login_url=None):
    return user_passes_test(lambda u: u.role in ('Secretaire','Directeur','Admin'),login_url=login_url)

def roleAdmin(login_url=None):
    return user_passes_test(lambda u: u.role=='Admin',login_url=login_url)

def roleCaissier(login_url=None):
    return user_passes_test(lambda u: u.role in ('Caissier','Admin') ,login_url=login_url)

def roleCaissierDirecteur(login_url=None):
    return user_passes_test(lambda u: u.role in ('Caissier','Directeur','Admin') ,login_url=login_url)

def roleEnseignant(login_url=None):
    return user_passes_test(lambda u: u.role in ('Enseignant','Admin'),login_url=login_url)