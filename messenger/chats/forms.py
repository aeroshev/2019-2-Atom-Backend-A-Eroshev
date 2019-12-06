from django import forms
from chats.models import Chat, Member
from users.models import User


class ChatForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), to_field_name="username", required=True)
    title = forms.CharField(max_length=128, required=True)
    is_group = forms.BooleanField(required=False)
    avatar = forms.ImageField(required=False)
    members = forms.ModelMultipleChoiceField(queryset=User.objects.all(), to_field_name="username", required=True)

    def clean_title(self):
        title = self.cleaned_data['title']
        if not title:
            self.add_error('title', "title can't be empty")
        return title

    def clean_members(self):
        members = self.cleaned_data['members']
        user = self.cleaned_data['user']

        if not 1 < members.count() < 21:
            self.add_error('members', 'Quantity members must be in interval 2-20')
        if members.filter(username=user):
            self.add_erorr('members', 'You already have member')
        return members

    def save(self):
        data = self.cleaned_data
        title_ = data['title']
        group = data['is_group']
        members = data['members']
        avatar = data['avatar']
        creator = data['user']

        new_chat = Chat.objects.create(title=title_, is_group_chat=group, chat_avatar=avatar, creator=creator)

        Member.objects.create(user=creator, chat=new_chat)
        for member in members:
            Member.objects.create(user=member, chat=new_chat)

        return new_chat
