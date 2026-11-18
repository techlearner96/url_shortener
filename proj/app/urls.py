from django.urls import path

from .views import GetOriginalUrlView, GenerateShortUrlView

app_name = "app"

urlpatterns = [
    path("shorten/", GenerateShortUrlView.as_view(), name="generate_short_url"),
    path("<str:short_code>/", GetOriginalUrlView.as_view(), name="redirect_to_original_url")

]