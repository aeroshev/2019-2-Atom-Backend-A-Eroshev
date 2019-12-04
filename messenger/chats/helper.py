

def to_json(chat):
    return {
        'id': chat.id,
        'title': chat.title,
        'is_group_chat': chat.is_group_chat,
        'chat_avatar': str(chat.chat_avatar),
        'creator': chat.creator,
    }

