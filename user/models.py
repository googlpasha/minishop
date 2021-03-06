from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager



class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['id', 'username', 'city', 'date_of_birth', 'spouse_name']

    objects = CustomUserManager()

    username = models.CharField(blank=True, max_length=100)
    city = models.CharField(max_length=50, blank=True, default='')
    spouse_name = models.CharField(blank=True, max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    

    def __str__(self):
        return self.email
