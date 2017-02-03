import os
def find_batteryinfo_file():
    file_list = os.listdir(os.curdir)
    print "_______________"
    for filename in file_list:
        if "BatteryInfo" not in filename:
            continue
        else:
            battery_file = filename
            print battery_file
            break

find_batteryinfo_file()


