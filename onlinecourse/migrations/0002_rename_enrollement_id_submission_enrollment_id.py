# Generated by Django 4.1.7 on 2023-03-05 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='enrollement_id',
            new_name='enrollment_id',
        ),
    ]
