from django.db import models
from users.models import User


class Chat(models.Model):
    title = models.CharField('Title chat', max_length=128, null=False, blank=False, default='NoName')
    is_group_chat = models.BooleanField('Group chat', null=False, blank=False, default=False)
    chat_avatar = models.ImageField('Avatar of chat', null=False, blank=False, default='default.png')
    last_message = models.OneToOneField('message.Message', on_delete=models.SET_NULL, null=True, related_name='Chat')
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return 'title ' + self.title

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'is_group_chat': self.is_group_chat,
            'chat_avatar': str(self.chat_avatar),
            'creator': self.creator,
        }


class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    last_read_message = models.ForeignKey('message.Message', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return 'user ' + self.user.username + ' in chat ' + self.chat.title

