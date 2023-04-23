# Django Libraries
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.views import View

# Project Libraries
from core.models import Workouts


class SearchTrainersView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        search_term = request.POST.get("textfield", None)
        result = Workouts.objects.none()
        if search_term:
            search_term = search_term.strip().lower()
            qs = Workouts.objects.all()
            result = qs.filter(
                Q(title__icontains=search_term)
                | Q(description__icontains=search_term)
                | Q(trainer__username__icontains=search_term)
                | Q(trainer__first_name__icontains=search_term)
                | Q(trainer__last_name__icontains=search_term)
                | Q(trainer__email__icontains=search_term)
            )
        else:
            messages.error(request, "Empty Search Field Value.")
        return render(request, "search/index.html", {"queryset": result})
