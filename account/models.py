from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    email = models.EmailField('メールアドレス', unique=True)
    username = models.CharField('ユーザー名', max_length=255, unique=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    pass
