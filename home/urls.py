from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("signup", views.signup, name='signup'),
    path("submission", views.submission, name='submission'),
]
