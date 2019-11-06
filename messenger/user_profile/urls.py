from user_profile.views import profile
from django.urls import path


urlpatterns = [
    path('', profile, name='profile'),
]