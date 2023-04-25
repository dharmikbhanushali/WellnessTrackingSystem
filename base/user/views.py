# Standard Library
import logging

from datetime import timedelta, timezone

# Django Libraries
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone as timezoneDjango
from django.utils.translation import gettext_lazy as translate
from django.views.generic import DetailView, RedirectView, UpdateView

# Project Libraries
from core import constants
from core.models import (
    Appointment,
    ClientMetrics,
    IntakeForm as IntakeFormModel,
    TrainerIntake as trainerFormModel,
    Workouts,
    WorkoutsAssigned,
)
from user.forms import IntakeForm, TrainerForm, WorkoutsForm


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
        return reverse("user:detail", kwargs={"username": self.request.user.username})


# # this is a test for templates
# def test_template(request):
#     return render(request, "pages/dietplan2.html")


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


def Workouts_list_all(request):
    workouts = Workouts.objects.all()
    trainerDetails = trainerFormModel.objects.all()
    context = {"workouts": workouts, "trainerDetails": trainerDetails}
    return render(request, "pages/workout1.html", context)


def recommend_workouts(request):
    workouts = Workouts.objects.filter(
        trainer__username="trainer123@gmail.com"
    )
    trainerDetails = trainerFormModel.objects.all()
    context = {"workouts": workouts, "trainerDetails": trainerDetails}
    return render(request, "pages/recommendedworkouts.html", context)

@login_required
def Intake_form(request):
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
        form = WorkoutsForm(request.POST, request.FILES)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.trainer = request.user
            # workout.image = form.cleaned_data['image']
            workout.save()
            return redirect("/trainer_dashboard/")
    else:
        form = WorkoutsForm()
    return render(request, "pages/createWorkoutForm.html", {"form": form})


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


@login_required
def view_workout(request, assigned_workouts_id):
    assigned_workout = get_object_or_404(WorkoutsAssigned, id=assigned_workouts_id)
    print(assigned_workout)
    context = {"assigned_workout": assigned_workout}
    return render(request, "pages/testing.html", context)


# def view_all_workouts(request):
#     workout = Workouts.objects.all
#     return render(request, "pages/workout1.html", {"workouts": workout})


# Workout recommendations
def workout_recommendations(request):
    # Get the user's intake form
    intake_form = IntakeForm.objects.get(user=request.user)
    # Get the user's preferred workout category and level
    category = intake_form.preferred_workout_category
    level = intake_form.preferred_workout_level
    # Get all workouts with the user's preferred category and level
    workouts = Workouts.objects.filter(category=category, level=level)
    context = {
        "workout_recomended": workouts,
    }
    return render(request, "pages/userDashboard.html", context)


# @login_required
# def client_dashboard(request):
#     user = request.user
#     intake_form = IntakeForm.objects.get(user=user)
#     workouts_assigned = WorkoutsAssigned.objects.filter(user=user)
#     today = timezone.now().date()
#     calories_burnt_today = workouts_assigned.filter(date_completed=today, completed=True).
# aggregate(Sum('workout__calories_burnt'))['workout__calories_burnt__sum']
#     past_7_days = today - timezone.timedelta(days=7)
#     workouts_completed_past_7_days = workouts_assigned.filter(date_completed__gte=past_7_days,
#  completed=True).values('date_completed').annotate(total_calories_burnt=Sum('workout__calories_burnt'))

#     context = {
#         'user': user,
#         'intake_form': intake_form,
#         'workouts_assigned': workouts_assigned,
#         'calories_burnt_today': calories_burnt_today,
#         'workouts_completed_past_7_days': workouts_completed_past_7_days,
#     }
#     return render(request, 'client_dashboard.html', context)


# Enrolling in a workout
@login_required
def enroll_workout(request, workout_id, date_assigned=None):
    workout = get_object_or_404(Workouts, id=workout_id)
    assigned_workout = WorkoutsAssigned(
        user=request.user,
        workout=workout,
        date_assigned=timezoneDjango.now().date(),
        date_completed=None,
        completed=False,
    )

    assigned_workout.save()

    metrics = ClientMetrics(
        user=request.user,
        date=timezoneDjango.now().date(),
        meals="Some meals here",
        sleep_cycle="Some sleep cycle here",
        progress_metrics="Some progress metrics here",
        calories_burnt=500,
        goal_progress=80.0,
    )
    metrics.save()
    # Add workout to metrics
    metrics.workouts.add(assigned_workout)
    return redirect("/client-dashboard/")


# Marking workout as complete
@login_required
def mark_workout_complete(request, workout_id):
    workout = Workouts.objects.get(id=workout_id)
    workout_assigned = WorkoutsAssigned.objects.get(
        user=request.user, workout=workout, completed=False
    )
    workout_assigned.completed = True
    workout_assigned.date_completed = timezone.now().date()
    workout_assigned.save()

    # Calculate calories burnt and add a record to the ClientMetrics model
    calories_burnt = workout_assigned.workout.calories
    client_metrics, created = ClientMetrics.objects.get_or_create(
        user=request.user, date=timezone.now().date()
    )
    # Add the completed workout to the list of completed workouts for the current day
    client_metrics.completed_workouts.add(workout_assigned)
    client_metrics.calories_burnt += calories_burnt
    client_metrics.save()
    return redirect("client_dashboard")


# this is a test for templates
# def test_template(request):
#     client_metrics = ClientMetrics.objects.all().values()
#     print(">>>>>client_metrics", client_metrics)
#     client_metrics = ClientMetrics.objects.filter(user=request.user).first()
#     print(">>>>>request.user", request.user)
#     print(">>>>>client_metrics", client_metrics)

#     #     client_metrics = {"Calories_burned_today": 124, "Calories_burned_in_last" : 500
#     # }
#     context = {
#         "client_metrics": client_metrics,
#         # "client_data": intake
#     }
#     return render(request, "pages/userDashboard.html", context)
#     # return render(request, "pages/userDashboard.html")


@login_required
def Client_dashboard(request):
    user = request.user
    intake_form = IntakeFormModel.objects.get(user=user)
    today = timezoneDjango.now().date()
    metrics_today = ClientMetrics.objects.filter(user=user, date=today).first()
    workouts_assigned_today = []
    if metrics_today:
        workouts_assigned_today = metrics_today.workouts.all()
    calories_burnt_today = metrics_today.calories_burnt if metrics_today else 0
    date_calories_pairs_last_week = {}
    date_calories_pairs_last_week = ClientMetrics.objects.filter(
        user=user, date=today + timedelta(days=1) - timedelta(days=7)
    )
    date_calories_pairs_last_week_dict_arr = []
    calories_burnt_last_week = 0
    for i in range(7):
        date_to_check = today - timedelta(days=i)

        workouts_assigned = WorkoutsAssigned.objects.filter(
            user=user, date_completed=date_to_check
        )
        calories_burnt_on_date = 0
        for w in workouts_assigned:
            calories_burnt_on_date += w.workout.calories
        # print(">>>>>>>>date_to_check", date_to_check)
        # print(">>>>>>>>calories_burnt_on_date", calories_burnt_on_date)

        calories_burnt_last_week += calories_burnt_on_date

        date_calories_pairs_last_week_dict_arr.insert(0, calories_burnt_on_date)

    context = {
        "user": user,
        "name": intake_form.name,
        "age": (today - intake_form.date_of_birth).days // 365,
        "weight": intake_form.weight,
        "workouts_assigned_today": workouts_assigned_today,
        "calories_burnt_today": calories_burnt_today,
        "calories_burnt_last_week": date_calories_pairs_last_week,
        "calories_burnt_last_week_int": calories_burnt_last_week,
        "calories_burnt_last_week_dict": date_calories_pairs_last_week_dict_arr,
    }
    return render(request, "pages/userDashboard.html", context)


# Retrieve workouts assigned based on the date assigned
def get_workouts_assigned_by_date(request, date):
    user = request.user
    assigned_workouts = WorkoutsAssigned.objects.filter(user=user, date_assigned=date)
    context = {"assigned_workouts": assigned_workouts}
    return render(request, "pages/userDashboard.html", context)


def get_workouts_assigned_all(request):
    user = request.user
    assigned_workouts = WorkoutsAssigned.objects.filter(user=user)
    context = {"assigned_workouts": assigned_workouts}
    return render(request, "pages/userDashboard.html", context)


@login_required
def trainerIntakeForm(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = TrainerForm(request.POST)
        if form.is_valid():
            trainer_form = form.save(commit=False)
            trainer_form.user = request.user
            trainer_form.save()
            return redirect("/trainer_dashboard/")
    else:
        form = TrainerForm(request.POST)
    return render(request, "pages/trainerform.html", {"form": form})


def redirectLoggedInUser(request):
    user = request.user
    user_type = user.user_type
    print(user_type)
    if user_type == constants.TRAINER:
        if trainerFormModel.objects.filter(user=user).exists():
            return redirect("/trainer_dashboard/")
        else:
            return redirect("/trainer-intake-form/")
    elif user_type == constants.CLIENT:
        if IntakeFormModel.objects.filter(user=user).exists():
            return redirect("/client-dashboard/")
        else:
            return redirect("/intake-form/")
