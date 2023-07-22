from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.db import models

# Other custom functions
# function to set default array 
def get_default_array():
    return []

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=50, default="")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, default="")
    auth_token = models.CharField(max_length=150)
    pass_token = models.CharField(max_length=150, default="")
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

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
    
class ShortAppointment(models.Model):
    name=models.CharField(max_length=60)
    email=models.EmailField(max_length=255)
    phone_no=models.IntegerField()
    date=models.DateField()
    department=models.TextField()
    doctor=models.TextField()
    message=models.CharField(max_length=250)

class Appointment(models.Model):
    type_of_therapy = models.CharField(max_length=50, default='')
    sex = models.CharField(max_length=50, default='')
    age = models.IntegerField(default=18)
    gender = models.CharField(max_length=50, default='')
    relationship_status = models.CharField(max_length=50, default='')
    is_religious = models.BooleanField(default=False)
    religious_status = models.CharField(max_length=50, default='')
    is_spritual = models.BooleanField(default=False)
    taken_therapy = models.BooleanField(default=False)
    therapy_reason = ArrayField(base_field=models.TextField(), default=get_default_array)
    expectations = ArrayField(base_field=models.TextField(), default=get_default_array)
    is_anxious = models.BooleanField(default=False)
    taking_medications = models.BooleanField(default=False)
    having_chronic_pain = models.BooleanField(default=False)
    financial_status = models.CharField(max_length=50, default='')
    resources = ArrayField(base_field=models.TextField(), default=get_default_array)
    communication_mode = models.CharField(max_length=50, default='')
    preferences = models.CharField(max_length=50, default='')
    country = models.CharField(max_length=50, default='')
    language = models.CharField(max_length=50, default='')
    mark_that_apply = ArrayField(base_field=models.TextField(), default=get_default_array)


class Appointment2(models.Model):
    counseller_experience = ArrayField(base_field=models.TextField(), default=get_default_array)
    Additional_focus_areas = ArrayField(base_field=models.TextField(), default=get_default_array)
    additional_details = models.TextField(default="")



