from django.db import models
from django.contrib.auth.models import User
from .constant import USER_TYPES

class User_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=15, blank=True, null=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='Subscriber')
