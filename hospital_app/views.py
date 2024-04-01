from .serializer import *
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django_filters import rest_framework as filter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
# Create your views here.
from rest_framework import status

class EmergencyViewset(viewsets.ModelViewSet):
    queryset=Emergency.objects.all()
    serializer_class=EmergencySerializer
    pagination_class=PageNumberPagination
    filter_backends=(filters.SearchFilter,filter.DjangoFilterBackend)
    filterset_fields =('patient_name',)
    search_fields=('patient_name',)

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers
    pagination_class=PageNumberPagination
    filter_backends=(filters.SearchFilter,filter.DjangoFilterBackend)
    filterset_fields=('name',) 
    search_fields=('name',)

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    pagination_class=PageNumberPagination
    filter_backends=(filters.SearchFilter,filter.DjangoFilterBackend)
    filterset_fields=('doctor','date') 
    search_fields=('doctor',)

        

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    pagination_class=PageNumberPagination
    filter_backends=(filters.SearchFilter,filter.DjangoFilterBackend)
    filterset_fields=('name','role',) 
    search_fields=('availability',)

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    pagination_class=PageNumberPagination
    filter_backends=(filters.SearchFilter,filter.DjangoFilterBackend)
    filterset_fields=('patient',' assigned_doctor') 
    search_fields=('assigned_doctor',)


class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    pagination_class=PageNumberPagination
    filter_backends=(filters.SearchFilter,filter.DjangoFilterBackend)
    filterset_fields=('patient','diagnosis',) 
    search_fields=('diagnosis',)

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    pagination_class=PageNumberPagination
    filter_backends=(filters.SearchFilter,filter.DjangoFilterBackend)
    filterset_fields=('patient','is_paid') 
    search_fields=('patient',)

class InvoiceItemViewSet(viewsets.ModelViewSet):
    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemSerializer
    pagination_class=PageNumberPagination
    filter_backends=(filters.SearchFilter,filter.DjangoFilterBackend)
    filterset_fields=('invoice','quantity','unit_price',) 
    search_fields=('invoice',)

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    pagination_class=PageNumberPagination
    filter_backends=(filters.SearchFilter,filter.DjangoFilterBackend)
    filterset_fields=('invoice','date_paid','quantity',) 
    search_fields=('invoice',)

class MedicalInventoryRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalInventoryRecord.objects.all()
    serializer_class = MedicalInventoryRecordSerializer  
    pagination_class=PageNumberPagination
    filter_backends=(filters.SearchFilter,filter.DjangoFilterBackend)
    filterset_fields=('item','description') 
    search_fields=('item',)          

      


