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


class Attachment(models.Model):
    TYPE_ATTACH = (
        ('I', 'IMAGE'),
        ('F', 'FILE')
    )
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    type = models.CharField('Type attachment', max_length=1, choices=TYPE_ATTACH, blank=False)
    url = models.URLField('URL', blank=False)

    def __str__(self):
        return 'id ' + str(self.id)
