# Generated by Django 4.1.9 on 2023-06-03 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DigitalMarketing', '0002_cvideoid_video'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AuthGroup',
        ),
        migrations.DeleteModel(
            name='AuthGroupPermissions',
        ),
        migrations.DeleteModel(
            name='AuthPermission',
        ),
        migrations.DeleteModel(
            name='AuthUser',
        ),
        migrations.DeleteModel(
            name='AuthUserGroups',
        ),
        migrations.DeleteModel(
            name='AuthUserUserPermissions',
        ),
        migrations.DeleteModel(
            name='Campaignquestionresponse',
        ),
        migrations.DeleteModel(
            name='Campaignvideo',
        ),
        migrations.DeleteModel(
            name='DjangoAdminLog',
        ),
        migrations.DeleteModel(
            name='DjangoContentType',
        ),
        migrations.DeleteModel(
            name='DjangoMigrations',
        ),
        migrations.DeleteModel(
            name='DjangoSession',
        ),
        migrations.DeleteModel(
            name='Sysdiagrams',
        ),
        migrations.DeleteModel(
            name='TbApprove',
        ),
        migrations.DeleteModel(
            name='TbCampaignquestion',
        ),
        migrations.DeleteModel(
            name='TbQuestion',
        ),
        migrations.DeleteModel(
            name='TbStatus',
        ),
        migrations.DeleteModel(
            name='TbUser',
        ),
        migrations.DeleteModel(
            name='TbUserrole',
        ),
        migrations.DeleteModel(
            name='TbVideo',
        ),
    ]
