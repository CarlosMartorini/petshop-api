from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=255)
    age = models.FloatField()
    weight = models.FloatField()
    sex = models.CharField(max_length=10)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    characteristics = models.ManyToManyField('Characteristic', on_delete=models.CASCADE)


class Group(models.Model):
    name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255)


class Characteristic(models.Model):
    name = models.CharField(max_length=255)
