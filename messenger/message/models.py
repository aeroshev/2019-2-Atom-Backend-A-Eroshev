from django.db import models
from chats.models import Chat
from users.models import User


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField('Text of message', null=True, blank=True, default='')
    added_at = models.DateTimeField('Time published', null=False, blank=False, auto_now_add=True)

    class Meta:
        ordering = ('-added_at',)

    def __str__(self):
        return 'id ' + str(self.id)


class Attachment(models.Model):
    TYPE_ATTACH = (
        ('I', 'IMAGE'),
        ('D', 'DOCUMENT')
    )
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    type = models.CharField('Type attachment', max_length=1, choices=TYPE_ATTACH, null=False, blank=False, default='D')
    url = models.URLField('URL', null=False, blank=False)

    def __str__(self):
        return 'id ' + str(self.id)
