"""Include all urls used for sample/testing/trying out features."""
# Django Libraries
from django.urls import path

# Project Libraries
from prototype.views import RenderSampleTemplate, SampleMailAdmin


app_name = "prototype"

urlpatterns = [
    path("email", SampleMailAdmin.as_view(), name="send_email"),
    path("template", RenderSampleTemplate.as_view(), name="render_template"),
]
