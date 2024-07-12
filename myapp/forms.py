from django import forms
from django.contrib.auth import get_user_model
from .models import Staff, UserProfile

User = get_user_model()

class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']  # Add other fields as necessary

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'age', 'email', 'phone', 'location', 'hobby', 'gender']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Staff.objects.filter(email=email).exists():
            raise forms.ValidationError("A staff member with this email already exists.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if Staff.objects.filter(phone=phone).exists():
            raise forms.ValidationError("A staff member with this phone number already exists.")
        return phone

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_image']
