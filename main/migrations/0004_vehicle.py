# Generated by Django 3.2.16 on 2022-12-25 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_sciencee_student_science'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parkingnumber', models.CharField(max_length=20)),
                ('vehiclecompany', models.CharField(max_length=50)),
                ('regno', models.CharField(max_length=10)),
                ('ownername', models.CharField(max_length=50)),
                ('ownercontact', models.CharField(max_length=15)),
                ('pdate', models.DateField()),
                ('intime', models.CharField(max_length=50)),
                ('outtime', models.CharField(max_length=50)),
                ('parkingcharge', models.CharField(max_length=50)),
                ('remark', models.CharField(max_length=500)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]