from django.db import models
from users.models import User
from chats.models import Chat
from message.models import Message


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    chat = models.ManyToManyField(Chat)
    last_read_message = models.OneToOneField(Message, on_delete=models.CASCADE)

    def __str__(self):
        return 'member ' + self.user
