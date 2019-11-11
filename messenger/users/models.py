from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=64)
    nick = models.CharField(max_length=128, blank=False)
    avatar = models.FilePathField()
    date_of_birthday = models.DateField()

    def __str__(self):
        return 'User: ' + self.nick
