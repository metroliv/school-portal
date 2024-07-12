from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Mark
from .forms import StudentForm
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .forms import MarkForm



@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})
@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'student_detail.html', {'student': student})
@login_required
def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})
@login_required
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})
@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})


@login_required
def enter_marks(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    
    if request.method == "POST":
        form = MarkForm(request.POST)
        if form.is_valid():
            mark = form.save(commit=False)
            mark.student = student
            # Additional logic to calculate grade, total, etc.
            mark.save()
            return redirect('student_detail', pk=student_id)
    else:
        form = MarkForm()
    
    return render(request, 'enter_marks.html', {'form': form, 'student': student})