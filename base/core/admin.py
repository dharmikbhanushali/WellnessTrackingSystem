"""Django admin customization."""
# Django Libraries
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as translate

# Project Libraries
from core.models import ClientMetrics, IntakeForm, Workouts, WorkoutsAssigned
from user.forms import UserAdminChangeForm, UserAdminCreationForm


User = get_user_model()


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""

    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    ordering = ["email"]
    list_display = ["email", "user_type", "is_staff", "is_superuser", "is_active"]
    list_display_links = ["email"]
    list_editable = ["is_staff", "is_active"]
    search_fields = ["email"]

    fieldsets = (
        (translate("Details"), {"fields": ("email", "password")}),
        (
            translate("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (translate("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    readonly_fields = ["last_login"]

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )


admin.site.register(User, UserAdmin)
admin.site.register(IntakeForm)
admin.site.register(Workouts)
admin.site.register(WorkoutsAssigned)
admin.site.register(ClientMetrics)
