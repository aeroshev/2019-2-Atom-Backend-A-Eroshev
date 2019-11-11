from message.views import get_message
from django.urls import path


urlpatterns = [
    path('<int:message_id>/', get_message, name='get_message'),
]