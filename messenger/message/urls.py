from message.views import get_message
from django.urls import path, include


urlpatterns = [
    path('<int:message_id>/', get_message, name='get_message'),
    path('<int:message_id>/attachment/', include('attachment.urls'))
]