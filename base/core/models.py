"""Database models."""
# Django Libraries
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils import timezone

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
    mobile_phone = models.CharField(max_length=20, null=True, blank=True)
    home_phone = models.CharField(max_length=20, null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=False, default=timezone.now)
    WORKOUT_CATEGORY_CHOICES = (
        ("CARDIO", "Cardio"),
        ("STRENGTH", "Strength"),
        ("FLEXIBILITY", "Flexibility"),
        ("BALANCE", "Balance"),
    )

    WORKOUT_LEVEL_CHOICES = (
        ("BEGINNER", "Beginner"),
        ("INTERMEDIATE", "Intermediate"),
        ("ADVANCED", "Advanced"),
    )
    preferred_workout_category = models.CharField(
        max_length=20, choices=WORKOUT_CATEGORY_CHOICES, null=True, blank=True
    )
    preferred_workout_level = models.CharField(
        max_length=20, choices=WORKOUT_LEVEL_CHOICES, null=True, blank=True
    )

    def __str__(self):
        return f"{self.user}'s Intake Form"


class Workouts(models.Model):
    trainer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_url = models.URLField(null=True, blank=True)
    plan_url = models.URLField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    views = models.PositiveIntegerField(default=0, null=True, blank=True)
    rating = models.PositiveIntegerField(default=0, null=True, blank=True)
    WORKOUT_CATEGORY_CHOICES = (
        ("CARDIO", "Cardio"),
        ("STRENGTH", "Strength"),
        ("FLEXIBILITY", "Flexibility"),
        ("BALANCE", "Balance"),
    )

    WORKOUT_LEVEL_CHOICES = (
        ("BEGINNER", "Beginner"),
        ("INTERMEDIATE", "Intermediate"),
        ("ADVANCED", "Advanced"),
    )
    category = models.CharField(
        max_length=255, choices=WORKOUT_CATEGORY_CHOICES, null=True, blank=True
    )
    level = models.CharField(
        max_length=255, choices=WORKOUT_LEVEL_CHOICES, null=True, blank=True
    )
    thumbnail = models.ImageField(upload_to="workout_thumbnails/", null=True, blank=True)
    video_file = models.FileField(upload_to="workout_videos/", null=True, blank=True)
    duration = models.PositiveIntegerField(null=True, blank=True)
    calories = models.IntegerField()

    def __str__(self):
        return self.title


class WorkoutsAssigned(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )
    workout = models.ForeignKey(
        Workouts, on_delete=models.CASCADE, null=True, blank=True
    )
    date_assigned = models.DateField(null=True, blank=True)
    date_completed = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False, null=True, blank=True)


class ClientMetrics(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    workouts = models.ManyToManyField(
        WorkoutsAssigned, related_name="assigned_workouts", null=True, blank=True
    )
    meals = models.TextField(null=True, blank=True)
    sleep_cycle = models.TextField(null=True, blank=True)
    progress_metrics = models.TextField(null=True, blank=True)
    calories_burnt = models.IntegerField(null=True, blank=True)
    # workouts_registered = models.ManyToManyField(Workouts)
    goal_progress = models.FloatField(null=True, blank=True)
    completed_workouts = models.ManyToManyField(
        WorkoutsAssigned, related_name="completed_workout", null=True, blank=True
    )

    def __str__(self):
        return f"{self.user.username}'s metrics for {self.date}"


class Appointment(models.Model):
    trainer = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="appointments"
    )
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField()
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class Room(models.Model):
    """Represents chat rooms that users can join"""

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)

    def __str__(self):
        """Returns human-readable representation of the model instance."""
        return self.name


class TrainerIntake(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    age = models.IntegerField()
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField()
    current_address = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    certifications = models.CharField(max_length=255, blank=True, null=True)
    experience_years = models.PositiveIntegerField(blank=True, null=True)
    previous_work_experience = models.TextField(blank=True, null=True)
    fitness_specialization = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
