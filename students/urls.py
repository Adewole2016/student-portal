from django.urls import path
from .views import student_list, add_student, add_department, add_level, add_course, update_student, delete_student

urlpatterns = [
    path('', student_list, name='student_list'),
    path('add-student/', add_student, name='add_student'),
    path('add-department/', add_department, name='add_department'),
    path('add-level/', add_level, name='add_level'),
    path('add-course/', add_course, name='add_course'),
    path('students/update/<int:student_id>/', update_student, name='update_student'),
    path('students/delete/<int:student_id>/', delete_student, name='delete_student'),
]
