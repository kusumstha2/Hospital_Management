# Generated by Django 5.0.3 on 2024-03-26 16:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0012_remove_triage_emergency_remove_triage_patient_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emergency',
            name='patient_name',
        ),
        migrations.AddField(
            model_name='appointment',
            name='emergency',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='hospital_app.emergency'),
        ),
        migrations.AddField(
            model_name='emergency',
            name='patient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='emergencies', to='hospital_app.patient'),
        ),
    ]