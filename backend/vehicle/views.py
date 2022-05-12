from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import VehicleCitySerializer,VehicleFullSerializer,OfficeSerializer,ClassSerializer,VehicleSerializer
from .models import VehicleClass, VehicleInfo, VehicleOffice



class VehicleView(APIView):
    def get(self, request):
        vehicles = VehicleInfo.objects.raw('SELECT * FROM vehicle_vehicleinfo JOIN vehicle_vehicleoffice ON vehicle_vehicleinfo.office_info_id = vehicle_vehicleoffice.id WHERE rented =0;') 
        serializer = VehicleCitySerializer(vehicles, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
class VehicleInfoView(APIView):
    def get(self, request):
        vehicles = VehicleInfo.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    def post(self, request):  
        print(request.data)
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SingleVehicleView(APIView):
    def get(self, request,vehicle_id):
        vehicles = VehicleInfo.objects.filter(id=vehicle_id)
        serializer = VehicleSerializer(vehicles, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    def put(self, request,vehicle_id):  
        print(request.data)
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request,vehicle_id):
        vehicles = VehicleInfo.objects.get(id=vehicle_id)
        vehicles.delete()
        return Response({"status": "success"}, status=status.HTTP_200_OK)
    


    
class VehicleFullView(APIView):
    def get(self, request,vehicle_id):
        if vehicle_id is not None:
            vehicles = VehicleInfo.objects.raw('SELECT * FROM vehicle_vehicleinfo JOIN vehicle_vehicleclass JOIN vehicle_vehicleoffice ON vehicle_vehicleinfo.vehicle_class_id = vehicle_vehicleclass.id AND vehicle_vehicleinfo.office_info_id = vehicle_vehicleoffice.id WHERE vehicle_vehicleinfo.id = %s;',[vehicle_id]) 
            serializer = VehicleFullSerializer(vehicles, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            vehicles =[]
            serializer = VehicleFullSerializer(vehicles, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
        
class VehicleOfficeView(APIView):
    def get(self, request):
        vehicles = VehicleOffice.objects.raw('SELECT * FROM vehicle_vehicleoffice;') 
        serializer = OfficeSerializer(vehicles, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    def post(self, request):  
        print(request.data)
        serializer = OfficeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class VehicleClassView(APIView):
    def get(self, request):
        vehicles = VehicleClass.objects.raw('SELECT * FROM vehicle_vehicleclass;') 
        serializer = ClassSerializer(vehicles, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    def post(self, request):  
        print(request.data)
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
 