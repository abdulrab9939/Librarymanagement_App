# Generated by Django 3.2.16 on 2022-12-24 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_science_student_sciencee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='sciencee',
            new_name='science',
        ),
    ]