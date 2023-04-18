"""URL mappings for the user API."""
# Django Libraries
from django.urls import path

# Project Libraries
from chat.views import all_rooms, room_detail, token


app_name = "chat"

urlpatterns = [
    path(r"^$", all_rooms, name="all_rooms"),
    path(r"token$", token, name="token"),
    path(r"rooms/(?P<slug>[-\w]+)/$", room_detail, name="room_detail"),
]
