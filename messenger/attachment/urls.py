from attachment.views import get_attach
from django.urls import path


urlpatterns = [
    path('', get_attach, name='get_attach')
]