import datetime


currentdate = datetime.date.today()
currenttime = datetime.time()
print(f'the current date is:\t{currentdate}\nthe current time is:\t{currenttime}')

currentdate.ctime()