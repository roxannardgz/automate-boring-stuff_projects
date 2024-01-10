## Date Detection

import re

#checks if the year is a leap year
def isLeapYear(year):
    if int(year) % 4 == 0:
        if int(year) % 100 == 0:
            if int(year) % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

#checks is the date is valis based on the dates for each month
def isValidDate(month, day, year):
    
    if month in ('04', '06', '08', '11'):   #checks if the month is in April, June, August and November
        if int(day)> 30:                    #verify max date is valid (max 30)
            print('Invalid Date: this month cannot have more than 30 days.')
    elif month == '02':                     #checks if month is February
        if int(day) > 29:                   #Verify if date is valid (max 29)
            print('Invalid Date: February can never have more than 29 days.')
        elif int(day) == 29:                
            isLeapYear(year)                #check if is leap year
            if isLeapYear(year) == True:
                print(f"{day}/{month}/{year} is a valid date, yay.")
            else:
                print('Invalid Date: ' + year + ' is not a leap year, therefore February cannot have 29 days.')
        else:
            print(f"{day}/{month}/{year} is a valid date, yay!!.")
    else:                                   #for the rest o the months
        print(f"{day}/{month}/{year} is a valid date.")
        
        
#checks if the inserted text follows the required date format
def isDate(given_date):
    dateRx = re.compile(r'''
                        (0[1-9]|[1-2][0-9]|3[0-1])       #day
                        (/)
                        (0[1-9]|1[0-2])                  #month
                        (/)
                        ([1-2][0-9]{3})                  #year
                        ''', re.VERBOSE)   

    detection = dateRx.search(given_date)

    if detection:
        day = detection.group(1)
        month = detection.group(3)
        year = detection.group(5)
        
        isValidDate(month, day, year)
        
    else:
        print('This doesn\'t follow the format or the values are out of range.')
        

given_date = input('Please insert a date in the DD/MM/YYYY format: ')
isDate(given_date)
