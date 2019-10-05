from django.db import models

# Create your models here.


class Entreprise(models.Model):
    nom = models.CharField(max_length=500,unique=True)
    adresse = models.CharField(max_length=550)
    telephone = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return "{} {} ".format(self.nom  ,self.created)

class Departement(models.Model):
    nom = models.CharField(max_length=500,unique=True)
    #chefUser = models.ForeignKey(, on_delete=models.CASCADE,)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return "{} {}".format(self.nom  ,self.created)

class ListNumero(models.Model):
    numero = models.CharField(max_length=500,unique=True)
    # idUser = models.IntegerField(null=True,blank=True)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    departement = models.ForeignKey(Departement,on_delete=models.CASCADE)
    level = models.IntegerField()
    code = models.CharField(max_length=50,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return "{} {}".format(self.numero , self.created)

class Personnel(models.Model):
    user = models.OneToOneField(ListNumero,on_delete=models.CASCADE,primary_key=True)
    nom = models.TextField()
    prenom = models.TextField()
    prostnom = models.TextField(null=True,blank=True,default="")
    telephone2 = models.TextField(null=True,blank=True ,default="")
    adresse = models.TextField(null=True,blank=True ,default="")
    description = models.TextField(null=True,blank=True ,default="")
    email = models.EmailField()
    password = models.TextField()
    isActive = models.BooleanField(default=True)
    imageUrl = models.ImageField(upload_to="upload/personnel",null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return "{} {} {} {} ".format(self.nom, self.prenom, self.telephone2 ,self.created)

class News(models.Model):
    user = models.ForeignKey(Personnel,on_delete=models.CASCADE)
    titre = models.TextField()
    contenu = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
    def __str__(self):
        return "{} {} {} ".format(self.titre, self.contenu, self.created)







