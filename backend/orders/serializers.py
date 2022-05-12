from rest_framework import serializers
from .models import OrderInfo,OrderInvoice,OrderPayment

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderInfo
        fields = ('id','cust_id','vehicle_id','pickup_id','dropoff_id','pickup_date','dropoff_date','start_odo','end_odo','odo_limit','amount')

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderInvoice
        fields = ('id','order_id','invoice_date','amount')


class PaymentSerializer(serializers.ModelSerializer):   
    class Meta:
        model = OrderPayment
        fields = ('id', 'invoice_id','pay_method','cardno','pay_date','amount')
    
    