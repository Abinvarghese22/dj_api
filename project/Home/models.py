from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Employee(models.Model):
    empname=models.CharField(max_length=50)
    phone=models.BigIntegerField()
    email=models.EmailField()
    date=models.DateField(null=True)

class Emp(models.Model):
    empname=models.CharField(max_length=50)
    phone=models.BigIntegerField()
    email=models.EmailField()
    date=models.DateField(null=True) 
    class Meta:
        db_table='tblemp'

class User(AbstractUser):
    phone=models.BigIntegerField(null=True)
    address=models.CharField(max_length=100,null=True)

class Student(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    age=models.IntegerField()

    def __str__(self):
        return self.name
    
class StudentProfile(models.Model):
    course=models.CharField(max_length=20)
    duration=models.CharField(max_length=20)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class Document(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/',null=True,blank=True)
    pdf=models.FileField(upload_to='pdfs/',null=True,blank=True)