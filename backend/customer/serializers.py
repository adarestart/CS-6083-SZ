from rest_framework import serializers
from .models import IndividualInfo,CorporationUser

class IndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualInfo
        fields = '__all__'


class CorporationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CorporationUser
        fields = '__all__'