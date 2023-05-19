# Generated by Django 4.1.9 on 2023-05-16 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DigitalMarketing', '0010_campaignvideo_tbcampaignquestion'),
    ]

    operations = [
        migrations.CreateModel(
            name='TbQuestion',
            fields=[
                ('questionid', models.IntegerField(db_column='QuestionID', primary_key=True, serialize=False)),
                ('questiontext', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='QuestionText', max_length=2000)),
                ('questionresponse', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='QuestionResponse', max_length=4000)),
            ],
            options={
                'db_table': 'tb_Question',
                'managed': False,
            },
        ),
    ]