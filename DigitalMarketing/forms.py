from .models import Video,TbQuestion
from django import forms

class Video_form(forms.ModelForm):
    class Meta:
        model=Video
        fields=("Title","video",)

        widgets ={
            'Title':forms.TextInput(attrs={'class':'form-control'}),
        }
# class video_detail(forms.ModelForm):
#     class Meta:
#         # model=video_details
#         fields=("quality","complaint",)

#         widgets ={
#             'Title':forms.TextInput(attrs={'class':'form-control'}),
#             "quality":forms.TextInput(attrs={'class':'form-control'}),
#             "complaint":forms.TextInput(attrs={'class':'form-control'}),
#         }

class Question(forms.ModelForm):
    class Meta:
        model=TbQuestion
        fields='__all__'
        