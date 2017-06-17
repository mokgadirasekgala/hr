

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






class Employee(User):
    start_date = models.DateField()
    @property
    def leave_days_remaining(self):
        #18 days at the end of each year
        #no leave within first three months of cycle
        #5 days carried over from previous cycle

        accumulated=0
        current_cycle_days=0
        total_days=0

        current_date = datetime.date.today()
        years_working = relativedelta(current_date, self.start_date).years
        months = relativedelta(current_date, self.start_date).months #number of months into new cycle

        print "Years" ,years_working
        print "Months", months

        if years_working==0 and months<3:#less than 3 months in new cycle
           return 0
        if years_working==1: #working for a year not yet 2 years, would have only accumulated 18 days
            accumulated= 18
        if years_working>=2: #working for 2 leave cycles, must back track to see if there was accumulation
            for i in range(2,years_working):


            leave_taken=Leave.objects.filter(employee_username=self.username)
            for leave in leave_taken:





        #deduct days taken
            #for every Leave with employee_usernme=thisemployee taken in current cycle
                 #current_cycle_days=current_cycle_days-leave.days_of_leave

            #check if leave days had been carried over from last year.
            #for every leave with employee_username =this.employee taken in past cycle






        return total_days




