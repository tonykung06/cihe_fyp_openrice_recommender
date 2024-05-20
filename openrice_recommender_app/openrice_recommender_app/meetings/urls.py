from django.urls import path
from meetings.views import detail, home, new, new_room, room_detail, room_list

urlpatterns = [
    path("", home, name="home"),
    path("<int:id>", detail, name="detail"),
    path("rooms/<int:id>", room_detail, name="room_detail"),
    path("rooms", room_list, name="room_list"),
    path("rooms/new", new_room, name="new_room"),
    path("new", new, name="new"),
]
