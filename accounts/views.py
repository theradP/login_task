from django.shortcuts import render, redirect
from .forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from ipware import get_client_ip
from .models import *
from .serializers import Countserializer
from django_q.tasks import schedule

def countrefresh():
    Userip.objects.all().update(count=0)


schedule('countrefresh', schedule_type='D')
# Create your views here.
def indexView(request):
    return render(request, 'index.html')

@login_required
def dashboardView(request):
    return render(request, 'dashboard.html')

def registerView(request):
    c=0
    ip = get_client_ip(request)
    queryset = Userip.objects.filter(user_ip=ip[0]).exists()
    if queryset:
        user = Userip.objects.filter(user_ip=ip[0]).values('count')
        count = Countserializer(user)
        count = count.data['count']+1
        user.update(count=count)
        c = count
    else:
        user = Userip(user_ip=ip[0], count=1)
        user.save()
    if c<=3:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login_url')
        else:
            form = UserCreationForm()
        return render(request, 'registration/register.html',{'form':form})
    else:
        return render(request,'registration/register_recaptcha.html')
