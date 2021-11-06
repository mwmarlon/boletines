from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class Indicadores(AbstractBaseUser):
    codigo = models.CharField(4)
    area = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=120)

    class Meta:
        verbose_name = "Indicador"
        verbose_name_plural = "Indicadores"
