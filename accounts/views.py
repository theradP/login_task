from django.shortcuts import render, redirect
from .forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from ipware import get_client_ip
from .models import *
# Create your views here.
def indexView(request):
    return render(request, 'index.html')

@login_required
def dashboardView(request):
    return render(request, 'dashboard.html')

def registerView(request):
    ip = get_client_ip(request)
    user = Userip(user_ip=ip[0])
    user.save()
    # print('---------------',type(ip[0]),ip[0])
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html',{'form':form})
