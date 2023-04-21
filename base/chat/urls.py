"""URL mappings for the user API."""
# Django Libraries
from django.urls import path, re_path

# Project Libraries
from chat.views import AllRoomsView, RoomDetailsView, TwilioTokenView


app_name = "chat"

urlpatterns = [
    path("", AllRoomsView.as_view(), name="all_rooms"),
    path("token", TwilioTokenView.as_view(), name="token"),
    re_path(r"rooms/(?P<slug>[-\w]+)/$", RoomDetailsView.as_view(), name="room_detail"),
]
