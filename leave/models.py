from __future__ import unicode_literals

from django.conf import settings
from django.db import models
import datetime
from django.contrib.auth.models import User


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

    @property
    def days_of_leave(self):
        return self.end_date-self.start_date

class Employee(User):
    start_date = models.DateField()

    @property
    def leave_days_remaining(self):
        #to calculate
        calculated_days=10
        return calculated_days




