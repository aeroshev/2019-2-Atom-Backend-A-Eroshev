from django.db import models
from users.models import User


class Chat(models.Model):
    title = models.CharField('Title chat', max_length=128, null=False, blank=False, default='NoName')
    is_group_chat = models.BooleanField('Group chat', null=False, blank=False, default=False)
    chat_avatar = models.FileField('Avatar of chat', null=False, blank=False, default='default.png')
    last_message = models.IntegerField('Id last message', null=True, blank=False)
    # creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return 'id ' + str(self.id)


class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    # new_message = models.IntegerField('Id of new message', null=True, blank=True, default='')
    last_read_message = models.IntegerField('Id last read message', null=True, blank=False)

    def __str__(self):
        return 'member ' + self.user

