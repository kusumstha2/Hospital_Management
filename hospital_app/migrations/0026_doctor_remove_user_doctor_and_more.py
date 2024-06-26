# Generated by Django 5.0.3 on 2024-04-18 05:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0025_user_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='doctor',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='assigned_doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staff', to='hospital_app.doctor'),
        ),
    ]
