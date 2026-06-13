from django.urls import path
from . import views



urlpatterns = [
    path("", views.room_view, name="rooms"),
    path("<str:room_name>/", views.chat_view, name="chat_room")
]
