from django.shortcuts import render, redirect
from .forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from ipware import get_client_ip
from .models import *
from datetime import date
# from django_q.tasks import schedule
#
# def countrefresh():
#     Userip.objects.all().update(count=0)
#
#
# schedule('countrefresh', schedule_type='D')
# Create your views here.
def indexView(request):
    return render(request, 'index.html')

@login_required
def dashboardView(request):
    return render(request, 'dashboard.html')

def registerView(request):
    current_date = date.today()
    ip = get_client_ip(request)
    user = Userip(user_ip=ip[0])
    user.save()
    hitcount = Userip.objects.filter(user_ip=ip[0], date=current_date).count()
    if request.method == "POST":
        if hitcount < 3:
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login_url')
        else:
            #redirect to captcha
            return render(request,'registration/register_recaptcha.html')

    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html',{'form':form})
