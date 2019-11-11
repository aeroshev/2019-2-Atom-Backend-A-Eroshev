from django.db import models


class Chat(models.Model):
    title = models.CharField(mex_length=128, blank=False)
    is_group_chat = models.BoolenField()
    last_message = models.OneToOne('Message', on_delete=models.CASCADE)

    def __str__(self):
        return 'Chat id: ' + self.chat_id
