from contact_list.views import contact_list
from django.urls import path


urlpatterns = [
    path('', contact_list, name='contact_list'),
]