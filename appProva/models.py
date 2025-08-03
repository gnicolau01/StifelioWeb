from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Usuari(models.Model):
    usuari = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    password = models.CharField(max_length=120)

    def __str__(self):
        return self.usuari.username


class Sabata(models.Model):
    nom = models.CharField(max_length=200)
    foto = models.ImageField()

    def __str__(self):
        return self.nom


class Review(models.Model):
    user = models.ForeignKey(Usuari, on_delete=models.CASCADE)
    producte = models.ForeignKey('Sabata', on_delete=models.SET_NULL, null=True)
    review = models.TextField()
    rating = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rating