# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class DigitalmarketingCvideoid(models.Model):
    id = models.BigAutoField(primary_key=True)
    videoid = models.CharField(db_column='videoID', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DigitalMarketing_cvideoid'


class DigitalmarketingVideo(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(db_column='Title', max_length=100)  # Field name made lowercase.
    video = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'DigitalMarketing_video'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class TbApprove(models.Model):
    userid = models.ForeignKey('TbUser', models.DO_NOTHING, db_column='UserID', blank=True, null=True)  # Field name made lowercase.
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
    userid = models.ForeignKey('TbUser', models.DO_NOTHING, db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    videoid = models.CharField(db_column='VideoID', max_length=250)  # Field name made lowercase.
    reason = models.CharField(db_column='Reason', max_length=255, blank=True, null=True)  # Field name made lowercase.
    videoname = models.CharField(db_column='videoName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    approver = models.CharField(db_column='Approver', max_length=255, blank=True, null=True)  # Field name made lowercase.
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
