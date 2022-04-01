
def countDayOfTheWeek():
    # This first line is provided for you
    file_name = input("Enter a file name: ")   
    f = open(file_name, "r")
    
    weekCount = {
      "Thu": 0,
      "Fri": 0,
      "Sat": 0
    }

    for line in f:
        line = line.strip()
        if line.startswith("From") and not line.startswith("From:"):
               dayOfWeek = line.split()[2]
               if(dayOfWeek == "Thu"):
                 weekCount["Thu"] += 1
               elif(dayOfWeek == "Fri"):
                 weekCount["Fri"] += 1
               elif(dayOfWeek == "Sat"):
                 weekCount["Sat"] += 1
    
    print(weekCount)


## if you want to test locally before you try to sync
## uncomment calculateAbsolute() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
countDayOfTheWeek()