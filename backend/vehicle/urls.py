from django.urls import path
from .views import VehicleInfoView,VehicleFullView,VehicleOfficeView,VehicleClassView,VehicleView,SingleVehicleView

urlpatterns = [
    path('', VehicleInfoView.as_view()),
    path('vehicle/', VehicleView.as_view()),
    path('vehicle/<int:vehicle_id>/', SingleVehicleView.as_view()),
    path('<int:vehicle_id>/', VehicleFullView.as_view()),
    path('office/', VehicleOfficeView.as_view()),
    path('class/', VehicleClassView.as_view()),
]