# Generated by Django 3.2.16 on 2023-01-09 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_rename_feepays_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='fepayment',
            name='prof',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.profile'),
        ),
    ]