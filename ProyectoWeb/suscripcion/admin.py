from django.contrib import admin
from .models import UserMembresia,Membresia,Suscripcion
# Register your models here.
admin.site.register([UserMembresia,Membresia,Suscripcion])