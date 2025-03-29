

from django.shortcuts import render, redirect, get_object_or_404
from .models import Lecturer
from .forms import LecturerForm


def lecturer_list(request):
    lecturers = Lecturer.objects.all()
    return render(request, 'lecturer/lecturer_list.html', {'lecturers': lecturers})

def add_lecturer(request):
    if request.method == "POST":
        form = LecturerForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            form.save()
            return redirect('lecturer_list')
    else:
        form = LecturerForm()
    
    return render(request, 'lecturer/add_lecturer.html', {'form': form})



def update_lecturer(request, id):  # Change parameter name to 'id'
    lecturer = get_object_or_404(Lecturer, id=id)  # Use 'id' here
    if request.method == "POST":
        form = LecturerForm(request.POST, request.FILES, instance=lecturer)
        if form.is_valid():
            form.save()
            return redirect('lecturer_list')
    else:
        form = LecturerForm(instance=lecturer)
    return render(request, 'lecturer/update_lecturer.html', {'form': form})


def delete_lecturer(request, id):  # Change lecturer_id to id
    lecturer = get_object_or_404(Lecturer, id=id)
    if request.method == "POST":
        lecturer.delete()
        return redirect('lecturer_list')
    return render(request, 'lecturer/delete_lecturer.html', {'lecturer': lecturer})
