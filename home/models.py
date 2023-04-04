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
    email = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.name