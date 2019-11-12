from members.views import get_member
from django.urls import path


urlpatterns = [
    path('', get_member, name='get_member')
]