from json import dumps


def to_json(chat, user=None):
    return dumps({
        'id': chat.id,
        'title': chat.title,
        'is_group_chat': chat.is_group_chat,
        'chat_avatar': str(chat.chat_avatar),
        'creator': chat.creator,
    }, ensure_ascii=False)

