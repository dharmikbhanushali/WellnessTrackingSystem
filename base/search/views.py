# Django Libraries
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import DetailView, ListView

# Project Libraries
from core.models import Workouts


class SearchTrainersView(LoginRequiredMixin, DetailView, ListView):
    paginate_by = 100  # if pagination is desired
    model = Workouts

    def get(self, request, *args, **kwargs):
        for key, value in request.GET.items():
            print(key, value)
        for key, value in kwargs.items():
            print(key, value)

        return HttpResponse("<h1>Hello HttpResponse</h1>")
