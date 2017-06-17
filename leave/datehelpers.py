from calendar import monthrange
from datetime import datetime, timedelta
from .workdays import networkdays




def isValidLeavePrediod(remaining_days,start_date,end_date):
    valid=True
    message="Valid"
    # Valid leave : valid dateperiod, Enough Days

    #date from to start end in right order
    #not earlier than current date
    #start and end not on weekend

    if start_date > end_date:
        valid=False
        message="Start date has to be before end date"


    if start_date<datetime.date.today():
        #assuming all leave must be booked prior to day leave is taken
        valid=False
        message="Start date has to be later than today"

    if start_date.weekday()>=5 or end_date.weekday()>=5:#saturday or sunday
        valid=False
        messae="Leave can't start or end on a weekend day"

    if not daysAvailable(remaining_days,start_date,end_date):
        valid=False
        message="You do not have enough days for the requested period"


    return (valid,message)




def daysAvailable(remaining_days,start_date,end_date):
    available=True
    leave_days=networkdays(start_date,end_date)
    if leave_days>remaining_days:
        available=False
    return available