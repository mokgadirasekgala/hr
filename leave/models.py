

from __future__ import unicode_literals

from django.conf import settings
from django.db import models
import datetime
from django.contrib.auth.models import User
from dateutil.relativedelta import relativedelta
from datehelpers import days_on_leave_count

class Leave(models.Model):
    STATUSES=(
        ('New','New'),
        ('Approved','Approved'),
        ('Declined','Declined'),
    )
    start_date = models.DateField()
    end_date=models.DateField()
    status=models.CharField(max_length=10,default='New', choices=STATUSES)
    employee_username=models.CharField(max_length=30)

    @property
    def days_of_leave(self):
        return days_on_leave_count(self.start_date,self.end_date)




def taken(n,employee):
    #number of days taken by employee in the nth month since working
    


class Employee(User):
    start_date = models.DateField()
    @property
    def leave_days_remaining(self):
        #1.5 days end of each month
        # #5 days carried over from previous cycle
        #cycle =year= end of 12 months

        # leave_days(n) -> recursive function giving leave days at the end of n months
        # taken(n) -> The number of days leave days taken in the period of  nth month since working
        #leave_days(1)=1.5-taken(1)
        #leave_days(2)=1.5+leave_days(1)-taken(2)
        #...
        #leave_days(11)=1.5+f(10)-taken(11)
        #On the  month=12 or n  is a multiple of 12), (we are in a going to new  cycle )
            #current=leave_days(11)-taken(12)
            #if current between (1-4) -left over from last cycle
                #leave_days(n)=current
            #if lcurrent>=5
                #leave_days(n)=5
            #if current=0
                #leave_days(n)=0
        #next month continue as above leave_days(n)=1.5+leave_days(n-1)-taken(n)



        return 10










        return total_days




