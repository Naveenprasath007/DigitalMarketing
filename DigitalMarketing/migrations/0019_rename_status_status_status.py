# Generated by Django 4.1.9 on 2023-05-27 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DigitalMarketing', '0018_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='status',
            old_name='Status',
            new_name='status',
        ),
    ]