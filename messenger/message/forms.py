from django import forms
from .models import Message, Attachment
from chats.models import Member


class MessageForm(forms.Form):
    chat_id = forms.IntegerField(label='Chat id', required=True)

    def cleaned_chat_id(self):
        clear_chat_id = self.cleaned_data['chat_id']

        if clear_chat_id < 1:
            self.add_error('chat_id', "id can't be lower 1")

        return clear_chat_id


class AddMessageForm(MessageForm):
    text = forms.CharField(label='Text', required=False)
    attachment_type = forms.CharField(label='Type attachment', max_length=1, required=False)
    url = forms.FileField(label='Path to attachment', required=False)

    def __init__(self, get, file, user):
        super().__init__(get, file)
        self.user = user

    def clean_attachment_type(self):
        attachment_type = self.cleaned_data['attachment_type']

        if len(attachment_type) > 1:
            self.add_error('attachment_type', 'type must contain 1 symbol')

    def save(self):
        data = self.cleaned_data
        user = data.user
        chat = data.chat
        text = data.text
        attachment_type = data.attachment_type
        url = data.url

        message = Message.objects.create(chat=chat, user=user, text=text)

        Attachment.objects.create(message=message, type=attachment_type, url=url)

        return message


class ReadMessageForm(MessageForm):
    message_id = forms.IntegerField(label='Message id')

    def __init__(self, get, user):
        super().__init(self, get)
        self.user = user

    def cleaned_message_id(self):
        clear_message_id = self.cleaned_data['message_id']

        if clear_message_id < 1:
            self.add_error('message_id', "id can't be lower 1")

        return clear_message_id

    def save(self):
        status = False

        data = self.cleaned_data
        message_id = data['message_id']
        chat_id = data['chat']
        reader = self.user

        read_message = None
        try:
            read_message = Message.objects.get(id=message_id)
        except Message.DoesNotExist:
            status = False

        if read_message:
            try:
                member = Member.objects.get(user=reader, chat=chat_id)
                member.update(last_read_message=message_id)

                status = True
            except Member.DoesNotExist:
                status = False

        return status
