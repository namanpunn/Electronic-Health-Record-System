# Generated by Django 5.0.4 on 2024-04-30 03:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ehrapp', '0007_doctor_address_doctor_emailid_doctor_licence'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='user',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='licence',
            field=models.ImageField(null=True, upload_to='ehr/static', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]),
        ),
    ]
