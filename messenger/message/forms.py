from django import forms
from .models import Message, Attachment
from chats.models import Member, Chat
from users.models import User


class MessageForm(forms.Form):
    chat = forms.ModelChoiceField(queryset=Chat.objects.all(), to_field_name='id', required=True)
    user = forms.ModelChoiceField(queryset=User.objects.all(), to_field_name='username', required=True)


class AddMessageForm(MessageForm):
    TYPE_ATTACH = (
        ('I', 'IMAGE'),
        ('D', 'DOCUMENT'),
        ('A', 'AUDIO')
    )
    text = forms.CharField(required=False)
    attachment_type = forms.ChoiceField(choices=TYPE_ATTACH, required=False)
    file = forms.FileField(required=False)
    image = forms.ImageField(required=False)
    audio = forms.FileField(required=False)

    def save(self):
        data = self.cleaned_data
        user = data['user']
        chat = data['chat']
        text = data['text']
        attachment_type = data['attachment_type']
        file = data['file']
        image = data['image']
        audio = data['audio']

        message = Message.objects.create(chat=chat, user=user, text=text)
        Attachment.objects.create(message=message, type=attachment_type, file=file, image=image, audio=audio)

        return message


class ReadMessageForm(MessageForm):
    message = forms.ModelChoiceField(queryset=Message.objects.all(), to_field_name='id', required=True)

    def cleaned_message(self):
        message = self.cleaned_data['message']
        chat = self.cleaned_data['chat']

        if message.chat != chat:
            self.add_erorr('message', 'This message are not contain in this chat')

    def save(self):
        data = self.cleaned_data
        message = data['message']
        chat = data['chat']
        reader = data['user']

        member = Member.objects.filter(user=reader, chat=chat)
        member.update(last_read_message=message)

        return member
