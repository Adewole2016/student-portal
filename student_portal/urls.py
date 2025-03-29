"""
URL configuration for student_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
#from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.urls import path
from students.views import custom_login  # Import your custom login view
from django.contrib.auth.views import LogoutView
from django.urls import path
from students.views import custom_login  # Make sure 'studentportal' is correct



urlpatterns = [
    path("login/", custom_login, name="login"),  # Use the imported view here
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
]



urlpatterns = [
    #path("admin/", admin.site.urls),
    path('', include('students.urls')),
    path('lecturers/', include('lecturer.urls')),
    path('non_academic_staff/', include('non_academic_staff.urls')),  # Non-Academic Staff URLs
    path("login/", custom_login, name="login"),
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Define the login URL
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




