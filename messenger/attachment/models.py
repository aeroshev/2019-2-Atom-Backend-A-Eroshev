from django.db import models


class Attachment(models.Model):
    TYPE_ATTACH = (
        ('I', 'IMAGE'),
        ('F', 'FILE')
    )
    chat = models.ForeignKey('chats.Chat', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    message = models.ForeignKey('message.Message', on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=TYPE_ATTACH, blank=False)
    url = models.URLField(blank=False)

    def __str__(self):
        return 'Attachment_id: ' + self.attachment_id
