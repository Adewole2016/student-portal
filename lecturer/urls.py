from django.urls import path
from .views import lecturer_list, add_lecturer, update_lecturer, delete_lecturer

urlpatterns = [
    path('', lecturer_list, name='lecturer_list'),
    path('add/', add_lecturer, name='add_lecturer'),
    path('update/<int:id>/', update_lecturer, name='update_lecturer'),
    path('delete/<int:id>/', delete_lecturer, name='delete_lecturer'),  # Ensure 'id' is used
]
