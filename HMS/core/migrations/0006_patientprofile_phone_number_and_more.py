# Generated by Django 4.1.5 on 2023-09-30 14:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_alter_patientprofile_birthdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientprofile',
            name='phone_number',
            field=models.IntegerField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='patientprofile',
            name='birthdate',
            field=models.DateField(default=datetime.date(2023, 9, 30)),
        ),
        migrations.CreateModel(
            name='DoctorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField()),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('phone_number', models.IntegerField(default=0, max_length=10)),
                ('height', models.IntegerField(default=1)),
                ('weight', models.IntegerField(default=1)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=6)),
                ('bloodgroup', models.CharField(choices=[('OP', 'O +ve'), ('ON', 'O -ve'), ('AP', 'A +ve'), ('AN', 'A -ve'), ('BP', 'B +ve'), ('BN', 'B -ve'), ('ABP', 'AB +ve'), ('ABN', 'AB -ve')], default='OP', max_length=6)),
                ('birthdate', models.DateField(default=datetime.date(2023, 9, 30))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]