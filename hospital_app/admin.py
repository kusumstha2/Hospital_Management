from django.contrib import admin
from .models import *

# class AppointmentInline(admin.TabularInline):
#     model = Appointment
#     extra = 0

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'date_of_birth', 'contact_phone', 'contact_email']
    search_fields = ['name', 'contact_phone', 'contact_email']
    list_filter = ['gender']
    fields = ['name', 'gender', 'date_of_birth', 'contact_phone', 'contact_email', 'address', 'medical_history']
    

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'assigned_doctor','date', 'time', 'purpose', 'status', 'created_at', 'updated_at']
    list_filter = ['status']
    search_fields = ['patient__name', 'purpose']
    list_per_page = 10
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "assigned_doctor":
            kwargs["queryset"] = Staff.objects.filter(role='doctor')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

@admin.register(Staff)
class DoctorAdmin(admin.ModelAdmin):
    list_display=('name','role','specialty','contact_info','availability')
    search_fields=('contact_info','availability')
    list_filter=('specialty',)
    list_per_page=10
    list_editable = ('availability',)


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'date', 'time', 'patient')
    list_filter = ('doctor', 'date', 'time', 'patient')
    list_per_page = 5

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'diagnosis', 'treatment', 'medications', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('patient__name', 'medications')
    list_per_page = 5

class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem

class PaymentInline(admin.TabularInline):
    model = Payment

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    inlines = [InvoiceItemInline, PaymentInline]
    list_display = ['id', 'patient', 'date_created', 'due_date', 'total_paid_amount', 'balance_due', 'is_fully_paid']
    list_filter = ['is_paid']
    search_fields = ['patient__name']

@admin.register(InvoiceItem)
class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ['invoice', 'description', 'quantity', 'unit_price', 'total_amount']
    list_filter = ['invoice__patient']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['invoice', 'date_paid', 'amount', 'payment_method']
    list_filter = ['invoice__patient']

@admin.register(MedicalInventoryRecord)
class MedicalInventoryRecordAdmin(admin.ModelAdmin):
    list_display = ['item', 'quantity', 'unit_price', 'total_value', 'date_used', 'quantity_used', 'date_incurred', 'amount_expense', 'notes_expense']
    search_fields = ['item', 'date_used', 'date_incurred']
    list_filter = ['date_used', 'date_incurred']

    def total_value(self, obj):
        return obj.total_value()

    total_value.short_description = 'Total Value'

class PatientInline(admin.TabularInline):
    model = Patient
    extra = 1

@admin.register(Emergency)
class EmergencyAdmin(admin.ModelAdmin):
    list_display = ('get_patient_name', 'accident', 'triage_level', 'location', 'created_at')
    search_fields = ('patient__name', 'accident', 'triage_level', 'location')
    list_filter = ('accident', 'triage_level', 'created_at',)

    def get_patient_name(self, obj):
        return obj.patient_name if obj.patient_name else "No Patient Name"

    get_patient_name.short_description = 'Patient Name'
