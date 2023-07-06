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

class Counselor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    expertise = models.CharField(max_length=200)
    
    def _str_(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    
    def _str_(self):
        return self.name

class CounselingRequest(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    counselor = models.ForeignKey(Counselor, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def _str_(self):
        return f"{self.client} - {self.created_at}"

