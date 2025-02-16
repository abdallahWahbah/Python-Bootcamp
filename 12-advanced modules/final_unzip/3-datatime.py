from datetime import time, date, datetime

## time
myTime = time(2, 10, 30) # 2 am(24 hour format), 10 min, 30 seconds
print(myTime.hour, myTime.minute, myTime.second)

## date
myDate = date.today() # 2025-02-16
print(myDate) # 2025-02-16
print(myDate.year, myDate.month, myDate.day)
print(myDate.ctime()) # Sun Feb 16 00:00:00 2025

## date and time 
myDateTime = datetime(2025, 7, 29, 13, 30, 7) # year, month, day, hour, minute, second
print(myDateTime) # 2025-07-29 13:30:07
myDateTime = myDateTime.replace(year=2030)
print(myDateTime) # 2030-07-29 13:30:07






## Get the current date and time
current_datetime = datetime.now()  
print(current_datetime) # 2025-02-16 16:29:43.338821
print(current_datetime.day, current_datetime.month, current_datetime.year) # 16 2 2025
print(current_datetime.hour, current_datetime.minute, current_datetime.second) # 16 29 43






## difference between 2 dates
date1 = date(2021, 11, 25)
date2 = date(2022, 11, 25)
dateDifference = date2 - date1 # difference in days
print(dateDifference) # 365 days, 0:00:00
print(dateDifference.days) # 365

## difference between 2 datetime2
datetime1 = datetime(2021, 11, 25, 22, 0)
datetime2 = datetime(2022, 11, 25, 12, 0)
datetimeDifference = datetime2 - datetime1 # difference in days and seconds
print(datetimeDifference) # 364 days, 14:00:00
print(datetimeDifference.days, datetimeDifference.seconds / 60 / 60) # 364 14 (hours)


## Get the current time (not important, you can use code above only (datetime.now()) )
current_time = datetime.now().time()  
print(current_time) # 16:28:6
print(current_time.hour, current_time.minute, current_time.second) # 16 28 6