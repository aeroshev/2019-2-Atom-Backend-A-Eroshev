from django.db import models


class Chat(models.Model):
	title = models.CharFIled(mex_length=128, blank=False)
	chat = models.ForeignKey(Sticker, on_delete=models.SET_NULL, null=True, related_name='chats') 
