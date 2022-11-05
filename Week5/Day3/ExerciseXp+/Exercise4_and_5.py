
# 🌟 Exercise 4 : Current Date
# Instructions
# Create a function that displays the current date.
# Hint : Use the datetime module.

# from datetime import datetime,timedelta
from datetime import *

def current_date():
    return datetime.today()

print(current_date())

# Exercise 5 : Amount Of Time Left Until January 1st
# Instructions
# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01hours).

def time_left_until_january():
    today = current_date()
    january = datetime(year=2023, month=1, day=1, hour=0, minute=00)
    until_january = january - today
    return f"the 1st of January is in {until_january} hours"

print(time_left_until_january())
