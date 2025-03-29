from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Student, Department, Level, Course
from .forms import StudentForm, DepartmentForm, LevelForm, CourseForm

@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

@login_required
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

@login_required
def add_department(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = DepartmentForm()
    return render(request, 'add_department.html', {'form': form})

@login_required
def add_level(request):
    if request.method == "POST":
        form = LevelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = LevelForm()
    return render(request, 'add_level.html', {'form': form})

@login_required
def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

@login_required
def update_student(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'update_student.html', {'form': form, 'student': student})


@login_required
def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == "POST":
        student.delete()
        return redirect('student_list')
    return render(request, 'delete_student.html', {'student': student})


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def custom_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("student_list")  # Redirect to the student list page
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")



