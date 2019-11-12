from message.views import get_message, get_attach
from django.urls import path


urlpatterns = [
    path('', get_attach, name='get_attach'),
    path('<int:message_id>/', get_message, name='get_message'),
]