# Django Libraries
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, get_user_model
from django.utils.translation import gettext_lazy as translate

# 3rd Party Libraries
from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm


User = get_user_model()


class UserAdminChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ("email",)


class UserAdminCreationForm(UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(UserCreationForm.Meta):
        model = User

        error_messages = {
            "email": {"unique": translate("This email has already been taken.")}
        }
        fields = ("email",)


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """

    ...


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """

    ...
