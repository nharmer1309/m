from datetime import date

# If today is Monday (aka 0 of 6), then run the report
if date.today().weekday() == 0:
    print("Laqgha Onine")

#tuesday
if date.today().weekday() == 1:
    print("Follow Up")
    
#wednesday
if date.today().weekday() == 2:
    print("Laqgha Blata l-Bajda :(")
    
#thursday
if date.today().weekday() == 3:
    print("Follow Up")
    
#friday
if date.today().weekday() == 4:
    print("Assenjatur")
    
#saturday
if date.today().weekday() == 5:
    print("Qaghda")
    
#sunday
if date.today().weekday() == 6:
    print("Filoghdu u filghaxija")





