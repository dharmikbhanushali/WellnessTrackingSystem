"""URL mappings for the user API."""
# Django Libraries
from django.urls import path

# Project Libraries
from user.views import (
    Client_dashboard,
    Create_workout,
    Trainer_dashboard,
    UserDetailView,
    UserRedirectView,
    UserUpdateView,
    Workouts_list_trainer,
    enroll_workout,
    get_workouts_assigned_all,
    get_workouts_assigned_by_date,
    mark_workout_complete,
    view_workout,
)


app_name = "user"

urlpatterns = [
    path("~redirect/", view=UserRedirectView.as_view(), name="redirect"),
    path("~update/", view=UserUpdateView.as_view(), name="update"),
    path("<str:username>/", view=UserDetailView.as_view(), name="detail"),
    # Display client dashboard
    # path("client-dashboard/", view=Client_dashboard, name="client_metrics"),
    # path("trainer_dashboard/", view=Trainer_dashboard, name="client_metrics"),
    # Create a new workout
    path("workout/create/", view=Create_workout, name="create_workoutre"),
    # View an individual workout
    # path("<int:pk>/", view=Update_workout, name="update_workout"),
    # Edit an existing workout
    # path("<int:pk>/edit/", view=Delete_workout, name="delete_workout"),
    # Delete a workout
    # path("<int:pk>/delete/", view=Delete_workout, name="workout_delete"),
    path("trainer/workouts/", view=Workouts_list_trainer, name="workouts_list"),
    # path("workout-video/<int:pk>/", view=view_workout_video, name="view_workout_video"),
    path("workouts/<int:workout_id>", view=view_workout, name="view_workouts"),
    path(
        "enroll-workout/<int:workout_id>/", view=enroll_workout, name="enroll_workout"
    ),
    path(
        "enroll-workout/<int:workout_id>/<str:date_assigned>/",
        view=enroll_workout,
        name="enroll_workout",
    ),
    path(
        "mark-complete/<int:workout_id>/",
        view=mark_workout_complete,
        name="mark_workout_complete",
    ),
    path(
        "assigned-workouts/",
        view=get_workouts_assigned_all,
        name="get_workouts_assigned_all",
    ),
    path(
        "assigned-workouts/<str:date>/",
        view=get_workouts_assigned_by_date,
        name="get_workouts_assigned_by_date",
    ),
    path(
        "client_dashboard/",
        view=Client_dashboard,
        name="Client_dashboard",
    ),
    path(
        "trainer_dashboard/",
        view=Trainer_dashboard,
        name="Trainer_dashboard",
    ),
]
