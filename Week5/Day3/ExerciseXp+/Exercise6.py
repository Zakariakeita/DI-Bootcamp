
# Exercise 6 : Birthday And Minutes
'''
Instructions
Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.'''

from datetime import * 
def minutes_lived(year,month,day,hour=0,minute=0):
    now=datetime.now()
    birthdate= datetime(year=year,month=month,day=day,hour=hour,minute=minute)
    time = now - birthdate
    totalminutes = (time.days*60*24) + (time.seconds // 60)
    return f" You lived {time.seconds} minutes In other words {time.days} days and {(time.seconds // 60 % 60)} minutes"

print(minutes_lived(year=2000,month=12,day=31))

