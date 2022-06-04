

import student
from django.shortcuts import redirect, render
from .forms import UpDateInfo
from .models import Student
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
def createstudent(request):
    form = UpDateInfo()
    if request.method == 'POST':
        form = UpDateInfo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form
    }

    return render(request, 'students/profile_update.html', context)


@login_required(login_url='login')
def home(request):
    students = Student.objects.all()
    context={
        'students':students
    }
    return render(request, 'students/dashboard.html',context)

@login_required(login_url='login')
def upDatestudent(request, pk):

	students = Student.objects.get(id=pk)
	form = UpDateInfo(instance=students)

	if request.method == 'POST':
		form = UpDateInfo(request.POST, instance=students)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'students/profile_update.html', context)


@login_required(login_url='login')
def DelStud(request,pk):
    students=Student.objects.get(id=pk)
    if request.method=="POST":
        students.delete()
        return redirect('/')
    context={'students':students}


    return render(request,'students/delete.html',context)