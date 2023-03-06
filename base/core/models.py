"""Database models."""
# Django Libraries
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    """User in the system."""

    CLIENT = "CL"
    TRAINER = "TR"
    USER_TYPES = [
        (CLIENT, "Client"),
        (TRAINER, "Trainer"),
    ]
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
