from django.urls import path
from .views import OrderView, InvoiceView,PaymentView,SingleOrderView,SinglePaymentView,SingleInvoiceView
urlpatterns = [
    path('', OrderView.as_view()),
    path('invoice/', InvoiceView.as_view()),
    path('payment/',PaymentView.as_view()),
    path('<int:order_id>/',SingleOrderView.as_view()),
    path('invoice/<int:order_id>/', SingleInvoiceView.as_view()),
    path('payment/<int:order_id>/',SinglePaymentView.as_view()),
    #path('vehicles/<int:vehicle_id>/', VehicleFullView.as_view()),
    #path('vehicles/<str:city>/',VehicleView.as_view()),
]