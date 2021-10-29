from django.db import models
from animals.models import Animal


class Characteristic(models.Model):
    name = models.CharField(max_length=255)

    animals = models.ManyToManyField(Animal, related_name='characteristics')
