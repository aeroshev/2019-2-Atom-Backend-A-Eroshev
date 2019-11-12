from django.db import models
from chats.models import Chat
from users.models import User


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField('Text of message')
    added_at = models.DateTimeField('Time published')

    def __str__(self):
        return 'id ' + str(self.id)
