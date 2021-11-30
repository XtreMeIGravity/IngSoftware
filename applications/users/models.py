from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    Gender_Choices = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otros'),
    )
    username = models.CharField(unique=True, max_length=50)
    email = models.EmailField()
    name = models.CharField(max_length=50, blank=True)
    lastname = models.CharField(max_length=50, blank=True)
    gender = models.CharField(choices=Gender_Choices, max_length=50, blank=True)
    date_of_birth = models.DateField(default="1998-09-15", blank=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    objects = UserManager()

    REQUIRED_FIELDS = ['email', ]

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.nombres + " " + self.apellidos
