from .models import TbQuestion,TbUserrole,TbUser
from django import forms




class Question(forms.ModelForm):
    class Meta:
        model=TbQuestion
        fields='__all__'

class userRole(forms.ModelForm):
    class Meta:
        model=TbUserrole
        fields='__all__'
        

class User(forms.ModelForm):
    class Meta:
        model=TbUser
        fields='__all__'
        