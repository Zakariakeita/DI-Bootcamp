# Exercise 7 : Upcoming Holiday
'''Instructions
Write a function that displays today’s date.
The function should also display the amount of time left from now until the next upcoming holiday and print which holiday that is. (Example: the next holiday is in 30 days and 12:03:45 hours).
Hint: Start by hardcoding the datetime and name of the upcoming holiday.'''

import holidays

def Upcoming_holiday(year=2022):
    from datetime import date
    today = date.today()
    print(f"Today date: {today}")

    year = int(today.strftime('%Y'))
    NG_holidays = holidays.Nigeria(years = year)
    # print(NG_holidays)

    # Print all the holidays in Nigeria
    last_day_of_year =  date((year+1),1,1)
    upcoming_date = last_day_of_year  # Init to end of this year
    upcoming_holiday = "" #No instance

    for date,holiday in NG_holidays.items():
        if (date > today):
            if(date < upcoming_date):
                upcoming_date = date
                upcoming_holiday = holiday
    if ( upcoming_date == last_day_of_year):
        print("No holidays upcoming this year")
    else:
        days= upcoming_date - today 
        print(f"the next holiday: {upcoming_holiday} is in {days} hours)")

Upcoming_holiday()
