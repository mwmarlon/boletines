from django.db import models
#importe de AbstractBaseUser
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    GENERO = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otros')
    )

    CARGO = (
        ('Administrador', 'Administrador'),
        ('Directivo', 'Directivo'),
        ('Docente', 'Docente'),
    )

    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    nombres = models.CharField(max_length=30, blank=True)
    apellidos = models.CharField(max_length=30, blank=True)
    genero = models.CharField(max_length=1, choices=GENERO, blank=True)
    cargo = models.CharField(max_length=15, choices=CARGO, blank=True)
    direccion = models.CharField(max_length=50, blank=True)
    telefono = models.CharField(max_length=15, blank=True)
    #
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email',]

    objects = UserManager()

    def get_short_name(self):
        return self.username
    
    def get_full_name(self):
        return "{} {}".format(self.nombres,self.apellidos)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"




