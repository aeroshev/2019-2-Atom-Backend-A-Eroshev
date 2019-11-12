from chats.views import get_info, chat_list
from django.urls import path, include


urlpatterns = [
    path('', chat_list, name='chat_list'),
    path('<int:chat_id>/', get_info, name='get_info')
]
