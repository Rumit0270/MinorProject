from django.db import models
from django import forms
# Create your models here.

class Symptom(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        
class Disease(models.Model):
    disease_name = models.CharField(max_length=100)
    symptoms = models.ForeignKey(Symptom,on_delete=models.DO_NOTHING, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True)
    specialists = models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.disease_name

    def diseasename(naaaam):
        disease_name=naaaam


class Patient(models.Model):
    user_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    email = models.EmailField(max_length=100, null=True)
    password = models.CharField(max_length=100)
    possible_disease = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.user_name

class Doctor(models.Model):
    name = models.CharField(max_length=30)
    contact = models.CharField(max_length=10)
    specialization = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.name
