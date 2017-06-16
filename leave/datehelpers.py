from calendar import monthrange
from datetime import datetime, timedelta
from .workdays import networkdays

#Valid leave : Not in first three months,valid dateperiod, Enough Days


def isValidLeavePrediod(work_start,remaining_days,start_date,end_date):
    valid=True
    message="Valid"

    if not ProbationPeriodOver(work_start,start_date):
        valid=False
        message="You would have not completed 3 months at that date"

    if not validDatePeriod(start_date,end_date):
        valid=False
        message="Start date has to be before end date"

    if not daysAvailable(remaining_days,start_date,end_date):
        valid=False
        message="You do not have enough days for the requested period"


    return (valid,message)




def monthdelta(d1, d2):
    delta = 0
    while True:
        mdays = monthrange(d1.year, d1.month)[1]
        d1 =d1+ timedelta(days=mdays)
        if d1 <= d2:
            delta += 1
        else:
            break
    return delta





def ProbationPeriodOver(work_startdate,leave_startdate):
    over= True
    months_worked=monthdelta(leave_startdate,work_startdate)
    if months_worked<3:
        over=False

def validDatePeriod(start_date,end_date):
    #from to start logical
    #not on a weekend
    valid=True
    if start_date>end_date:
        valid=False
    return valid


def daysAvailable(remaining_days,start_date,end_date):
    available=True
    leave_days=networkdays(start_date,end_date)
    if leave_days>remaining_days:
        available=False
    return available