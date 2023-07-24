from django.db import models

# Create your models here.
class Userform(models.Model):
    username= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    Designation= models.CharField(max_length=100)
    DateofJoinning= models.DateField()
    Biometricid= models.CharField(max_length=100,primary_key=True)
    password= models.CharField(max_length=100)
    
class Regulation(models.Model):
    Sno= models.IntegerField()
    Regulation= models.CharField(max_length=100)
    startyear= models.IntegerField()
    endyear= models.IntegerField()
class Courses(models.Model):
    Sno= models.IntegerField()
    Coursenam= models.CharField(max_length=100)
    Coursecode= models.CharField(max_length=100)
    


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

    