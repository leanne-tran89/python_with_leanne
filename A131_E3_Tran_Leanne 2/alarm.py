#Leanne Tran
#2/15/23
#Exercise 3, Part 3

# This program asks the user to enter the current time in military format and 
# asks the number of hours after which the alarm should go off
# (program should print the time at which the alarm will ring)


DAY = 24
TWO_DAYS = 48

currentTime = int(input("What is the current time (in military format)? "))
alarmTime = int(input("After how many hours should the alarm go off? "))

ringTime = currentTime + alarmTime

if (ringTime <= DAY):
    alarm = ringTime
else:
    if (ringTime <= TWO_DAYS):
        alarm = ringTime - DAY
    else:
        alarm = ringTime - DAY - DAY

print("The alarm should go off at " + str(alarm))
    