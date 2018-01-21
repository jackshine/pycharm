from django import forms
from .models import *


class DailyForm(forms.ModelForm):
    class Meta:
        model = Daily
        fields = ['dailyname','daily']

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['userid','username','blogname','password','sex']