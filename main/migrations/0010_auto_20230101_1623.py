# Generated by Django 3.2.16 on 2023-01-01 10:53

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_fepayment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fepayment',
            name='dat',
        ),
        migrations.AddField(
            model_name='fepayment',
            name='issuedate',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='fepayment',
            name='expiredate',
            field=models.DateField(default=main.models.get_expiry),
        ),
    ]
