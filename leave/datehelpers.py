
import datetime
from datetime import timedelta


def isPublicHoliday(mydate):
    public_holidays = [(1, 1), (21, 3), (14, 4), (17, 4), (27, 4), (1, 5), (16, 6), (9, 8), (24, 9), (16, 12), (25, 12),
                       (26, 12)]
    if (mydate.day,mydate.month) in public_holidays:
        return True
    return False


def days_on_leave_count(start,end):
	public_holidays=[(1,1),(21,3),(14,4),(17,4),(27,4),(1,5),(16,6),(9,8),(24,9),(16,12),(25,12),(26,12)]
	total_days=(end-start).days +1
	oneday=timedelta(days=1)
	current_date=start
	while current_date<=end:
		if current_date.weekday()>=5 or isPublicHoliday(current_date): #day is weekend or public holiday
			total_days-=1
		current_date+=oneday
	return total_days

def isValidDatePrediod(start_date,end_date):
    valid=True
    message="Valid"
    #Valid leavePeriod-> valid dateperiod

    #date from to start end in right order
    #not earlier than current date
    #start and end not on weekend

    if start_date > end_date:
        valid=False
        message="Start date has to be before end date"


    # if start_date<datetime.date.today():
    #     #assuming all leave must be booked prior to day leave is taken
    #     valid=False
    #     message="Start date has to be later than today"

    if start_date.weekday()>=5 or end_date.weekday()>=5:#saturday or sunday
        valid=False
        message="Leave can't start or end on a weekend day"

    return (valid,message)


def daysAreAvailable(remaining_days,start_date,end_date):
    available=True
    leave_days=days_on_leave_count(start_date,end_date)
    if leave_days>remaining_days:
        available=False
    return available