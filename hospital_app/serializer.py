from rest_framework import serializers
from .models import *
class PatientSerializers(serializers.ModelSerializer):
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


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            'patient', 
            'date',
            'time',
            'purpose',
            'status',
            'notes',
            'created_at',
            'updated_at',
            
        )  
        model=Appointment
       
# class DoctorSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields=(
#             'name',
#             'specialty',
#             'contact_info',
#             'availability',
            
#              )   
#         model=Doctor 

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            'name',
            'contact_info',
            'availability',
            ) 
        model=Staff 

# class PatientAppointmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields=(
#             'name', 
#             'assigned_doctor',
#         )
#         model = Patient_Appointment

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

# class TriageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Triage
#         fields = (
#             'patient',
#             'emergency', 
#             'triage_level', 
#             'triage_time',
#         )     

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = (
          'id', 
          'patient', 
          'date_created',
          'due_date', 
          'total_paid_amount',
          'balance_due', 
          'is_fully_paid',
        )           
                  
                       
              
        