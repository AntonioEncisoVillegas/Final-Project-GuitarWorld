from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import SET_NULL
from django.contrib.auth.models import User

# Create your models here.

class Brand(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Country(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    

class GuitarComercial(models.Model):
    name=models.CharField(max_length=30)
    model=models.CharField(max_length=30)
    description=models.TextField()
    features=models.TextField()
    score=models.PositiveIntegerField()
    image=models.ImageField(upload_to="guitarComercial/image/")
    video=models.CharField(max_length=255)
    brand=models.ForeignKey(Brand, on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return self.name + " " + str(self.id)

class GuitarHandMade(models.Model):
    name=models.CharField(max_length=30)
    model=models.CharField(max_length=30)
    description=models.TextField()
    features=models.TextField()
    score=models.PositiveIntegerField()
    image=models.ImageField(upload_to="guitarHandMade/image/")
    video=models.CharField(max_length=255)
    luthier=models.CharField(max_length=50)
    luthier_history=models.TextField()
    country=models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name + " " + str(self.id)
    
class PunctuationComercial(models.Model):
    rate=models.PositiveIntegerField()
    user=models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    guuitar=models.ForeignKey(GuitarComercial, on_delete=models.SET_NULL, blank=True, null=True)

class PunctuationHandMade(models.Model):
    rate=models.PositiveIntegerField()
    user=models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    guuitar=models.ForeignKey(GuitarHandMade, on_delete=models.SET_NULL, blank=True, null=True)