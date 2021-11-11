from django.db import models

# Create your models here.


class Allergy(models.Model):
    allergyName = models.CharField(max_length=30)
    highLevelAllergy = models.CharField(blank= True, null=True, max_length=30)
    level = models.IntegerField()
    myAllergy = models.CharField(max_length=10)

class Result(models.Model):
    productName = models.CharField(max_length=100)
    productContent = models.TextField()
    allergyResult = models.TextField()
    create_date = models.TextField()