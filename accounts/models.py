from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """Custom User model for better control on User database fields"""
    email = models.EmailField(unique=True)