TO RUN
clone repo
run on terminal in dir-python manage.py makemigrations
run on terminal in dir-python manage.py migrate

on localhost:8000/newemploye Create an rmploye
login employee localhost:8000/login

you can log leave an see on dashboard



ASSUMPTIONS
1. You can book leave  for a date before current date (sick leave taken before booking)
2.nth month a person is working is the period fro relative start date to relative end date -1 day
    example: If i start working 1 March 2016, my 1st month interval [1 March, 31 March) and 2nd Month interval [1 April,30 April)



LEAVE DAYS REMAINING
On your dashboard you can view two values for leave days remaining.
1. The leave days not yet taken(future leave days)
2. the leave days you have left after taking all planned/requested leave (even future leave)
