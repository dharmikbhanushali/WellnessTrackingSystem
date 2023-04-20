# Django Libraries
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, get_user_model
from django.utils.translation import gettext_lazy as translate

# 3rd Party Libraries
from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm

# Project Libraries
from core.constants import USER_TYPES
from core.models import IntakeForm, Workouts, WorkoutsAssigned, WorkoutVideo


User = get_user_model()


class UserAdminChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        # fields = ("email",)


class UserAdminCreationForm(UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": translate("This username has already been taken.")}
        }
        # fields = ("email",)


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """

    user_type = forms.ChoiceField(choices=USER_TYPES)

    def save(self, request):
        # Ensure you call the parent class's safe.
        # .save() returns a User object.
        user = super().save(request)

        # Add your own processing here.
        user.user_type = self.cleaned_data["user_type"]
        user.save()
        # You must return the original result.
        return user


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """

    ...


class IntakeForm(forms.ModelForm):
    class Meta:
        model = IntakeForm
        fields = [
            "name",
            "date_of_birth",
            "gender",
            "email",
            "mobile_phone",
            "home_phone",
            "height",
            "weight",
            "preferred_workout_category",
            "preferred_workout_level",
        ]
        widgets = {
            "preferred_workout_category": forms.CheckboxSelectMultiple(),
            "preferred_workout_level": forms.CheckboxSelectMultiple(),
        }


class WorkoutsForm(forms.ModelForm):
    class Meta:
        model = Workouts
        fields = [
            "trainer",
            "title",
            "description",
            "video_url",
            "plan_url",
            "rating",
            "category",
            "level",
        ]
        widgets = {
            "category": forms.CheckboxSelectMultiple(),
            "level": forms.CheckboxSelectMultiple(),
        }


class UploadWorkoutVideoForm(forms.ModelForm):
    class Meta:
        model = WorkoutVideo
        fields = ["title", "description", "video_file"]


class EnrollWorkoutForm(forms.ModelForm):
    class Meta:
        model = WorkoutsAssigned
        fields = ["workout", "date_assigned"]


class MarkWorkoutCompleteForm(forms.ModelForm):
    class Meta:
        model = WorkoutsAssigned
        fields = ["completed", "date_completed"]


# class Intakeform(forms.ModelForm):

#     class Meta:
#         model = ClientMetrics
