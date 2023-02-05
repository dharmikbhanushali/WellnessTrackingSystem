"""Django command to create django superuser automatically on first boot."""
# Standard Library
import logging

# Django Libraries
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

# 3rd Party Libraries
from rest_framework.authtoken.models import Token
from tqdm import tqdm

# Project Libraries
from settings.base import env


logger = logging.getLogger("wrike_api")
logger.setLevel("INFO")


class Command(BaseCommand):
    """Django command to automatically create superuser on first boot."""

    def handle(self, *args, **options):
        """Uses Environment Variables to create admin user is no admin user exists.

        Entrypoint for command.

        Notes:
            `DJANGO_SUPERUSER_USERNAME`, `DJANGO_SUPERUSER_EMAIL`,
            `DJANGO_SUPERUSER_PASSWORD` from `.env` files are used to create the
            admin user.

        See Also:
            :ref:`settings`
        """
        users = get_user_model()
        if users.objects.filter(is_superuser=True).count() == 0:
            name = env("DJANGO_SUPERUSER_USERNAME")
            email = env("DJANGO_SUPERUSER_EMAIL")
            password = env("DJANGO_SUPERUSER_PASSWORD")
            token = None
            logger.info(f"Creating account for {name} ({email})")
            for i in tqdm(range(1), total=1, desc="Add Super User..."):
                user = users.objects.create_superuser(
                    email=email, name=name, password=password
                )
                token, created = Token.objects.get_or_create(user=user)
            logger.info(f"Auth Token for {name} ({email}) is: `token {token}`")
        else:
            logger.info("Admin account exists!, Skipping creation of admin user.")
