"""Database models."""
# Django Libraries
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings

# Project Libraries

from core.constants import CLIENT, USER_TYPES


class User(AbstractUser):
    """User in the system."""

    # todo: what for admin?
    user_type = models.CharField(
        max_length=2,
        choices=USER_TYPES,
        default=CLIENT,
    )

    def __str__(self):
        return f"{self.email} and {self.get_full_name()} : is_staff= {self.is_staff}"

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.
        """
        return reverse("user:detail", kwargs={"username": self.username})

    def get_user_type(self):
        """Get Current user's type.

        Returns:

        """
        return self.user_type


class IntakeForm(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField(auto_now_add=False, default=timezone.now)
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField()
    mobile_phone = models.CharField(max_length=20)
    home_phone = models.CharField(max_length=20)
    height = models.FloatField()
    weight = models.FloatField()
    date_joined = models.DateTimeField(auto_now_add=False, default=timezone.now)

    def __str__(self):
        return f"{self.user}'s Intake Form"


class Workouts(models.Model):
    trainer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_url = models.URLField(null=True, blank=True)
    plan_url = models.URLField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)
    rating = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class WorkoutsAssigned(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workouts, on_delete=models.CASCADE)
    date_assigned = models.DateField()
    date_completed = models.DateField()
    completed = models.BooleanField(default=False)


class ClientMetrics(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    workouts = models.ManyToManyField(
        WorkoutsAssigned, related_name="assigned_workouts"
    )
    meals = models.TextField()
    sleep_cycle = models.TextField()
    progress_metrics = models.TextField()
    calories_burnt = models.IntegerField()
    # workouts_registered = models.ManyToManyField(Workouts)
    goal_progress = models.FloatField()
    completed_workouts = models.ManyToManyField(
        WorkoutsAssigned, related_name="completed_workout"
    )


def __str__(self):
    return f"{self.user.username}'s metrics for {self.date}"
