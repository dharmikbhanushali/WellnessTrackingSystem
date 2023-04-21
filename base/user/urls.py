"""URL mappings for the user API."""
# Django Libraries
from django.urls import path

# Project Libraries
from user.views import (
    Client_dashboard,
    Create_workout,
    Delete_workout,
    Intake_form,
    Trainer_dashboard,
    Update_workout,
    UserDetailView,
    UserRedirectView,
    UserUpdateView,
    Workouts_list_trainer,
    enroll_workout,
    mark_workout_complete,
    view_all_workouts,
    view_workout_video,
    view_workouts,
)


app_name = "user"

urlpatterns = [
    path("~redirect/", view=UserRedirectView.as_view(), name="redirect"),
    path("~update/", view=UserUpdateView.as_view(), name="update"),
    path("<str:username>/", view=UserDetailView.as_view(), name="detail"),
    # Display client dashboard
    path("client-dashboard/", view=Client_dashboard, name="client_metrics"),
    path("trainer_dashboard/", view=Trainer_dashboard, name="client_metrics"),
    # Create a new workout
    path("create/", view=Create_workout, name="ccreate_workoutre"),
    # View an individual workout
    path("<int:pk>/", view=Update_workout, name="update_workout"),
    # Edit an existing workout
    path("<int:pk>/edit/", view=Delete_workout, name="delete_workout"),
    # Delete a workout
    path("<int:pk>/delete/", view=Delete_workout, name="workout_delete"),
    path("trainer/workouts/", view=Workouts_list_trainer, name="workouts_list"),
    path("intake-form/", view=Intake_form, name="intake_form"),
    path("workout-video/<int:pk>/", view=view_workout_video, name="view_workout_video"),
    path("workouts/<int:workout_id>", view=view_workouts, name="view_workouts"),
    path("workouts/a/", view_all_workouts, name="view_all_workouts"),
    path("enroll/<int:workout_id>/", enroll_workout, name="enroll_workout"),
    path(
        "mark-complete/<int:workout_id>/",
        mark_workout_complete,
        name="mark_workout_complete",
    ),
]
