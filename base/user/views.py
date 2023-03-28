# Standard Library
import logging

# Django Libraries
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import gettext_lazy as translate
from django.views.generic import DetailView, RedirectView, UpdateView


User = get_user_model()

logger = logging.getLogger("fitness-tracker")


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = "users/user_detail.html"


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ["first_name", "last_name", "password"]
    success_message = translate("Information successfully updated")
    template_name = "users/user_form.html"

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False
    model = User

    def get_redirect_url(self):
        # todo: check if user has intake form or not in database.
        # todo: based upon the user type, redirect to specific url
        if True:
            logger.info("Here................")
            if self.request.user.get_user_type() == "Client":
                # return render(self.request, "pages/userform.html")
                return reverse("test")
            return reverse("test")
        return reverse("user:detail", kwargs={"username": self.request.user.username})


def test_template(request):
    return render(request, "pages/userDashboard.html")


def test_template_form(request):
    return render(request, "pages/userform.html")
