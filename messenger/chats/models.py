from django.db import models
from users.models import User


class Chat(models.Model):
    title = models.CharField(max_length=128, blank=False)
    is_group_chat = models.BooleanField('Group chat', blank=False, default=False)
    last_message = models.TextField('Last message', null=True)

    def __str__(self):
        return 'id ' + str(self.id)


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    last_read_message = models.TextField('Last read message', null=True)

    def __str__(self):
        return 'member ' + self.user

