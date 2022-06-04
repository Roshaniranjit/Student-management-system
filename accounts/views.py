from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import CreateuserForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
# Create your views here.


def register(request):
    form = CreateuserForm()

    if request.method == 'POST':
        form = CreateuserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created for '+user)
            return redirect('login')

    else:
        form = CreateuserForm()

    context = {"form": form}
    return render(request, 'accounts/register.html', context)



def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')
