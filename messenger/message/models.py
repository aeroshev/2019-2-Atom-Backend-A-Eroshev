from django.db import models
from chats.models import Chat
from users.models import User


def user_directory_path(instance, filename):
    return 'user_{0}/attachment/{1}'.format(instance.user.id, filename)


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField('Text of message', null=True, blank=True, default='')
    added_at = models.DateTimeField('Time published', null=False, blank=False, auto_now_add=True)

    class Meta:
        ordering = ('-added_at',)

    def __str__(self):
        return 'id ' + str(self.id)

    def to_json(self):
        return {
            'chat_id': self.chat.id,
            'user_username': self.user.username,
            'text': self.text,
            'added_at': self.added_at
        }


class Attachment(models.Model):
    TYPE_ATTACH = (
        ('I', 'IMAGE'),
        ('D', 'DOCUMENT'),
        ('A', 'AUDIO')
    )
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField('Type attachment', max_length=1, choices=TYPE_ATTACH, null=False, blank=False, default='D')
    file = models.FileField(upload_to=user_directory_path, max_length=(10 * 1024 * 1024), null=True)
    image = models.ImageField(upload_to=user_directory_path, max_length=(5 * 1024 * 1024), null=True)
    audio = models.FileField(upload_to=user_directory_path, max_length=(5 * 1024 * 1024), null=True)

    def __str__(self):
        return 'id ' + str(self.id)

    def to_json(self):
        return {
            'message_id': self.message.id,
            'chat_id': self.chat.id,
            'user_username': self.user.username,
            'attachment type': self.type,
            'attachment file': self.file,
            'attachment image': self.image,
            'attachment audio': self.audio
        }
