"""base_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/

Examples:
    Function views
        1. Add an import:  from my_app import views
        2. Add a URL to urlpatterns:  path('', views.home, name='home')
    Class-based views
        1. Add an import:  from other_app.views import Home
        2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
    Including another URLconf
        1. Import the include() function: from django.urls import include, path
        2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""
# Django Libraries
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import debug, defaults as default_views
from django.views.generic import TemplateView

# Project Libraries
from user.views import test_template, test_template_form


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# ----------------------------------------------------------------------------
# Debug Urls
# ----------------------------------------------------------------------------
if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path("debug/", debug.default_urlconf),
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        # 3rd Party Libraries
        import debug_toolbar

        urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# ----------------------------------------------------------------------------
# Custom API  url
# ----------------------------------------------------------------------------
urlpatterns += [
    path("user/", include("user.urls")),
]

# ----------------------------------------------------------------------------
# Account management urls
# ----------------------------------------------------------------------------
urlpatterns += [
    # User management
    # path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("allauth.urls")),
    path("accounts/", include("allauth_2fa.urls")),
]

# ----------------------------------------------------------------------------
# App urls
# ----------------------------------------------------------------------------
urlpatterns += [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    path("test_template/", view=test_template, name="test"),
    path("test_template_form/", view=test_template_form, name="test_form"),
]
