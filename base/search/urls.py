"""URL mappings for the user API."""
# Django Libraries
from django.urls import path

# Project Libraries
from search.views import SearchTrainersView


app_name = "search"

urlpatterns = [path("", SearchTrainersView.as_view(), name="search_trainers")]
