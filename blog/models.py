from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250, default="")
    slug=models.SlugField(max_length=260, default="")
    sub_title = models.CharField(max_length=250, default="")
    category = models.CharField(max_length=250, default="")
    blog_img = models.ImageField(upload_to="blog/images")
    content = models.TextField()
    pub_date = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        to_assign=slugify(self.title)
        if Blog.objects.filter(slug=to_assign).exists():
            to_assign= to_assign+str(Blog.objects.all().count())
        self.slug=to_assign

        super().save(*args, **kwargs)

# class counsel(models.Model):
#     client_name= models.CharField(max_length=60)
#     date_requested= models.DateField()

# class therapist(models.Models):
#     th_name= models.CharField(max_length=80)

# class  appointment(models.Models):
#     client=models.TextField()
#     therapist=models.CharField(max_length=100)
#     starting=models.DateTimeField()
#     ending=models.DateTimeField()


