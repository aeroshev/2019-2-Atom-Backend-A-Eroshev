from stickers.views import get_sticker
from django.urls import path


urlpatterns = [
    path('<int:sticker_id>/', get_sticker, name='get_sticker'),
]
