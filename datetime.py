import datetime;

def function():

#################printing normal date and time#############################################
	print(datetime.datetime.now())
	print(datetime.datetime.today())
###############################Date Formatting######################################
	print("%y-year %a-weekday %b-month %d-day of month %c- Local date and time %x- Local Date %X-Local time")
	print(datetime.datetime.now().strftime("%a,%d,%b,%a"))
	print(datetime.datetime.now().strftime("Local date and time is :  %c" ))
	print(datetime.datetime.now().strftime("Local date is : %x"))
	print(datetime.datetime.now().strftime("Local time: %X"))

############Time Formatting######################################333
	print("%I/%H - 12/24 Hour, %M- Minute, %S -Second, %p- locales's AM,PM")
	print(datetime.datetime.now().strftime("Current time is %I:%M:%S:%p"))
	print(datetime.datetime.now().strftime("Current time in 24 hours format is  %H:%M:%S:%p"))


###############Calling function###################################
function()
