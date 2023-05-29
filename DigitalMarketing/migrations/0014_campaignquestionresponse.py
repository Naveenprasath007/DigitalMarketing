# Generated by Django 4.1.9 on 2023-05-19 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DigitalMarketing', '0013_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaignquestionresponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField(db_column='UserID')),
                ('response', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Response', max_length=2000)),
            ],
            options={
                'db_table': 'CampaignQuestionResponse',
                'managed': False,
            },
        ),
    ]