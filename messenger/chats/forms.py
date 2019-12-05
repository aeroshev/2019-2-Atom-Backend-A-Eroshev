from django import forms
from chats.models import Chat, Member
from users.models import User


class ChatForm(forms.Form):
    title = forms.CharField(label='Chat title', max_length=128, required=True)
    is_group = forms.BooleanField(label='Group chat', required=False)
    avatar = forms.FileField(label='Chat avatar', required=False)
    # members = forms.ModelChoiceField(label='Members', required=False,

                                     #count <2 >20


    def __init__(self, get, user):
        super().__init__(get)
        self.user = user

    def clean_title(self):
        title = self.cleaned_data['title']
        if not title:
            self.add_error('title', "title can't be empty")
        return title

    def save(self):
        data = self.cleaned_data
        title = data['title']
        group = data['group']
        members = data['members']
        avatar = data['avatar']
        creator = self.user

        new_chat = Chat.objects.create(title=title, is_group_chat=group, chat_avatar=avatar, creator=creator)

        Member.objects.create(user=creator, chat=new_chat)
        for member in members:
            Member.objects.create(user=member, chat=new_chat)

        return new_chat
