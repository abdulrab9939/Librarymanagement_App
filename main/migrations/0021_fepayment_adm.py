# Generated by Django 3.2.16 on 2023-01-09 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_fepayment_prof'),
    ]

    operations = [
        migrations.AddField(
            model_name='fepayment',
            name='adm',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.admitcard'),
        ),
    ]
