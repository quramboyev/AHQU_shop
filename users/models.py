from django.contrib.auth.models import AbstractUser
from django.db import models
from .validators import validate_uzbek_phone

class CustomUserModel(AbstractUser):
    phone_number = models.CharField(max_length=13, unique=True, validators=[validate_uzbek_phone])
    photo  = models.ImageField(upload_to='users/photos/', blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)