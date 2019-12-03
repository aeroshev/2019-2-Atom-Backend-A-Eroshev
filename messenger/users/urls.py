from users.views import get_profile, create_profile, search
from django.urls import path


urlpatterns = [
    path('<int:user_id>/', get_profile, name='get_profile'),
    path('', create_profile, name='create_profile'),
    path('search/', search, name='search')
]
