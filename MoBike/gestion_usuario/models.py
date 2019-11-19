from django.db import models
from django.contrib.auth.models import User


class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto_perfil = models.ImageField(upload_to='foto_perfil', blank=True)

