from __future__ import unicode_literals

from django.conf import settings
from django.db import models
import datetime
from django.contrib.auth.models import User
from dateutil.relativedelta import relativedelta


from django.contrib.auth import get_user_model as user_model

class Leave(models.Model):
    STATUSES=(
        ('New','New'),
        ('Approved','Approved'),
        ('Declined','Declined'),
    )
    start_date = models.DateField()
    end_date=models.DateField()
    status=models.CharField(max_length=10,default='New', choices=STATUSES)
    employee_username=models.CharField(max_length=30, default="old")

    @property
    def days_of_leave(self):
        return self.end_date-self.start_date

class Employee(User):
    start_date = models.DateField()



    @property
    def leave_days_remaining(self):
        leave_days=0
        used_days=0 #in current leave cycle
        current_date=datetime.date.today()
        years_working=relativedelta(current_date,self.start_date).years
        months=relativedelta(current_date,self.start_date).months

        if years_working>=1 and months!=0:#already into a new cycle with more than year working
            leave_days=5 + months*1.5
        if years_working==0 and months==11: #in current cyclye
            leave_days=0





        return 10




