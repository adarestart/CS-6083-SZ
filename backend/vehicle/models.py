from django.db import models

# Create your models here.

class VehicleOffice(models.Model):
    # office_id = models.IntegerField(verbose_name="office id", primary_key=True)
    street = models.CharField(verbose_name="street", max_length=50)
    city = models.CharField(verbose_name="city", max_length=50)
    state = models.CharField(verbose_name="state", max_length=2,default='NY')
    zipcode = models.CharField(verbose_name="zipcode", max_length=6)
    phone = models.CharField(verbose_name="phone #", max_length=10)


    class Meta:
        verbose_name = 'Office'

    def __str__(self):
        return self.city


class VehicleClass(models.Model):
    # class_id = models.IntegerField(verbose_name="class id", max_length=2, primary_key=True)
    class_type = models.CharField(verbose_name="class type", max_length=50)

    daily_rate = models.DecimalField(verbose_name="daily rate for vehicle", max_digits=4, decimal_places=2)
    extra_rate = models.DecimalField(verbose_name="extra rate for vehicle", max_digits=4, decimal_places=2)
   

    class Meta:
        verbose_name = 'Class'

    def __str__(self):
        return self.class_type


class VehicleInfo(models.Model):
    # I guess we should have a PK mark here ================================= |
    # vehicle_id = models.CharField(verbose_name="vehicle id", max_length=10, primary_key=True)
    make = models.CharField(verbose_name="make", max_length=20)
    model = models.CharField(verbose_name="vehicle's model", max_length=20)
    make_year = models.DateField(verbose_name="made year")
    VIN = models.CharField(verbose_name="Vehicle_Identification_Number", max_length=10)
    LPN = models.CharField(verbose_name="License Plate Number", max_length=10)
    #slug = models.SlugField(max_length=1000)
    rented = models.BooleanField(default=False)

    vehicle_class = models.ForeignKey('VehicleClass', on_delete=models.CASCADE)
    office_info = models.ForeignKey('VehicleOffice', on_delete=models.CASCADE)

class VehicleFullInfo(models.Model):
    make = models.CharField(verbose_name="make", max_length=20)
    model = models.CharField(verbose_name="vehicle's model", max_length=20)
    make_year = models.DateField(verbose_name="made year")
    VIN = models.CharField(verbose_name="Vehicle_Identification_Number", max_length=10)
    LPN = models.CharField(verbose_name="License Plate Number", max_length=10)
    rented = models.BooleanField(default=False)

    class_type = models.CharField(verbose_name="class type", max_length=50)
    daily_rate = models.DecimalField(verbose_name="daily rate for vehicle", max_digits=4, decimal_places=2)
    extra_rate = models.DecimalField(verbose_name="extra rate for vehicle", max_digits=4, decimal_places=2)
   
    # add a few lines here
    street = models.CharField(verbose_name="street", max_length=50)
    city = models.CharField(verbose_name="city", max_length=50)
    state = models.CharField(verbose_name="state", max_length=2)
    zipcode = models.CharField(verbose_name="zipcode", max_length=6)
    phone = models.CharField(verbose_name="phone #", max_length=10)


    vehicle_class = models.ForeignKey('VehicleClass', on_delete=models.CASCADE)
    office_info = models.ForeignKey('VehicleOffice', on_delete=models.CASCADE)

class VehicleCity(models.Model):
    make = models.CharField(verbose_name="make", max_length=20)
    model = models.CharField(verbose_name="vehicle's model", max_length=20)
    make_year = models.DateField(verbose_name="made year")
    VIN = models.CharField(verbose_name="Vehicle_Identification_Number", max_length=10)
    LPN = models.CharField(verbose_name="License Plate Number", max_length=10)
    rented = models.BooleanField(default=False)
    city = models.CharField(verbose_name="city", max_length=50)
    
    vehicle_class = models.ForeignKey('VehicleClass', on_delete=models.CASCADE)
    office_info = models.ForeignKey('VehicleOffice', on_delete=models.CASCADE)


