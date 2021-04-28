from django.db import models
from input_mask.widgets import InputMask

class Users(models.Model):
    nome = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    cep = models.IntegerField
    address = models.CharField(max_length=30)
    number = models.IntegerField
    complement = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    

# class CpfMask(InputMask):
#     cep = {'cep': '99999-99'}


