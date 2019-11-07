from chats.views import chat_list
from django.urls import path, include


urlpatterns = [
    path('<int:chat_id>/', chat_list, name='chat_list'),
    path('<int:chat_id>/message/', include('message.urls')),
    path('<int:chat_id>/sticker/', include('stickers.urls'))
]
