from django.db import models
from regex import DEBUG

# Create your models here.


class OrderInfo(models.Model):
    # office_id = models.IntegerField(verbose_name="office id", primary_key=True)
    pickup_id = models.CharField(verbose_name="pick up id",max_length=10)
    dropoff_id = models.CharField(verbose_name="drop off id",max_length=10)
    pickup_date = models.DateField(verbose_name="pick up date")
    dropoff_date = models.DateField(verbose_name="drop off date")
    start_odo = models.DecimalField(verbose_name="start odometer", max_digits=7, decimal_places=2)
    end_odo = models.DecimalField(verbose_name="end odometer", max_digits=7, decimal_places=2)
    # if start != end --> already returned 
    # 1. return a car
    # 2. rent a car
    odo_limit = models.DecimalField(verbose_name="odometer limit", max_digits=5, decimal_places=2)
    amount = models.DecimalField(verbose_name="order_amount", max_digits=8, decimal_places=2,default=0)

    vehicle_id = models.ForeignKey('vehicle.VehicleInfo',on_delete=models.SET(999))
    cust_id = models.ForeignKey('customer.IndividualInfo',on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Order'

    def __str__(self):
        return self.id+", "+self.cust_id+", "+self.vehicle_id

class OrderInvoice(models.Model):
    # office_id = models.IntegerField(verbose_name="office id", primary_key=True)
    invoice_date = models.DateField(verbose_name="invoice date")
    amount = models.DecimalField(verbose_name="invoice_amount", max_digits=8, decimal_places=2)
    
    order_id = models.ForeignKey('OrderInfo',on_delete=models.SET_DEFAULT,default=999)

    class Meta:
        verbose_name = 'Invoice'

    def __str__(self):
        return self.id+", "+self.amount

class OrderPayment(models.Model):
    # office_id = models.IntegerField(verbose_name="office id", primary_key=True)
    payment_choices = (
        (1, "debit card"),
        (2, "credit card"),
    )
    pay_method = models.SmallIntegerField(verbose_name="payment method", choices=payment_choices)
    cardno = models.CharField(verbose_name="Card Number",max_length=16)
    pay_date = models.DateField(verbose_name="payment date")
    amount = models.DecimalField(verbose_name="payment_amount", max_digits=8, decimal_places=2)
    
    invoice_id = models.ForeignKey('OrderInvoice',on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Payment'

    def __str__(self):
        return self.id+", "+self.amount