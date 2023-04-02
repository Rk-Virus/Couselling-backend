from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField
    user_name = models.CharField(max_length=50, default="")
    user_dob = models.DateField()
    profile_img = models.ImageField(upload_to="home/images")

    def __str__(self):
        return self.user_name