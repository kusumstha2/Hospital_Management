from django.db import models
from django.contrib.auth.models import User
from datetime import time,date
from django.utils import timezone


# Create your models here.

    
class Emergency(models.Model):
    # patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='emergencies',default=1)
    patient_name= models.CharField(max_length=25,null=True,blank=True)
    accident = models.CharField(max_length=255)
    description = models.TextField()
    TRIAGE_LEVEL_CHOICES = [
        ('1', 'Immediate'),
        ('2', 'Delayed'),
        ('3', 'Minimal'),
        ('4', 'Expectant'),
    ]

    triage_level = models.CharField(max_length=1, choices=TRIAGE_LEVEL_CHOICES,default='1')
    created_at = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.accident
  
class Patient(models.Model):
    GENDER_CHOICES =[
        ('M','Male'),
        ('F','Female'),
        ('O','Other'),
        ]
     
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES)
    date_of_birth =models.DateField(null=True,blank=True)
    contact_phone=models.CharField(max_length=10,blank=True,null=True)
    contact_email=models.EmailField(blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    medical_history=models.TextField(blank=True,null=True)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    emergency = models.ForeignKey(Emergency, on_delete=models.CASCADE,null=True,blank=True,related_name='patient')
    @property
    def age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
    def __str__(self):
        return self.name
    
class Staff(models.Model):
    AVAILABILITY_CHOICE=[
        ('available', 'Available'),
        ('busy', 'Busy'),
        ('on_leave', 'On Leave'),
    ]
    ROLE=[('doctor','Doctor'),
          ('nurse','Nurse'),
          ('reception','Receptionist'),
          ('cleaner','Cleaner')]
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=10)
    role = models.CharField(max_length=20,choices = ROLE, default ='reception')
    specialty = models.CharField(max_length=100,null =True,blank = True)
    availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICE, default='available')

    def __str__(self):
        return f"{self.name}-{self.availability}"     
    
class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Cancelled', 'Cancelled'),
        ('Completed', 'Completed'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    assigned_doctor = models.ForeignKey(Staff, on_delete=models.CASCADE,null=True,blank=True, related_name='staff')
    date = models.DateField()
    time = models.TimeField()
    purpose = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Scheduled')
    notes = models.TextField(blank=True, null=True)
    # emergency = models.ForeignKey(Emergency, on_delete=models.CASCADE, related_name='appointments',default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient.name}'s appointment on {self.date} at {self.time}"    


# class Staff(models.Model):
#     AVAILABILITY_CHOICE=[
#         ('available', 'Available'),
#         ('busy', 'Busy'),
#         ('on_leave', 'On Leave'),
#     ]
#     name = models.CharField(max_length=100)
#     contact_info = models.CharField(max_length=100)
#     availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICE, default='available')
    
#     def __str__(self):
#         return f"{self.name}-{self.availability}"

    

       
# class Patient_Appointment(models.Model):
#     name = models.CharField(max_length=100)
#     assigned_doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)

#     def __str__(self):
#         return self.name

class Schedule(models.Model):
    doctor = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date} - {self.time} - {self.doctor}"  
     
class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    treatment = models.TextField()
    medications = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
 
    def __str__(self):
        return f"{self.patient}'s Medical Record"
    #permission garne baki ca
    # view, update, add,delete wala permission
 
class Invoice(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)   
    date_created=models.DateTimeField(default=timezone.now) 
    due_date=models.DateField()
    is_paid=models.BooleanField(default=False)
    
    def total_amount(self):
        return sum(item.total_amount()for item in self.items.all())
    
    
    def total_paid_amount(self):
        return sum(payment.amount for payment in self.payments.all())
    
    def balance_due(self):
        return self.total_amount() - self.total_paid_amount()

    def is_fully_paid(self):
        return self.balance_due() == 0
    
    def __str__(self):
        return f"Invoice #{self.pk} - {self.patient} - Total: {self.total_amount()} - Due: {self.due_date}"

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def total_amount(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return f"{self.description} - Quantity: {self.quantity} - Total: {self.total_amount()}"

class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='payments', on_delete=models.CASCADE)
    date_paid = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=100)

    def __str__(self):
        return f"Payment for Invoice #{self.invoice.pk} - {self.amount} - Method: {self.payment_method}"   

class MedicalInventoryRecord(models.Model):
    item = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    quantity = models.IntegerField(default=0)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    date_used = models.DateTimeField(default=timezone.now)
    quantity_used = models.IntegerField(default=0)
    notes_usage = models.TextField(blank=True)
    date_incurred = models.DateTimeField(default=timezone.now)
    amount_expense = models.DecimalField(max_digits=10, decimal_places=2)
    notes_expense = models.TextField(blank=True)

    def total_value(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return f"{self.item} - Quantity: {self.quantity}, Unit Price: {self.unit_price}, Total Value: {self.total_value()}, Date Used: {self.date_used}, Quantity Used: {self.quantity_used}, Date Incurred: {self.date_incurred}, Amount Incurred: {self.amount_expense}"

