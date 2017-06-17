from leave.models import Leave, Employee
from django.shortcuts import render
from django.shortcuts import redirect
import datetime
from .forms import LogLeaveForm, CreateEmployeeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

def create_employee(request): #for hr admin
    form=CreateEmployeeForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password=form.cleaned_data['password']
            email=form.cleaned_data['email']
            firstname=form.cleaned_data['firstname']
            lastname=form.cleaned_data['lastname']
            startdate=form.cleaned_data['startdate']
            emp = Employee.objects.create_user(username=username, password=password, email=email, first_name=firstname,last_name=lastname, start_date=startdate)
            messages.success(request, "New Employee Created by Admin. Let the Employee login")
            return redirect('login')
        else:
            messages.error(request, "Something wrong with the details entered, try again ")
            return redirect('/newemployee')
    else:
        return render(request, 'leave/newemployee.html',{'form':form})


@login_required(login_url="login/")
def index(request):

    leave_requests=Leave.objects.filter(employee_username=request.user.username)
    emp = Employee.objects.get(username=request.user.username)
    if len(leave_requests)==0:
        leave_requests=None

    context = {
        'days_remaining':emp.leave_days_remaining(),
        'leave_requests':leave_requests,
        'username': emp.username,
        'first_name':emp.first_name,
        'last_name':emp.last_name,
        'start_date':emp.start_date
    }
    return render(request,'leave/index.html',context)


@login_required(login_url="login/")
def log_leave(request):
    form = LogLeaveForm(request.POST)
    emp = Employee.objects.get(username=request.user.username)
    if request.method=='POST':
        if form.is_valid():
            startdate=form.cleaned_data['startdate']
            enddate=form.cleaned_data['enddate']
            validated=emp.isPreApproved(startdate,enddate)
            print validated
            if validated[0]:
                leave = Leave.objects.create(start_date=startdate, end_date=enddate,employee_username=request.user.username)
                messages.success(request,'Leave Logged for Approval')
                return redirect('/')
            else:
                messages.error(request,validated[1])
                return redirect('/leave')
        else:
            messages.error(request, "Something wrong with the details entered, try again ")
            return redirect('/leave')


    else:
        context={
            'employee': emp,
            'form':form
        }
        return render(request, 'leave/leave.html', context)


