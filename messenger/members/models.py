from django.db import models


class Member(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    chat = models.ManyToManyField('chats.Chat')
    # new_messages = ?
    last_read_message = models.OneToOneField('message.Message', on_delete=models.CASCADE)
