from django import forms
from django.forms import fields
class UserForm(forms.Form):
    mobile = fields.CharField(label='手机号',max_length=16)
    password = fields.CharField(label='密码',max_length=32)