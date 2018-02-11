from django import forms
from .models import *


class DailyForm(forms.ModelForm):
    class Meta:
        model = Daily
        fields = ['title','body']

class UserInfoLoginForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['username','password']


class UserInfoRegisterForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['username','password']