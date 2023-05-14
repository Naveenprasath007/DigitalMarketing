from django.db import models
from .validators import file_size
# Create your models here.


class Video(models.Model):
    Title=models.CharField(max_length=100)
    video=models.FileField(upload_to="video/%m/%y",validators=[file_size])
    def __str__(self):
        return self.Title
    
class video_details(models.Model):
    Title=models.CharField(max_length=100)
    video=models.FileField(upload_to="video/%m/%y",validators=[file_size])
    quality=models.BooleanField()
    qualitycommmand=models.CharField(max_length=100)
    complaint=models.BooleanField()
    complaintcommand=models.CharField(max_length=100)
    transcribe=models.CharField(max_length=1000)
    def __str__(self):
        return self.Title