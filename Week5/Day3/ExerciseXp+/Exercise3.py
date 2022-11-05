# 🌟 Exercise 3: String Module
# Instructions
# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module

import string
import random

length = 5
letters = ''.join(random.choice(string.ascii_letters) for i in range(length))
print(letters)
