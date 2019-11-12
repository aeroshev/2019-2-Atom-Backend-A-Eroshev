from django.db import models


class User(models.Model):
    first_name = models.CharField('First name', max_length=32, null=True)
    last_name = models.CharField('Second name', max_length=64, null=True)
    nick = models.CharField('Nickname', max_length=128, blank=False)
    avatar = models.FilePathField('Path to avatar')
    date_of_birthday = models.DateField('Date of birthday', null=True)

    def __str__(self):
        return self.nick
