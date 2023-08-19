from django.urls import path
from .views import RateAPIView

urlpatterns = [path("show_rates/", RateAPIView.as_view())]
