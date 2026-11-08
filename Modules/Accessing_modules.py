import sys

location=sys.path

print()

for i in location:
    print(i)


import calendar

leap_days=calendar.leapdays(2000,2050)
isLeap=calendar.isleap(2032)
print("This Year Is Leap : ",isLeap)
print(leap_days)