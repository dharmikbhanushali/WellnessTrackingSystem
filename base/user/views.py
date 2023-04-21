# Standard Library
import logging

# Django Libraries
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.translation import gettext_lazy as translate
from django.views.generic import DetailView, RedirectView, UpdateView

# Project Libraries
from core.models import Appointment, ClientMetrics, Workouts, WorkoutVideo
from user.forms import IntakeForm, UploadWorkoutVideoForm, WorkoutsForm


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
    return render(request, "chat/room_detail.html")


def test_template_form(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = IntakeForm(request.POST)
        if form.is_valid():
            intake_form = form.save(commit=False)
            intake_form.user = request.user
            intake_form.save()
            return redirect("/client-dashboard/")

    else:
        form = IntakeForm()
    return render(request, "pages/userform.html", {"form": form})


# if request.method == "POST":
#     form = IntakeForm(request.POST)
#     if form.is_valid():
#         intake_form = form.save(commit=False)
#         intake_form.user = request.user
#         intake_form.save()
#         messages.success(request, "Intake form submitted successfully.")
#         return redirect("client_dashboard")
# else:
#     form = IntakeForm()
# return render(request, "pages/userform.html",{'form': form})


def Workouts_list_all(request):
    workouts = Workouts.objects.all()
    context = {"workouts": workouts}
    return render(request, "workouts_list.html", context)


@login_required
def Intake_form(request):
    if request.method == "POST":
        form = IntakeForm(request.POST)
        if form.is_valid():
            intake_form = form.save(commit=False)
            intake_form.user = request.user
            intake_form.save()
            messages.success(request, "Intake form submitted successfully.")
            return redirect("client_dashboard")
    else:
        form = IntakeForm()
    return render(request, "userForm.html", {"form": form})


@login_required
def Client_dashboard(request):
    client_metrics = ClientMetrics.objects.filter(user=request.user)
    context = {
        "client_metrics": client_metrics,
    }
    return render(request, "pages/userDashboard.html", context)


# Trainer dashboard
@login_required
def Trainer_dashboard(request):
    trainer = request.user
    workout_plans = Workouts.objects.filter(trainer=trainer)
    appointments = Appointment.objects.filter(trainer=trainer)

    context = {
        "trainer": trainer,
        "workout_plans": workout_plans,
        "appointments": appointments,
    }
    return render(request, "pages/trainerDashboard.html", context)


@login_required
def Create_workout(request):
    if request.method == "POST":
        form = WorkoutsForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.trainer = request.user
            workout.save()
            return redirect("workouts_list")
    else:
        form = WorkoutsForm()
    return render(request, "create_workout.html", {"form": form})


def upload_workout_video(request):
    if request.method == "POST":
        form = UploadWorkoutVideoForm(request.POST, request.FILES)
        if form.is_valid():
            workout_video = form.save()
            return redirect("placeholder_workout_page_view", pk=workout_video.pk)
    else:
        form = UploadWorkoutVideoForm()
    return render(request, "upload_workout_video.html", {"form": form})


@login_required
def Update_workout(request, pk):
    workout = get_object_or_404(Workouts, pk=pk)
    if request.method == "POST":
        form = WorkoutsForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            return redirect("workouts_list")
    else:
        form = WorkoutsForm(instance=workout)
    return render(request, "update_workout.html", {"form": form})


@login_required
def Delete_workout(request, pk):
    workout = get_object_or_404(Workouts, pk=pk)
    workout.delete()
    return redirect("workouts_list")


@login_required
def Workouts_list_trainer(request):
    workouts = Workouts.objects.filter(trainer=request.user)
    return render(request, "workouts_list.html", {"workouts": workouts})


@login_required
def View_appointments(request):
    trainer = request.user
    appointments = Appointment.objects.filter(trainer=trainer)
    context = {"appointments": appointments}
    return render(request, "view_appointments.html", context)


def view_workout_video(request, pk):
    video = get_object_or_404(WorkoutVideo, pk=pk)
    return render(request, "workout_video_placeholder.html", {"video": video})


def view_workouts(request, pk):
    workout = get_object_or_404(Workouts, pk=pk)
    return render(request, "workout_detail_placeholder.html", {"workout": workout})
