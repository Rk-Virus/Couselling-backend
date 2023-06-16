from django.urls import path
from blog import views

urlpatterns = [
    path("", views.index, name='blog'),
    #path("<str:slug>", views.blogPost, name='blogPost'),
    path("<int:id>", views.blogPost, name='blogPost'),

]
