from django.db import models


class Member(models.Model):
    user = models.OneToOne('User', on_delete=models.CASCADE)
    chat = models.ManyToMany('Chat')
    # new_messages = ?
    last_read_message = models.OneToOne('Message', on_delete=models.CASCADE)
