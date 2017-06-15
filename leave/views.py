from leave.models import Leave, Employee
from django.shortcuts import render
import datetime
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def trial(request):
    # Only for testing purposes. Will be removed
    # Leave.objects.all().delete()
    # dt = timedelta(days=2)
    # leave = Leave(start_date=datetime.date.today(), end_date=datetime.date.today() + dt)
    # leave.save()
    # myleave = Leave.objects.all()

    Employee.objects.all().delete()
    emp = Employee(username='modizzzle', password='pass123', email="rasekgalam@gmail.com", first_name='Mokgadi',
                   last_name='Rasekgala', start_date=datetime.date.today())
    user=User.objects.all()
    emp.save()
    myemp = Employee.objects.all()
    print user[0]

    context = {
               # 'start': myleave[0].start_date,
               # 'days': myleave[0].days_of_leave,
               'found_user':user[0].username,
               'found_user_pass': user[0].password,
               'left_days': myemp[0].leave_days_remaining,
               'emp_name':myemp[0].first_name + myemp[0].last_name
              }

    return render(request, 'leave/trial.html', context)




@login_required(login_url="logdddin")


# def login_post(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)

def index(request):
    #if no session back to login
    #else -basic dashboard

    context = {
        'employee': 'Mokgadi'

    }
    return render(request,'leave/index.html',context)



def log_leave(request):
    context={
        'employee': 'Mokgadi'
    }
    return render(request, 'leave/leave.html', context)
