# Generated by Django 4.1.9 on 2023-05-27 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DigitalMarketing', '0017_alter_cvideoid_videoid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VideoID', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='videoID', max_length=250)),
                ('Status', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Status', max_length=250)),
                ('userid', models.ForeignKey(db_column='userid', on_delete=django.db.models.deletion.DO_NOTHING, to='DigitalMarketing.tbuser')),
            ],
        ),
    ]