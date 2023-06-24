from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=50, default="")
    dob = models.DateField()
    profile_img = models.ImageField(upload_to="home/images")

    def __str__(self):
        return self.name


class Contact(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50, default="")
    email = models.EmailField(max_length=254, default="")
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    name=models.CharField(max_length=60)
    email=models.EmailField(max_length=255)
    phone_no=models.IntegerField()
    date=models.DateField()
    department=models.TextField()
    doctor=models.TextField()
    message=models.CharField(max_length=250)