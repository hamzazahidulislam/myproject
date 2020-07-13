from django.shortcuts import render, redirect
from .forms import *
from .models import *


def create_student(request):
    form = StudentCreateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('create-student')
    context = {
        'form': form
    }
    return render(request, 'student/create_std.html', context)

def get_result(request):
    form = ResultForm()
    context = {'form': form}
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            std_class = form.cleaned_data["std_class"]
            roll = form.cleaned_data["roll"]

            try:
                std = StudentList.objects.get(std_class=std_class, roll=roll)
                context = {'gpa': std.gpa, 'form': form}
            except Exception as err:
                context = {'error': str(err), 'form': form}
    return render(request, 'student/get_result.html', context)