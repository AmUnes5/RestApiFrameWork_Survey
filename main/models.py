from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class etudiant(models.Model):
    sexe = models.CharField(max_length=10)
    age = models.IntegerField()
    nationalite = models.CharField(max_length=25)
    ville = models.CharField(max_length=25)
    universite = models.CharField(max_length=50)
    diplome = models.CharField(max_length=15)
    annee = models.IntegerField()
    activites = models.CharField(max_length=50)
    RateEnseignant = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    RateAdministratif = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    RateBDE = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    aspects = models.TextField(blank=True)
    autoformation = models.BooleanField()
    objectifs = models.BooleanField()
