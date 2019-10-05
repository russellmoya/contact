from django.contrib import admin
from .models import Personnel,News,ListNumero,Entreprise,Departement
# Register your models here.
admin.register(Personnel,News,Entreprise,Departement,ListNumero)