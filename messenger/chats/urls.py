from chats.views import chat_list
from django.urls import path, include


urlpatterns = [
    path('', chat_list, name='chat_list'),
    path('message/', include('message.urls')),
]
