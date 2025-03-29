from django import forms
from .models import Student, Department, Level, Course

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['matric_no', 'full_name', 'age', 'department', 'level', 'passport']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']

class LevelForm(forms.ModelForm):
    class Meta:
        model = Level
        fields = ['name']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'department']
