from django.db import models
from .validators import file_size
from datetime import datetime
# Create your models here.


class Video(models.Model):
    Title=models.CharField(max_length=100)
    video=models.FileField(upload_to="video/%m/%y",validators=[file_size])
    def __str__(self):
        return self.Title
    
# class video_details(models.Model):
#     Title=models.CharField(max_length=100)
#     video=models.FileField(upload_to="video/%m/%y",validators=[file_size])
#     quality=models.BooleanField()
#     qualitycommmand=models.CharField(max_length=100)
#     complaint=models.BooleanField()
#     complaintcommand=models.CharField(max_length=100)
#     transcribe=models.CharField(max_length=1000)
#     def __str__(self):
#         return self.Title
    
class TbVideo(models.Model):
    videoid = models.CharField(max_length=100,db_column='VideoID', primary_key=True)  # Field name made lowercase.
    previousvideoid = models.IntegerField(db_column='PreviousVideoID')  # Field name made lowercase.
    videoname = models.CharField(db_column='VideoName', max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    videopath = models.CharField(db_column='VideoPath', max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    videotranscription = models.TextField(db_column='VideoTranscription', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_Video'

    def __str__(self):
        return self.videoname
    

# class Campaignvideo(models.Model):
#     campaignvideoid = models.CharField(db_column='CampaignVideoID',max_length=100, primary_key=True)  # Field name made lowercase.
#     videoid = models.ForeignKey('TbVideo', models.DO_NOTHING, db_column='VideoID')  # Field name made lowercase.
#     campaignid = models.CharField(db_column='CampaignID',max_length=100)  # Field name made lowercase.
#     previousvideoid = models.CharField(db_column='PreviousVideoID',max_length=100,)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CampaignVideo'
    
#     def __str__(self):
#         return self.campaignvideoid


class Campaignvideo(models.Model):
    campaignvideoid = models.CharField(db_column='CampaignVideoID', primary_key=True, max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    videoid = models.ForeignKey('TbVideo', models.DO_NOTHING, db_column='VideoID')  # Field name made lowercase.
    campaignid = models.CharField(db_column='CampaignID', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    previousvideoid = models.CharField(db_column='PreviousVideoID', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CampaignVideo'

    def __str__(self):
        return self.campaignvideoid




class TbQuestion(models.Model):
    questionid = models.IntegerField(db_column='QuestionID', primary_key=True)  # Field name made lowercase.
    questiontext = models.CharField(db_column='QuestionText', max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    questionresponse = models.CharField(db_column='QuestionResponse', max_length=4000, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_Question'

    def __int__(self):
        return self.questionid
    

# class TbCampaignquestion(models.Model):
#     campaignquestionid = models.CharField(db_column='CampaignQuestionID',max_length=100, primary_key=True)  # Field name made lowercase.
#     campaignvideoid = models.CharField(Campaignvideo,db_column='CampaignVideoID',max_length=100,)  # Field name made lowercase.
#     userroleid = models.CharField(models.DO_NOTHING,db_column='UserRoleID',max_length=100)  # Field name made lowercase.
#     # questionid = models.IntegerField(db_column='QuestionID')  # Field name made lowercase.
#     questionid = models.ForeignKey(TbQuestion, models.DO_NOTHING, db_column='QuestionID')

#     class Meta:
#         managed = False
#         db_table = 'tb_CampaignQuestion'
#     def __str__(self):
#         return self.campaignquestionid
    
class TbCampaignquestion(models.Model):
    campaignquestionid = models.CharField(db_column='CampaignQuestionID', primary_key=True, max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    campaignvideoid = models.ForeignKey(Campaignvideo, models.DO_NOTHING, db_column='CampaignVideoID')  # Field name made lowercase.
    userroleid = models.ForeignKey('TbUserrole', models.DO_NOTHING, db_column='UserRoleID', blank=True, null=True)  # Field name made lowercase.
    questionid = models.ForeignKey('TbQuestion', models.DO_NOTHING, db_column='QuestionID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_CampaignQuestion'

    def __int__(self):
        return self.campaignquestionid
    


class TbUser(models.Model):
    userid = models.CharField(db_column='UserID',max_length=250, primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    userroleid = models.ForeignKey('TbUserrole', models.DO_NOTHING, db_column='UserRoleID')  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'tb_User'

    def __int__(self):
        return self.userid

class Campaignquestionresponse(models.Model):
    campaignquestionid = models.ForeignKey('TbCampaignquestion', models.DO_NOTHING, db_column='CampaignQuestionID')  # Field name made lowercase.
    userid = models.ForeignKey('TbUser',models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    response = models.CharField(db_column='Response', max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CampaignQuestionResponse'

    def __int__(self):
        return self.response




class TbUserrole(models.Model):
    userroleid = models.CharField(db_column='UserRoleID',max_length=250, primary_key=True)  # Field name made lowercase.
    userrolename = models.CharField(db_column='UserRoleName', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_UserRole'

    def __str__(self):
        return self.userrolename
    


class cVideoId(models.Model):
    VideoID = models.CharField(db_column='videoID', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS') 

    def __str__(self):
        return self.VideoID
    

class Status(models.Model):
    userid = models.ForeignKey(TbUser,models.DO_NOTHING, db_column='userid') 
    VideoID = models.CharField(db_column='videoID', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS')
    status = models.CharField(db_column='Status', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS')
    reason = models.CharField(db_column='Reason',max_length=250,null=True,blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS')
    date =  models.DateField(default=datetime.now)
    def __str__(self):
        return self.VideoID
    
class Approve(models.Model):
    userid = models.ForeignKey(TbUser,models.DO_NOTHING, db_column='userid') 
    VideoID = models.CharField(db_column='videoID', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS')
    VideoTitle = models.CharField(db_column='videoTitle', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS')
    VideoPath = models.CharField(db_column='videoPath', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS')
    approvedDate =  models.DateField(default=datetime.now)
    def __str__(self):
        return self.VideoID