from django.urls import path

from chat.views import ChatSelectionView, RoomView

app_name = "chat"
urlpatterns = [
    path('', ChatSelectionView.as_view(), name='index'),
    path("<str:room_name>/", RoomView.as_view(), name="room"),
]