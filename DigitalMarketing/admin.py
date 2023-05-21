from django.contrib import admin
from .models import Video,TbVideo,Campaignvideo,TbCampaignquestion,TbQuestion,Campaignquestionresponse
# Register your models here.

admin.site.register(Video)
# admin.site.register(video_details)
admin.site.register(TbVideo)
admin.site.register(Campaignvideo)
admin.site.register(TbCampaignquestion)
admin.site.register(TbQuestion)
admin.site.register(Campaignquestionresponse)
