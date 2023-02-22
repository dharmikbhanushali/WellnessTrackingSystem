# Django Libraries
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as translate
from django.views.generic import DetailView, RedirectView, UpdateView


User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # slug_field = "email"
    # slug_url_kwarg = "email"
    slug_field = "username"
    slug_url_kwarg = "username"


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ["name"]
    success_message = translate("Information successfully updated")

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        # return reverse("user:detail", kwargs={"email": self.request.user})
        return reverse("users:detail", kwargs={"username": self.request.user.username})
