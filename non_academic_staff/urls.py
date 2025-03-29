from django.urls import path
from .views import non_academic_staff_list, add_non_academic_staff, update_non_academic_staff, delete_non_academic_staff



urlpatterns = [
    path('', non_academic_staff_list, name='non_academic_staff_list'),
    path('add/', add_non_academic_staff, name='add_non_academic_staff'),

    path('update/<int:id>/', update_non_academic_staff, name='update_non_academic_staff'),
    path('delete/<int:id>/', delete_non_academic_staff, name='delete_non_academic_staff'),  # Ensure 'id' is used
]
