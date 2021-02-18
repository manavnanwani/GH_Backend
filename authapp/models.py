from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(verbose_name='username', max_length=255, unique=True)
    REQUIRED_FIELDS = ['first_name','last_name','email','password']
    USERNAME_FIELD = 'username'
    def get_username(self): 
        return self.username
