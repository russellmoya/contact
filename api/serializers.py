from rest_framework import serializers
from .models import News,ListNumero,Personnel,Departement,Entreprise

class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id','user','titre','contenu','')


class ListNumeroSerializers(serializers.ModelSerializer):
    class Meta:
        model = ListNumero
        fields = ['id','numero','entreprise','departement','level','code']

class DepartementSerializers(serializers.ModelSerializer):
    class Meta:
        model = Departement
        fields = ('id','nom')

class EntrepriseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Entreprise
        fields = ('id','nom','adresse','telephone')



class PersonnelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        fields = ('user','nom','prenom','prostnom','telephone2','adresse','description ','email','password ','isActive','imageUrl')