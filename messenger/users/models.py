from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.FilePathField('Avatar of user', null=True, blank=False, default='default.png')
    date_of_birthday = models.DateField('Date of birthday', null=True, blank=False)

    def __str__(self):
        return self.username
