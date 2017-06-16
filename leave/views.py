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

    # Employee.objects.all().delete()
    # user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    # user.save()
    emp = Employee.objects.create_user(username='kkk', password='pass', email="rasekgalam@gmail.com", first_name='Mokgadi',last_name='Rasekgala', start_date=datetime.date.today())
    # emp.save()
    print "saved"
    found=User.objects.get(username='lll')
    print found.email
    print found.username
    print found.password
    # emp=Employee(user=user))
    # emp.save()
    # myemp = Employee.objects.all()
    # User.objects.all().delete()
    #User.objects.create_superuser(username='admin1', password='123', email='')
    return render(request, 'leave/trial.html')





# def login_post(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
@login_required(login_url="login/")
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
