# Standard Library
import logging

from datetime import timedelta

# Django Libraries
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as translate
from django.views.generic import DetailView, RedirectView, UpdateView

# Project Libraries
from core.models import Appointment, ClientMetrics, Workouts, WorkoutsAssigned
from user.forms import IntakeForm, WorkoutsForm


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


# View added to test backend data
# def testing(request):
#     user = request.user

#     # Get user's metrics
#     try:
#         metrics = ClientMetrics.objects.filter(user=user).latest('date')
#         calories_burned_today = metrics.calories_burnt
#     except ClientMetrics.DoesNotExist:
#         calories_burned_today = 0

#     # Get calories burned in the last 7 days
#     seven_days_ago = datetime.now() - datetime.timedelta(days=7)
#     calories_burned_last_seven_days = ClientMetrics.objects.filter(user=user, date__gte=seven_days_ago)
# .aggregate(models.Sum('calories_burnt'))['calories_burnt__sum'] or 0
#     # Get calories burned for each day in the last 7 days
#     days = [(datetime.now() - datetime.timedelta(days=i)).date() for i in range(7)]
#     calories_burned_by_day = []
#     for day in days:
#         calories_burned = ClientMetrics.objects.filter(user=user, date=day).
# aggregate(models.Sum('calories_burnt'))['calories_burnt__sum'] or 0
#         calories_burned_by_day.append({'day': day.strftime('%A'), 'calories_burned': calories_burned})

#     # Get user's info
#     user_info = {'name': user.get_full_name(), 'age': user.age, 'weight': user.weight}

#     # Get active classes for the user
#     active_classes = WorkoutsAssigned.objects.filter(user=user, completed=False).order_by('-date_assigned')

#     context = {'calories_burned_today': calories_burned_today,
#                'calories_burned_last_seven_days': calories_burned_last_seven_days,
#                'calories_burned_by_day': calories_burned_by_day,
#                'user_info': user_info,
#                'active_classes': active_classes}
#     return render(request, 'pages/userDashboard.html', context)


# # if request.method == "POST":
# #     form = IntakeForm(request.POST)
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


# @login_required
# def Client_dashboard(request):
#     client_metrics = ClientMetrics.objects.filter(user=request.user)
#     context = {
#         "client_metrics": client_metrics,
#     }
#     return render(request, "pages/userDashboard.html", context)

# @login_required
# def client_dashboard(request):
#     user = request.user

#     # Get user's metrics
#     try:
#         metrics = ClientMetrics.objects.filter(user=user).latest('date')
#         calories_burned_today = metrics.calories_burnt
#     except ClientMetrics.DoesNotExist:
#         calories_burned_today = 0

#     # Get calories burned in the last 7 days
#     seven_days_ago = datetime.now() - timedelta(days=7)
#     calories_burned_last_seven_days = ClientMetrics.objects.filter(user=user,
# date__gte=seven_days_ago).aggregate(models.Sum('calories_burnt'))['calories_burnt__sum'] or 0

#     # Get calories burned for each day in the last 7 days
#     days = [(datetime.now() - timedelta(days=i)).date() for i in range(7)]
#     calories_burned_by_day = []
#     for day in days:
#         calories_burned = ClientMetrics.objects.filter(user=user, date=day)
# .aggregate(models.Sum('calories_burnt'))['calories_burnt__sum'] or 0
#         calories_burned_by_day.append({'day': day.strftime('%A'), 'calories_burned': calories_burned})

#     # Get user's info
#     user_info = {'name': user.get_full_name(), 'age': user.age, 'weight': user.weight}

#     # Get active classes for the user
#     active_classes = WorkoutsAssigned.objects.filter(user=user, completed=False).order_by('-date_assigned')

#     context = {'calories_burned_today': calories_burned_today,
#                'calories_burned_last_seven_days': calories_burned_last_seven_days,
#                'calories_burned_by_day': calories_burned_by_day,
#                'user_info': user_info,
#                'active_classes': active_classes}
#     return render(request, 'pages/userDashboard.html', context)


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
            workout.save()
            return redirect("workouts_list")
    else:
        form = WorkoutsForm()
    return render(request, "testing.html", {"form": form})


# def upload_workout_video(request):
#     if request.method == "POST":
#         form = UploadWorkoutVideoForm(request.POST, request.FILES)
#         if form.is_valid():
#             workout_video = form.save()
#             return redirect("placeholder_workout_page_view", pk=workout_video.pk)
#     else:
#         form = UploadWorkoutVideoForm()
#     return render(request, "upload_workout_video.html", {"form": form})


# @login_required
# def Update_workout(request, pk):
#     workout = get_object_or_404(Workouts, pk=pk)
#     if request.method == "POST":
#         form = WorkoutsForm(request.POST, instance=workout)
#         if form.is_valid():
#             form.save()
#             return redirect("workouts_list")
#     else:
#         form = WorkoutsForm(instance=workout)
#     return render(request, "update_workout.html", {"form": form})


# @login_required
# def Delete_workout(request, pk):
#     workout = get_object_or_404(Workouts, pk=pk)
#     workout.delete()
#     return redirect("workouts_list")


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


# def view_workout_video(request, pk):
#     video = get_object_or_404(WorkoutVideo, pk=pk)
#     return render(request, "workout_video_placeholder.html", {"video": video})


def view_workout(request, workout_id):
    workout = get_object_or_404(Workouts, id=workout_id)
    return render(request, "workout_detail_placeholder.html", {"workout": workout})


def view_all_workouts(request):
    workout = get_object_or_404(Workouts)
    return render(request, "workout_list_view_placeholder.html", {"workouts": workout})


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
    user = request.user
    workout = Workouts.objects.get(id=workout_id)
    if date_assigned:
        WorkoutsAssigned.objects.create(
            user=user, workout=workout, date_assigned=date_assigned
        )
    else:
        WorkoutsAssigned.objects.create(user=user, workout=workout)
    return redirect("client_dashboard")


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


@login_required
def Client_dashboard(request):
    user = request.user
    intake_form = IntakeForm.objects.get(user=user)
    today = timezone.now().date()
    metrics_today = ClientMetrics.objects.filter(user=user, date=today).first()
    workouts_assigned_today = []
    if metrics_today:
        workouts_assigned_today = metrics_today.workouts.all()
    calories_burnt_today = metrics_today.calories_burnt if metrics_today else 0
    # Calculate calories burnt for the last 7 days
    # last_week = today - timedelta(days=7)
    # calories_burnt_last_week = (
    #     ClientMetrics.objects.filter(
    #         user=user, date__range=[last_week, today]
    #     ).aggregate(sum("calories_burnt"))["calories_burnt__sum"]
    #     or 0
    # )
    date_calories_pairs_last_week = {}
    for i in range(7):
        date_to_check = today - timedelta(days=i)
        calories_burnt_on_date = (
            ClientMetrics.objects.filter(user=user, date=date_to_check).aggregate(
                sum("calories_burnt")
            )["calories_burnt__sum"]
            or 0
        )
        date_calories_pairs_last_week[
            date_to_check.strftime("%m/%d/%Y")
        ] = calories_burnt_on_date

    context = {
        "user": user,
        "name": intake_form.name,
        "age": (today - intake_form.date_of_birth).days // 365,
        "gender": intake_form.get_gender_display(),
        "workouts_assigned_today": workouts_assigned_today,
        "calories_burnt_today": calories_burnt_today,
        "calories_burnt_last_week": date_calories_pairs_last_week,
    }
    return render(request, "client_dashboard.html", context)


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
