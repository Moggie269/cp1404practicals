"""
CP1404/CP5632 - Practical
Questions related to the Python random module.
"""

# What did you see on line 1? -> 11
# What was the smallest number you could have seen, what was the largest? min = 5, max = 20
#
# What did you see on line 2? -> 9
# What was the smallest number you could have seen, what was the largest? -> min = 3, max = 9
# Could line 2 have produced a 4? -> It could not have produce a 4 since it produces only odd numbers between 3 and 10.
#
# What did you see on line 3? -> 2.86178224756525
# What was the smallest number you could have seen, what was the largest? min = 2.5, max = 5.499999999999999

import random
print(random.randint(1,100))