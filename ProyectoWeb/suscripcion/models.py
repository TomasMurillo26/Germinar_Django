from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

User= get_user_model()

# Create your models here.
class Membresia(models.Model):
    TIPO_MEMBRESIA = (
        ('Gratis', 'free'),
        ('Germinar', 'ger')
    )

    slug = models.SlugField()
    tipoMembresia = models.CharField(choices=TIPO_MEMBRESIA, max_length=30, default='Gratis')
    precioMemebresia = models.IntegerField(default=3000)

    def __str__(self):
        return self.tipoMembresia

class UserMembresia(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tipoMembresia = models.ForeignKey(Membresia, on_delete=models.SET_NULL,  default='Gratis', null=True)

    def __str__(self):
        return self.user.username

def post_save_usermembresia_create(sender, instance, created, *args, **kwargs):
    if created:
        UserMembresia.objects.get_or_create(user=instance)

    userMembresia, created = UserMembresia.objects.get_or_create(user=instance)

post_save.connect(post_save_usermembresia_create, sender=User)

class Suscripcion(models.Model):
    userMembresia = models.ForeignKey(UserMembresia, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.userMembresia.user.username