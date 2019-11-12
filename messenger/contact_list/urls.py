from contact_list.views import get_list
from django.urls import path, include


urlpatterns = [
    path('', get_list, name='get_list')
]
