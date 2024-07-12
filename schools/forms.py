from django import forms
from django.contrib.auth import get_user_model
from .models import School, Class, Stream, Student

User = get_user_model()


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['name', 'address']

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name']

class StreamForm(forms.ModelForm):
    class Meta:
        model = Stream
        fields = ['name']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'date_of_birth', 'stream']
