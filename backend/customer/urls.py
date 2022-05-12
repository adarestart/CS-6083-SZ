from django.urls import path
from .views import IndividualView,CorporationView

urlpatterns = [
    path('individual/', IndividualView.as_view()),
    path('corp/',CorporationView.as_view()),
]