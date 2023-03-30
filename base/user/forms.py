# Django Libraries
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, get_user_model
from django.utils.translation import gettext_lazy as translate

# 3rd Party Libraries
from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm

# Project Libraries
from core.constants import USER_TYPES


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
