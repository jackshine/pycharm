from django import forms

from pycharm.django.BlogProject.myblog.model.models import *


class DailyForm(forms.ModelForm):
    class Meta:
        model = Daily
        fields = ['dailyname','daily']