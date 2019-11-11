from django.db import models


class Chat(models.Model):
    title = models.CharField(max_length=128, blank=False)
    is_group_chat = models.BooleanField()
    last_message = models.TextField()

    def __str__(self):
        return 'Chat id: ' + self.chat_id
