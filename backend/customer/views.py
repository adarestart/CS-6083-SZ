from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import IndividualSerializer,CorporationSerializer
from .models import IndividualInfo,CorporationUser

# Create your views here.
class IndividualView(APIView):
    def get(self, request):
        vehicles = IndividualInfo.objects.all()
        serializer = IndividualSerializer(vehicles, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    def post(self, request):  
        print(request.data)
        serializer = IndividualSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CorporationView(APIView):
    def get(self, request):
        vehicles = CorporationUser.objects.all()
        serializer = CorporationSerializer(vehicles, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    def post(self, request):  
        print(request.data)
        serializer = CorporationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
     
 
