from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='index'),
    path("contact", views.contact, name='contact'),
    path("signup", views.signup, name='signup'),
    path("login", views.login, name='login'),
    path("logout", views.logout, name='logout'),
    path("appointment", views.appointment, name='appointment'),
    path("appointment2", views.appointment2, name='appointment2'),
    path("verify/<email>", views.verify, name='verify'),
    path("verifyemail/<token>", views.verifyemail, name='verifyemail'),
]
