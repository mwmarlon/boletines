from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class Indicadores(LoginRequiredMixin, TimeStampedModel):
    codigo = models.CharField(max_length=4)
    area = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=120)

    class Meta:
        verbose_name = "Indicador"
        verbose_name_plural = "Indicadores"

    def __str__(self):
        return self.codigo


