from django.shortcuts import render, redirect, get_object_or_404
from .models import Non_Academic_Staff
from .forms import Non_Academic_StaffForm


def non_academic_staff_list(request):
    non_academic_staff_list = Non_Academic_Staff.objects.all()
    return render(request, 'non_academic_staff/non_academic_staff_list.html', 
                  {'non_academic_staff': non_academic_staff_list})  # Fix variable name


def add_non_academic_staff(request):
    if request.method == "POST":
        form = Non_Academic_StaffForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            form.save()
            return redirect('non_academic_staff_list')
        else:
            print(form.errors)  # Debugging: Print form errors in the console
    else:
        form = Non_Academic_StaffForm()
    
    return render(request, 'non_academic_staff/add_non_academic_staff.html', {'form': form})


def update_non_academic_staff(request, id):
    non_academic_staff = get_object_or_404(Non_Academic_Staff, id=id)  # Fix variable
    if request.method == "POST":
        form = Non_Academic_StaffForm(request.POST, request.FILES, instance=non_academic_staff)
        if form.is_valid():
            form.save()
            return redirect('non_academic_staff_list')
    else:
        form = Non_Academic_StaffForm(instance=non_academic_staff)  # Fix variable
    return render(request, 'non_academic_staff/update_non_academic_staff.html', {'form': form})  # Fix template path


def delete_non_academic_staff(request, id):
    non_academic_staff = get_object_or_404(Non_Academic_Staff, id=id)  # Fix variable
    if request.method == "POST":
        non_academic_staff.delete()
        return redirect('non_academic_staff_list')
    return render(request, 'non_academic_staff/delete_non_academic_staff.html', 
                  {'non_academic_staff': non_academic_staff})  # Fix template path
