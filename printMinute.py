from datetime import datetime

odds= [1,3,5,9,10,13]

currentMin=datetime.today().minute
print(currentMin)
if currentMin in odds:
  print("Current time is odd")
else:
  print("current time is not in odd")
