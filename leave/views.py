from leave.models import Leave, Employee
from django.shortcuts import render
from django.shortcuts import redirect
import datetime
from .forms import LogLeaveForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

def create_employee(request): #for hr admin
    if request.method == 'POST':
        username = request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        emp = Employee.objects.create_user(username=username, password=password, email=email, first_name=firstname,last_name=lastname, start_date=datetime.date.today())
        messages.success(request, "New Employee Created by Admin. Let the Employee login")
        return redirect('login')
    else:
        return render(request, 'leave/newemployee.html')


@login_required(login_url="login/")
def index(request):
    context = {
        'username': request.user.username,
        'first_name':request.user.first_name,
        'last_name':request.user.last_name
    }
    return render(request,'leave/index.html',context)



def log_leave(request):
    form = LogLeaveForm(request.POST)
    if request.method=='POST':
        if form.is_valid():
            startdate=form.cleaned_data['startdate']
            enddate=form.cleaned_data['enddate']
            messages.success(request,"Leave logged")
            return redirect('/')
        else:
            messages.error(request,'Cant Sorry ')
            return redirect('/leave')
    else:
        context={
            'employee': 'Mokgadi'
        }
        return render(request, 'leave/leave.html', context,{'form':form})


