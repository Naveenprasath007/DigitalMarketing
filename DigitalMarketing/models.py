from django.db import models
from .validators import file_size
from datetime import datetime


class Video(models.Model):
    Title=models.CharField(max_length=100)
    video=models.FileField(upload_to="video/%y/%m",validators=[file_size])
    def __str__(self):
        return self.Title

class cVideoId(models.Model):
    VideoID = models.CharField(db_column='videoID', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS') 

    def __str__(self):
        return self.VideoID
    

class Campaignquestionresponse(models.Model):
    campaignquestionid = models.ForeignKey('TbCampaignquestion', models.DO_NOTHING, db_column='CampaignQuestionID', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('TbUser', models.DO_NOTHING, db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    response = models.CharField(db_column='Response', max_length=2000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CampaignQuestionResponse'


class Campaignvideo(models.Model):
    campaignvideoid = models.CharField(db_column='CampaignVideoID', primary_key=True, max_length=255)  # Field name made lowercase.
    videoid = models.ForeignKey('TbVideo', models.DO_NOTHING, db_column='VideoID', blank=True, null=True)  # Field name made lowercase.
    campaignid = models.CharField(db_column='CampaignID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    previousvideoid = models.CharField(db_column='PreviousVideoID', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CampaignVideo'

class TbApprove(models.Model):
    userid = models.ForeignKey('TbUser', models.DO_NOTHING, db_column='UserID',primary_key=True)  # Field name made lowercase.
    videoid = models.CharField(db_column='VideoID', max_length=250)  # Field name made lowercase.
    videotitle = models.CharField(db_column='VideoTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    videopath = models.CharField(db_column='VideoPath', max_length=255, blank=True, null=True)  # Field name made lowercase.
    approveddate = models.DateTimeField(db_column='ApprovedDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_Approve'


class TbCampaignquestion(models.Model):
    campaignquestionid = models.CharField(db_column='CampaignQuestionID', primary_key=True, max_length=255)  # Field name made lowercase.
    campaignvideoid = models.ForeignKey(Campaignvideo, models.DO_NOTHING, db_column='CampaignVideoID', blank=True, null=True)  # Field name made lowercase.
    userroleid = models.ForeignKey('TbUserrole', models.DO_NOTHING, db_column='UserRoleID', blank=True, null=True)  # Field name made lowercase.
    questionid = models.ForeignKey('TbQuestion', models.DO_NOTHING, db_column='QuestionID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_CampaignQuestion'


class TbQuestion(models.Model):
    questionid = models.CharField(db_column='QuestionID', primary_key=True, max_length=255)  # Field name made lowercase.
    questiontext = models.CharField(db_column='QuestionText', max_length=2000)  # Field name made lowercase.
    questionresponse = models.CharField(db_column='QuestionResponse', max_length=4000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_Question'


class TbStatus(models.Model):
    userid = models.ForeignKey('TbUser', models.DO_NOTHING, db_column='UserID', primary_key=True)  # Field name made lowercase.
    videoid = models.CharField(db_column='VideoID', max_length=250)  # Field name made lowercase.
    reason = models.CharField(db_column='Reason', max_length=255, blank=True, null=True)  # Field name made lowercase.
    videoname = models.CharField(db_column='videoName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    approver = models.CharField(db_column='Approver', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_Status'


class TbUser(models.Model):
    userid = models.CharField(db_column='UserID', primary_key=True, max_length=255)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=250)  # Field name made lowercase.
    userroleid = models.ForeignKey('TbUserrole', models.DO_NOTHING, db_column='UserRoleID', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_User'


class TbUserrole(models.Model):
    userroleid = models.CharField(db_column='UserRoleID', primary_key=True, max_length=255)  # Field name made lowercase.
    userrolename = models.CharField(db_column='UserRoleName', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_UserRole'


class TbVideo(models.Model):
    videoid = models.CharField(db_column='VideoID', primary_key=True, max_length=255)  # Field name made lowercase.
    previousvideoid = models.CharField(db_column='PreviousVideoID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    videoname = models.CharField(db_column='VideoName', max_length=2000)  # Field name made lowercase.
    videopath = models.CharField(db_column='VideoPath', max_length=2000)  # Field name made lowercase.
    videotranscription = models.TextField(db_column='VideoTranscription')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_Video'