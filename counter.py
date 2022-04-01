
from calendar import week
from this import d


def countDayOfTheWeek():
    # This first line is provided for you
    file_name = input("Enter a file name: ")   
    f = open(file_name, "r")

    weekCount = dict()

    for line in f:
        line = line.strip()
        if line.startswith("From") and not line.startswith("From:"):
               dayOfWeek = line.split()[2]
               if dayOfWeek not in weekCount:
                 weekCount[dayOfWeek] = 1
               else:
                 weekCount[dayOfWeek] += 1
    
    print(weekCount)


## if you want to test locally before you try to sync
## uncomment calculateAbsolute() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
##countDayOfTheWeek()