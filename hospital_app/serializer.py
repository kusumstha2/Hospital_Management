from rest_framework import serializers
from .models import *
from rest_framework import serializers


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name', 
            'gender',
            'date_of_birth', 
            'contact_phone',
            'contact_email',
            'address',
            'medical_history', 
            'created_at',
            'updated_at',
        )
        model = Patient
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            'name',
        )
        model=Doctor

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            'patient',
            'assigned_doctor', 
            'date',
            'time',
            'purpose',
            'status',
            'notes',
            'created_at',
            'updated_at',
            
        )  
        model=Appointment
class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            'doctor',
            'date',
            'time',
            'patient',
         )    

class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            'patient',
            'diagnosis',
            'treatment',
            'medications',
            'created_at',
            'updated_at',
        )
        model=Schedule



class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = (
            'invoice',
            'description', 
            'quantity',
            'unit_price',
            'total_amount',
        )

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            'invoice',
            'date_paid',
            'amount',
            'payment_method',
        )
class MedicalInventoryRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalInventoryRecord
        fields =(
            'item', 
            'quantity',
            'unit_price',
            'total_value', 
            'date_used',
            'quantity_used',
            'notes_usage',
            'date_incurred', 
            'amount_expense', 
            'notes_expense'
        )

class EmergencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Emergency
        fields = (
            'patient_name',
            'accident',
            'description',
            'triage_level',
            'location',
            'created_at',
            'updated_at',
        )



from rest_framework import serializers

class InvoiceSerializer(serializers.ModelSerializer):
    total_amount = serializers.SerializerMethodField()
    total_paid_amount = serializers.SerializerMethodField()
    balance_due = serializers.SerializerMethodField()
    is_fully_paid = serializers.SerializerMethodField()

    class Meta:
        model = Invoice
        fields = ['id', 'patient', 'date_created', 'due_date', 'is_paid', 'total_amount', 'total_paid_amount', 'balance_due', 'is_fully_paid']

    def get_total_amount(self, obj):
        return sum(item.total_amount() for item in obj.items.all())

    def get_total_paid_amount(self, obj):
        return sum(payment.amount for payment in obj.payments.all())

    def get_balance_due(self, obj):
        return self.get_total_amount(obj) - self.get_total_paid_amount(obj)

    def get_is_fully_paid(self, obj):
        return self.get_balance_due(obj) == 0
