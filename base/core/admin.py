"""Django admin customization."""
# Django Libraries
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as translate

# Project Libraries
from core.models import User


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""

    ordering = ["id"]
    list_display = ["email", "name", "is_staff", "is_superuser", "is_active"]
    list_display_links = ["email", "name"]
    list_editable = ["is_staff", "is_active"]
    search_fields = ["email", "name"]
    fieldsets = (
        (translate("details"), {"fields": ("email", "password")}),
        (translate("Personal Info"), {"fields": ("name",)}),
        (
            translate("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (translate("Important dates"), {"fields": ("last_login",)}),
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
                    "name",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )


admin.site.register(User, UserAdmin)
