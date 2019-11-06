from start_page.views import start
from django.urls import path


urlpatterns = [
    path('', start, name='start'),
]