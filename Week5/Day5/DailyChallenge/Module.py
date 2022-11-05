# Python program to check the
# loading time of the website

# Importing the libraries
from urllib.request import urlopen
from time import time

# Obtaining the URL of website
website = urlopen('https://www.google.com/')

# Return the number of seconds
# passed since epoch
open_time = time()

# Read the complete website
output = website.read()

# Return the number of seconds
# passed since epoch
close_time = time()

# Close the website
website.close()

# Subtract and print the open time
# of website from close time
print('The loading time of website is',round(close_time-open_time,3),'seconds')
