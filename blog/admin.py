from django.contrib import admin
from .models import Blog

class BlogModalAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'pub_date')
    search_fields=('title','sub_title')
    list_per_page=10

# Register your models here.
admin.site.register(Blog, BlogModalAdmin)
