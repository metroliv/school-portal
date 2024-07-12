from django import forms
from django.contrib.auth.models import User
from .models import Group, GroupMessage

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'members']

class GroupMessageForm(forms.ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['content']
