from calendar import monthrange
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


def days_on_leave_count(start,end):
	public_holidays=[(1,1),(21,3),(14,4),(17,4),(27,4),(1,5),(16,6),(9,8),(24,9),(16,12),(25,12),(26,12)]
	total_days=(end-start).days +1
	oneday=timedelta(days=1)
	current_date=start
	for i in range(0,total_days+1):
		if current_date.weekday()>=5 or (current_date.day,current_date.month) in public_holidays: #day is weekend or public holiday
			total_days-=1
		current_date+=oneday
	return total_days

def isValidLeavePrediod(work_start_date,remaining_days,start_date,end_date):
    valid=True
    message="Valid"
    # Valid leave : valid dateperiod, Enough Days, not on probation

    #date from to start end in right order
    #not earlier than current date
    #start and end not on weekend
    if OnProbation(work_start_date,start_date):
        valid=False
        message="You wouldn't have worked for three months at the time of your leave"

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


def OnProbation(work_start_date,leave_start_date):
    probation=True
    months_working = relativedelta(leave_start_date, work_start_date).months
    if months_working>=3:
        probation=False
    return probation



def daysAvailable(remaining_days,start_date,end_date):
    available=True
    leave_days=days_on_leave_count(start_date,end_date)
    if leave_days>remaining_days:
        available=False
    return available