from django.db import models
from chats.models import Chat
from users.models import User
from message.models import Message


class Attachment(models.Model):
    TYPE_ATTACH = (
        ('I', 'IMAGE'),
        ('F', 'FILE')
    )
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    type = models.CharField('Type attachment', max_length=1, choices=TYPE_ATTACH, blank=False)
    url = models.URLField('URL', blank=False)

    def __str__(self):
        return 'id ' + str(self.id)
