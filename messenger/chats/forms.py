from django import forms
from chats.models import Chat, Member
from users.models import User


class ChatForm(forms.Form):
    # user = forms.ModelChoiceField(queryset=User.objects.all(), to_field_name='username', required=True)
    title = forms.CharField(max_length=128, required=True)
    is_group = forms.BooleanField(required=False)
    avatar = forms.ImageField(required=False)
    members = forms.ModelMultipleChoiceField(queryset=User.objects.all(), to_field_name='username', required=True)

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean_members(self):
        members = self.cleaned_data['members']
        # user = self.cleaned_data['user']
        user = self.user

        if not 0 < members.count() < 20:
            self.add_error('members', 'Quantity members must be in interval 2-20')
        if members.filter(username=user.username):
            self.add_error('members', 'You already have member')
        return members

    def clean(self):
        # user = self.cleaned_data['user']
        user = self.user
        title = self.cleaned_data['title']

        if Chat.objects.select_related('creator').filter(title=title, creator=user):
            self.add_error('title', 'This chat already exist')
        return self.cleaned_data

    def save(self):
        data = self.cleaned_data
        title = data['title']
        group = data['is_group']
        members = data['members']
        avatar = data['avatar']
        # creator = data['user']
        creator = self.user

        new_chat = Chat.objects.create(title=title, is_group_chat=group, chat_avatar=avatar, creator=creator)
        Member.objects.create(user=creator, chat=new_chat)
        for member in members:
            Member.objects.create(user=member, chat=new_chat)
        return new_chat
