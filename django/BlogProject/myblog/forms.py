from django import forms
from django.forms import fields
from .models import *

class DailyForm(forms.ModelForm):
    class Meta:
        model = Daily
        fields = ['dailyname','daily']