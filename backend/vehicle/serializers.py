from rest_framework import serializers
from .models import VehicleClass, VehicleInfo, VehicleOffice, VehicleFullInfo, VehicleCity

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleClass
        fields = ('id', 'class_type','daily_rate','extra_rate')

class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleOffice
        fields = ('id', 'street','city','state','zipcode','phone')

class VehicleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VehicleInfo
        fields = ('id', 'make','model','make_year','VIN','LPN','rented','vehicle_class','office_info')

class VehicleFullSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VehicleFullInfo
        #fields = ('id', 'make','model','make_year','VIN','LPN','vehicle_class','office_info','class_type','daily_rate','extra_rate')
        fields = ('id', 'make','model','make_year','VIN','LPN','vehicle_class','office_info','class_type','daily_rate','extra_rate','street','city','state','zipcode','phone')


class VehicleCitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VehicleCity
        fields = ('id', 'make','model','make_year','VIN','LPN','city','vehicle_class','office_info')
