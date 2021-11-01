from django.db import models

# Create your models here.

class Result(models.Model):
    #resultNum = models.AutoField()
    productName = models.CharField(max_length=100)
    productContent = models.TextField()
    allergyResult = models.TextField()
    create_date = models.DateTimeField()

class Allergy(models.Model):
    #allergyNum = models.IntegerField()
    highLevelAllergy = models.CharField(max_length=30)
    lowLevelAllergy = models.CharField(max_length=30)
    level = models.IntegerField()
    myAllergy = models.CharField(max_length=10)