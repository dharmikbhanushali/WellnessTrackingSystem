# Django Libraries
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

# 3rd Party Libraries
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import ChatGrant

# Project Libraries
from core.models import Room


class AllRoomsView(LoginRequiredMixin, TemplateView):
    template_name = "chat/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rooms"] = Room.objects.all()
        return context


class RoomDetailsView(LoginRequiredMixin, TemplateView):
    template_name = "chat/room_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = kwargs.get("slug")
        context["room"] = Room.objects.get(slug=slug)
        return context

    def post(self, request, *args, **kwargs):
        # todo: on first post method, chat doesn't load why?
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class TwilioTokenView(LoginRequiredMixin, TemplateView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.account_sid = settings.TWILIO_ACCOUNT_SID
        self.api_key = settings.TWILIO_API_KEY
        self.api_secret = settings.TWILIO_API_SECRET
        self.chat_service_sid = settings.TWILIO_CHAT_SERVICE_SID
        self.access_token = None

    def get_twilio_token(self, identity="default_user"):
        self.access_token = AccessToken(
            self.account_sid, self.api_key, self.api_secret, identity=identity
        )

    def get(self, request, *args, **kwargs):
        identity = request.GET.get("identity", request.user.username)
        device_id = request.GET.get("device", "default")  # unique device ID

        self.get_twilio_token(identity)

        # Create a unique endpoint ID for the device
        endpoint = f"MyDjangoChatRoom:{identity}:{device_id}"

        if self.chat_service_sid:
            chat_grant = ChatGrant(
                endpoint_id=endpoint, service_sid=self.chat_service_sid
            )
            self.access_token.add_grant(chat_grant)

        response = {
            "identity": identity,
            "token": self.access_token.to_jwt(),
            "channel_name": "Sarah Lee",
        }

        return JsonResponse(response)


@login_required
def all_rooms(request):
    rooms = Room.objects.all()
    return render(request, "chat/index.html", {"rooms": rooms})


def room_detail(request, slug):
    room = Room.objects.get(slug=slug)
    return render(request, "chat/room_detail.html", {"room": room})


def token(request):
    # 3rd Party Libraries
    from faker import Faker

    fake = Faker()
    identity = request.GET.get("identity", fake.user_name())
    device_id = request.GET.get("device", "default")  # unique device ID

    account_sid = settings.TWILIO_ACCOUNT_SID
    api_key = settings.TWILIO_API_KEY
    api_secret = settings.TWILIO_API_SECRET
    chat_service_sid = settings.TWILIO_CHAT_SERVICE_SID

    token = AccessToken(account_sid, api_key, api_secret, identity=identity)

    # Create a unique endpoint ID for the device
    endpoint = f"MyDjangoChatRoom:{identity}:{device_id}"

    if chat_service_sid:
        chat_grant = ChatGrant(endpoint_id=endpoint, service_sid=chat_service_sid)
        token.add_grant(chat_grant)

    response = {"identity": identity, "token": token.to_jwt(), "channel_name": "Sarah Lee"}

    return JsonResponse(response)
