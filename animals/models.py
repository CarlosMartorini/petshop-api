from django.db import models

from characteristics.models import Characteristic


class Animal(models.Model):
    name = models.CharField(max_length=255)
    age = models.FloatField()
    weight = models.FloatField()
    sex = models.CharField(max_length=10)
    
    group = models.ForeignKey('groups.Group', on_delete=models.CASCADE, related_name='animals')
