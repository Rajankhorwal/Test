
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from .models import *
from .form1 import CreateUserForm
# from .filters import OrderFilter


def index(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')

            messages.success(request,'account created for '+user)

            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)

def loginPage(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('next')
        else:
            messages.info(request,'username or pass is incorrect')
    context={}
    return render(request,'login.html',context)
def logoutuser(request):
    logout(request)
    return redirect('login')

def next(request):
    context={}
    return render(request,'try.html',context)


