"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print('Denominator cannot be equal to 0!')
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

# 1. When will a ValueError occur? -> In case we input a string
# 2. When will a ZeroDivisionError occur? -> In case denominator is equal to 0
# 3. Could you change the code to avoid the possibility of a ZeroDivisionError? -> Yes