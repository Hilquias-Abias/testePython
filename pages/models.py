from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=50)
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    cep = models.IntegerField
    address = models.CharField(max_length=30)
    number = models.IntegerField
    complement = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
