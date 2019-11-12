from chats.views import get_info
from django.urls import path, include


urlpatterns = [
    path('<int:chat_id>/', get_info, name='get_info')
]
