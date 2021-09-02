from django.db import models
from django.contrib.auth.models import BaseUserManager


#
class PublicacionManager(BaseUserManager, models.Manager):
    def createPublicacion(self, username, email, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username=username,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user