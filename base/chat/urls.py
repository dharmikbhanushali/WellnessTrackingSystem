"""URL mappings for the user API."""
# Django Libraries
from django.conf.urls import url

# Project Libraries
from chat.views import all_rooms, room_detail, token


app_name = "chat"

urlpatterns = [
    url(r"^$", all_rooms, name="all_rooms"),
    url(r"token$", token, name="token"),
    url(r"rooms/(?P<slug>[-\w]+)/$", room_detail, name="room_detail"),
]
