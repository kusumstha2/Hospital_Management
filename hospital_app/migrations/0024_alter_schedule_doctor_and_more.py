# Generated by Django 5.0.3 on 2024-04-18 04:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0023_alter_staff_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_app.user'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='assigned_doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staff', to='hospital_app.user'),
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
    ]
