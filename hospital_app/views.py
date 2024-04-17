from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters
from .models import Emergency, Patient, Schedule, Appointment, MedicalRecord, Invoice, InvoiceItem, Payment, MedicalInventoryRecord
from .serializer import EmergencySerializer, PatientSerializer, ScheduleSerializer, AppointmentSerializer, MedicalRecordSerializer, InvoiceSerializer, InvoiceItemSerializer, PaymentSerializer, MedicalInventoryRecordSerializer
from .permission import isReceptionistReadOnly, isDoctororReadOnly
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class EmergencyViewSet(viewsets.ModelViewSet):
    queryset = Emergency.objects.all()
    serializer_class = EmergencySerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter,DjangoFilterBackend)
    filterset_fields = ('patient_name',)
    search_fields = ('patient_name',)

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filterset_fields = ('name',)
    search_fields = ('name',)
    permission_classes = [isReceptionistReadOnly]

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filterset_fields = ('doctor', 'date')
    search_fields = ('doctor',)

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filterset_fields = ('patient', 'assigned_doctor')
    search_fields = ('assigned_doctor',)

class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filterset_fields = ('patient', 'diagnosis',)
    search_fields = ('diagnosis',)
    permission_classes = [isDoctororReadOnly]

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all().order_by('id')
    serializer_class = InvoiceSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filterset_fields = ('patient', 'is_paid')
    search_fields = ('patient',)

class InvoiceItemViewSet(viewsets.ModelViewSet):
    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filterset_fields = ('invoice', 'quantity', 'unit_price',)
    search_fields = ('invoice',)

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filterset_fields = ('invoice', 'date_paid', 'quantity',)
    search_fields = ('invoice',)

class MedicalInventoryRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalInventoryRecord.objects.all()
    serializer_class = MedicalInventoryRecordSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filterset_fields = ('item', 'description',)
    search_fields = ('item',)
