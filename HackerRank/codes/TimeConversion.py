__author__ = 'rekhin'
# Given a time in AM/PM format, convert it to military (24-hour) time.
import sys

print "Enter the time : ",
time = raw_input().strip()
length = len(time)
firstTwodigit = time[0:2]
amOrPm = time[length-2:length]
def printTime():
    print(time[0:length-2])
if amOrPm == "AM":
    if firstTwodigit == "12":
        timelist = list(time)
        timelist[0:2]="00"
        time=''.join(timelist)
        printTime()
    else:
        printTime()

else:
    if firstTwodigit == "12":
        printTime()
    else:
        hour = int(firstTwodigit)
        hour+= 12
        timelist = list(time)
        timelist[0:2]=str(hour)
        time = ''.join(timelist)
        printTime()
