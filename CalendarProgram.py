import calendar
  
#Lets create a plain calendar, starts calendar with sunday

c=calendar.TextCalendar(calendar.SUNDAY)
st=c.formatmonth(2020,1,0,0)
print(st)


#The calendar provides useful utilities for given locale, such as day and month names
for month in calendar.month_name:
        print(month)

print("****************************")

for day in calendar.day_name:
        print(day)

#Calculate days based on rule: for example, consider a team meeting on the first friday of every month
#To figure out what days that would be for each month.
print("Team meetings will be on")
#13 is non inclusive in this range
for monthnumber in range(1,13):
        #This will print weeks array list present in month
        cal=calendar.monthcalendar(2018,monthnumber)

#This will store first week into weekone variable and weektwo in weektwo variable
        weekone=cal[0]
        weektwo=cal[1]

        if weekone[calendar.FRIDAY]!=0:
                meetday=weekone[calendar.FRIDAY]
#               print(meetday)
        else:
                meetday=weektwo[calendar.FRIDAY]
#               print(meetday)

#       print(calendar.month_name[monthnumber])
#       print(meetday)
        print("%10s %2d" % (calendar.month_name[monthnumber],meetday))
