# Generated by Django 3.2.16 on 2023-01-09 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_fepayment_enl'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feepay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuname', models.CharField(max_length=90, null=True)),
                ('sten', models.CharField(max_length=90, null=True)),
                ('stemail', models.CharField(max_length=90, null=True)),
                ('stcon', models.IntegerField(null=True)),
                ('stbranch', models.CharField(max_length=90, null=True)),
                ('stdob', models.DateField()),
                ('stfee', models.IntegerField(null=True)),
                ('stfeex', models.IntegerField(null=True)),
                ('sttotalfee', models.IntegerField(null=True)),
                ('penaltyfee', models.IntegerField(null=True)),
            ],
        ),
    ]
