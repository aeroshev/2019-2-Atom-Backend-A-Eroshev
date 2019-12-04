from chats.models import Member
from .models import Message, Attachment


def to_json(message, attachments):
    attach_list = []
    for attachment in attachments:
        attach_list.append({
            'attachment_type': attachment.type,
            'attachment path': attachment.url
        })

    return {
        'text': message.text,
        'added_at': message.added_at,
        'attachments': attach_list
    }


def message_list(chat_id, user_id):
    member = None
    list_messages = list()

    try:
        member = Member.objects.get(user=user_id, chat=chat_id)
    except Member.DoesNotExist:
        pass

    if member:
        messages = None
        try:
            messages = list(Message.objects.filter(chat=chat_id))
        except Message.DoesNotExist:
            pass

        for message in messages:
            attachments = list(Attachment.objects.filter(message=message.id))

            list_messages.append(to_json(message, attachments))

    return list_messages



