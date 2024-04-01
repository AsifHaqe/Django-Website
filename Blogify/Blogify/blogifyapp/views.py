from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import usersForm
from django.contrib import messages

# Create your views here.
def Homepage(request):
    return render(request,'blogapp/home.html')

def blogpage(request):
    return render(request,'blogapp/blog.html')

def loginpage(request):
    forms = LoginForm()
    return render(request,'blogapp/login.html',{'forms': forms})

def singnuppage(request):
    if request.method =='POST':
        forms = usersForm(request.POST)
        
        if forms.is_valid():
            forms.save()
            messages.successs(request,"Registration successsful")
            return redirect('blogapp.singnup.html')
    else:     # print(forms.cleaned_data)
        forms = usersForm()
    return render(request,'blogapp/singnup.html',{'forms': forms})

def dashboardpage(request):
    return render(request,'blogapp/dashboard.html')
