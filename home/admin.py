from django.contrib import admin
from .models import Profile,Contact, ShortAppointment, Appointment, Appointment2

#Altering admin panels
class ProfileModalAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields=('name','email')
    list_per_page=10

class ContactModalAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields=('name','email')
    list_per_page=10

# Register your models here.
admin.site.register(Profile, ProfileModalAdmin)
admin.site.register(Contact, ContactModalAdmin)
admin.site.register(ShortAppointment)
admin.site.register(Appointment)
admin.site.register(Appointment2)
