from django.db import models


class Member(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    chat = models.ManyToManyField('Chat')
    # new_messages = ?
    last_read_message = models.OneToOneField('Message', on_delete=models.CASCADE)
