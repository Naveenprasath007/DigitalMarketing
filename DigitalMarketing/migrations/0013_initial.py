# Generated by Django 4.1.9 on 2023-05-17 10:18

import DigitalMarketing.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('DigitalMarketing', '0012_delete_video_delete_campaignvideo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaignvideo',
            fields=[
                ('campaignvideoid', models.CharField(db_column='CampaignVideoID', max_length=100, primary_key=True, serialize=False)),
                ('campaignid', models.CharField(db_column='CampaignID', max_length=100)),
                ('previousvideoid', models.CharField(db_column='PreviousVideoID', max_length=100)),
            ],
            options={
                'db_table': 'CampaignVideo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbCampaignquestion',
            fields=[
                ('campaignquestionid', models.CharField(db_column='CampaignQuestionID', max_length=100, primary_key=True, serialize=False)),
                ('userroleid', models.IntegerField(db_column='UserRoleID')),
                ('questionid', models.IntegerField(db_column='QuestionID')),
            ],
            options={
                'db_table': 'tb_CampaignQuestion',
                'managed': False,
            },
        ),
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
        migrations.CreateModel(
            name='TbVideo',
            fields=[
                ('videoid', models.CharField(db_column='VideoID', max_length=100, primary_key=True, serialize=False)),
                ('previousvideoid', models.IntegerField(db_column='PreviousVideoID')),
                ('videoname', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='VideoName', max_length=2000)),
                ('videopath', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='VideoPath', max_length=2000)),
                ('videotranscription', models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='VideoTranscription')),
            ],
            options={
                'db_table': 'tb_Video',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('video', models.FileField(upload_to='video/%m/%y', validators=[DigitalMarketing.validators.file_size])),
            ],
        ),
    ]
