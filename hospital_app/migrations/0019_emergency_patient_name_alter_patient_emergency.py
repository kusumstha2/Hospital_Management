# Generated by Django 5.0.3 on 2024-03-30 11:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0018_rename_name_emergency_accident_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='emergency',
            name='patient_name',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='emergency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='hospital_app.emergency'),
        ),
    ]
