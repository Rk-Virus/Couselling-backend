from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField
    user_name = models.CharField(max_length=50)
    reg_date = models.DateField