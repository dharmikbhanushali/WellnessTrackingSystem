"""Django command to wait for the database to be available."""
# Standard Library
from time import sleep

# Django Libraries
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError

# 3rd Party Libraries
from psycopg2 import OperationalError as Psycopg2OpError


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        wait_time = 5
        is_db_up = False
        while is_db_up is False:
            try:
                self.check(databases=["default"])
                is_db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write(
                    f"Database unavailable, waiting {wait_time} second..."
                )
                sleep(wait_time)
        self.stdout.write(self.style.SUCCESS("Database available!"))
