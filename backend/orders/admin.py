from django.contrib import admin
from .models import OrderInfo,OrderInvoice,OrderPayment
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','vehicle_id', 'cust_id', 'pickup_id','dropoff_id','pickup_date','dropoff_date')

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id','order_id','invoice_date','amount')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id','invoice_id','pay_date','amount')

admin.site.register(OrderInfo, OrderAdmin)
admin.site.register(OrderInvoice, InvoiceAdmin)
admin.site.register(OrderPayment, PaymentAdmin)