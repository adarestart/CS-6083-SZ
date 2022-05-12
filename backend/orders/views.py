from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OrderSerializer,InvoiceSerializer,PaymentSerializer
from .models import OrderInfo,OrderPayment,OrderInvoice

# Create your views here.
class OrderView(APIView):
    def get(self, request):
        vehicles = OrderInfo.objects.all()
        serializer = OrderSerializer(vehicles, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    def post(self, request):  
        print(request.data)
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SingleOrderView(APIView):
    def get(self, request,order_id):
        vehicles = OrderInfo.objects.filter(id=order_id)
        serializer = OrderSerializer(vehicles, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
    def put(self, request,order_id):  
        print(request.data)
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request,order_id):
        print("delete: "+str(order_id))
        vehicles = OrderInfo.objects.get(id=order_id)
        vehicles.delete()
        return Response({"status": "success"}, status=status.HTTP_200_OK)
    
  
class InvoiceView(APIView):
    def get(self, request):
        vehicles = OrderInvoice.objects.all()
        serializer = InvoiceSerializer(vehicles, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    def post(self, request):  
        print(request.data)
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SingleInvoiceView(APIView):
    def get(self, request,order_id):
        vehicles = OrderInvoice.objects.filter(id=order_id)
        serializer = InvoiceSerializer(vehicles, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
    def put(self, request,order_id):  
        print(request.data)
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request,order_id):
        print("delete: "+str(order_id))
        vehicles = OrderInvoice.objects.get(id=order_id)
        vehicles.delete()
        return Response({"status": "success"}, status=status.HTTP_200_OK)
     
class PaymentView(APIView):
    def get(self, request):
        vehicles = OrderPayment.objects.all()
        serializer = PaymentSerializer(vehicles, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    def post(self, request):  
        print(request.data)
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SinglePaymentView(APIView):
    def get(self, request,order_id):
        vehicles = OrderPayment.objects.filter(id=order_id)
        serializer = PaymentSerializer(vehicles, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
    def put(self, request,order_id):  
        print(request.data)
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request,order_id):
        print("delete: "+str(order_id))
        vehicles = OrderPayment.objects.get(id=order_id)
        vehicles.delete()
        return Response({"status": "success"}, status=status.HTTP_200_OK)
    



