from django.db import models


class Chat(models.Model):
    title = models.CharField(max_length=128, blank=False)
    is_group_chat = models.BooleanField('Group chat', blank=False)
    last_message = models.TextField('Last message', null=True)

    def __str__(self):
        return 'id ' + str(self.id)
