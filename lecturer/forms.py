from django import forms
from .models import Lecturer

class LecturerForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = ['first_name', 'last_name', 'email', 'phone', 'department', 'courses_taught', 'passport']
        widgets = {
            'passport': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }
