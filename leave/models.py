

from __future__ import unicode_literals

from django.conf import settings
from django.db import models
import datetime
from django.contrib.auth.models import User
from dateutil.relativedelta import relativedelta
from datetime import timedelta
from datehelpers import days_on_leave_count,daysAreAvailable,isValidDatePrediod

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

    def days_of_leave(self):
        return days_on_leave_count(self.start_date,self.end_date)



class Employee(User):
    start_date = models.DateField()


    def get_month_interval(self,n):
        # get tuple giving start and end date on the nth month of employee working
        #if you start work 1st Jan 2017
        #n=1, 1 Jan-30 Jan
        #n=2, 1 Feb 2017- 29Feb
        s = relativedelta(months=n - 1)
        e = relativedelta(months=n)
        day=timedelta(days=1)
        return (self.start_date + s, self.start_date + e-day)

    def days_taken_in_interval(self,period_start,period_end):
        #days of leave taken from start date to end
        leave_taken = Leave.objects.filter(employee_username=self.username, start_date__gte=period_start,
                                           start_date__lte=period_end)
        days = 0
        for leave in leave_taken:
            days += leave.days_of_leave()
        return days


    def taken(self,n):
        #number of leave days taken by employee in the nth month interval since working
        #if the start date of a leave is in the nth month and the end date in the kth month, the leave is taken in the nth month
        period=self.get_month_interval(n)
        period_start=period[0]
        period_end=period[1]

        return self.days_taken_in_interval(period_start,period_end)


    def leave_days_remaining_at_date(self,atDate):
        leave_requests = Leave.objects.filter(employee_username=self.username).order_by('-start_date')
        if atDate<leave_requests[0].start_date: #booking for earlier date, all later leave dates included
            atDate=leave_requests[0].start_date
        years_working=relativedelta(atDate, self.start_date).years
        months = relativedelta(atDate, self.start_date).months #months working excluding years
        days= relativedelta(atDate, self.start_date).days


        total_months=(years_working*12) +months

        remaining=leave_day_at_n_months(total_months,self)
        #you could have taken leave in the last days before the month ends
        delta=timedelta(days=-days)
        extra_leave_days=self.days_taken_in_interval(atDate+delta,atDate)




        return remaining-extra_leave_days



    def leave_days_remaining(self):
        return self.leave_days_remaining_at_date(datetime.date.today())

    def leave_not_taken(self):
        #if you have already started taking the leave, the leave is considered taken even if not all days taken
        leave_requests = Leave.objects.filter(employee_username=self.username).order_by('-start_date')
        days=0
        for leave in leave_requests:
            if leave.start_date>datetime.date.today():
                days+=leave.days_of_leave()
        return days





    def isOnProbationAtDate(self,atDate):
        probation = False
        years_working=relativedelta(atDate, self.start_date).years
        months_working = relativedelta(atDate, self.start_date).months
        if months_working < 3  and years_working<1 :
            probation = True
        return probation

    def isOnProbation(self):
        return self.isOnProbationAtDate(datetime.date.today())

    def isPreApproved(self,start_date,end_date):
        #returns tuple giving approved boolean and reason
        #leave requested meets condition will be accepted to be approved later
        #is not on Probation
        #Has enough leave days
        #valid date period
        approved=True
        reason="You meet requiremnts, Leave sent through to manager for approval"
        validPeriod=isValidDatePrediod(start_date,end_date)
        if not validPeriod[0]:
            return (False,validPeriod[1])
        if self.isOnProbationAtDate(start_date):
            return(False,"You will still be on probation on leave date")
        if not daysAreAvailable(self.leave_days_remaining_at_date(start_date),start_date,end_date):
            return (False,"You do not have enough days")
        return (approved,reason)






def leave_day_at_n_months(n,employee):
    # leave_days(n) -> recursive function giving leave days at the end of n months
    # taken(n) -> The number of days leave days taken in the period of  nth month since working
    # leave_days(1)=1.5-taken(1)
    # leave_days(2)=1.5+leave_days(1)-taken(2)
    # ...
    # leave_days(11)=1.5+f(10)-taken(11)
    # On the  month=12 or n  is a multiple of 12), (we are in a going to new  cycle )
    # current=leave_days(11)-taken(12)
    # if current between (1-4) -left over from last cycle
    # leave_days(n)=current
    # if lcurrent>=5
    # leave_days(n)=5
    # if current=0
    # leave_days(n)=0
    # next month continue as above leave_days(n)=1.5+leave_days(n-1)-taken(n)
    if n==0:
        return 0
    if n==1:
        return 1.5-employee.taken(1)
    elif n % 12==0:
        current=leave_day_at_n_months(n-1,employee)-employee.taken(n)
        if current>=1 and current<=4:
            return current
        if current>=5:
            return 5
        if current==0:
            return 0
    else:
        return 1.5+leave_day_at_n_months(n-1,employee)-employee.taken(n)




