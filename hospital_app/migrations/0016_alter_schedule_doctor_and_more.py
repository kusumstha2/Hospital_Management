# Generated by Django 5.0.3 on 2024-03-27 06:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0015_remove_appointment_emergency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_app.staff'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='assigned_doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital_app.staff'),
        ),
        migrations.AddField(
            model_name='staff',
            name='role',
            field=models.CharField(choices=[('doctor', 'Doctor'), ('nurse', 'Nurse'), ('reception', 'Receptionist'), ('cleaner', 'Cleaner')], default='receptionist', max_length=20),
        ),
        migrations.AddField(
            model_name='staff',
            name='specialty',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='contact_info',
            field=models.CharField(max_length=10),
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
    ]
