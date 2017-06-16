from leave.models import Leave, Employee
from django.shortcuts import render
from django.shortcuts import redirect
import datetime
from .forms import LogLeaveForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .datehelpers import isValidLeavePrediod

def create_employee(request): #for hr admin
    if request.method == 'POST':
        username = request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        emp = Employee.objects.create_user(username=username, password=password, email=email, first_name=firstname,last_name=lastname, start_date=datetime.date(2017,1,1))
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
            emp=Employee.objects.get(username=request.user.username)
            validated=isValidLeavePrediod(emp.start_date,emp.leave_days_remaining,startdate,enddate)
            if validated[0]:
                messages.success(request,'Leave Logged for Approval')
                return redirect('/')
            else:
                leave=Leave.objects.create(start_date=startdate,end_date=enddate,employee_username=request.user.username)
                messages.error(request,validated[1])
                return redirect('/leave')
        else:
            messages.error(request, "Something wrong with the details entered, try again ")
            return redirect('/leave')


    else:
        context={
            'employee': 'Mokgadi',
            'form':form
        }
        return render(request, 'leave/leave.html', context)


