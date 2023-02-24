"""Database models."""
# Django Libraries
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    """User in the system."""

    def __str__(self):
        return f"{self.email} and {self.get_full_name()} : is_staff= {self.is_staff}"

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.
        """
        return reverse("user:detail", kwargs={"username": self.username})
