from chat_page.views import chat_page
from django.urls import path


urlpatterns = [
    path('', chat_page, name='chat_page'),
]