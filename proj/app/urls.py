from django.urls import path

from .views import RedirectToOriginalUrlView, GenerateShortUrlView

app_name = "app"

urlpatterns = [
    path("shorten/", GenerateShortUrlView.as_view(), name="generate_short_url"),
    path("<str:short_code>/", RedirectToOriginalUrlView.as_view(), name="redirect_to_original_url")

]