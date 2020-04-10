from django.shortcuts import render, redirect
from .forms import UserCreationForm, FormWithCaptcha
from django.contrib.auth.decorators import login_required
from ipware import get_client_ip
from .models import *
from datetime import date


# Create your views here.
def indexView(request):
    return render(request, 'index.html')

@login_required
def dashboardView(request):
    return render(request, 'dashboard.html')

def registerView(request):
    current_date = date.today()
    ip = get_client_ip(request)

    hits = Userip.objects.filter(user_ip=ip[0], date=current_date).count()
    print('______------',hits)
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = Userip(user_ip=ip[0])
            user.save()
            return redirect('login_url')
    elif hits >= 3:
        form = FormWithCaptcha()
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html',{'form':form})
