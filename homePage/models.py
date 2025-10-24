from django.db import models

# Create your models here.

class credentialsModel(models.Model):
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    pno = models.IntegerField()
    dob = models.DateField()
    password = models.CharField()
    confirm_password = models.CharField(max_length=30)


