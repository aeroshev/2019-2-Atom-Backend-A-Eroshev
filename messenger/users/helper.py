

def to_json(user):
    return {
        'last_login': user.last_login,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'is_active': user.is_active,
        'avatar': user.avatar,
        'date_of_birthday': user.date_of_birthday,
    }
