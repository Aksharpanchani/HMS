# Generated by Django 4.1.5 on 2023-11-10 10:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_remove_patientprofile_weight_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='report',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
    ]