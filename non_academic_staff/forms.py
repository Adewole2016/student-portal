from django import forms
from .models import Non_Academic_Staff

class Non_Academic_StaffForm(forms.ModelForm):
    class Meta:
        model = Non_Academic_Staff
        fields = ['first_name', 'last_name', 'email', 'phone', 'department', 'passport']
        widgets = {
            'passport': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }  # <-- Closing brace added here
