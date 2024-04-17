from django.urls import path
from rest_framework import routers
from .views import *
router=routers.SimpleRouter()


router.register(r'emergency',EmergencyViewSet,basename='emergency')
router.register(r'patient',PatientViewSet,basename='patient')
# router.register(r'staff',StaffViewSet,basename='staff')
router.register(r'appointment',AppointmentViewSet,basename='appointment')
router.register(r'medicalrecord',MedicalRecordViewSet,basename='medicalrecord')
router.register(r'medicalinventoryrecord',MedicalInventoryRecordViewSet,basename='medicalinventoryrecord')
router.register(r'invoice',InvoiceViewSet,basename='invoice')
router.register(r'invoiceitem',InvoiceItemViewSet,basename='invoiceitem')
router.register(r'payment',PaymentViewSet,basename='payment')
router.register(r'schedule',ScheduleViewSet,basename='schedule')

urlpatterns =router.urls+ [

]