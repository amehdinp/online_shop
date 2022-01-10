from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import MyUserManager


class User (AbstractUser):
    email = models.EmailField(max_length=100,  unique=True)
    fullname = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname']
    objects = MyUserManager()

    def __str__(self):
        return self.email

    def has_perms(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_superuser

