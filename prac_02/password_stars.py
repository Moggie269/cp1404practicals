"""CP1404 prac_02 - Password stars"""
minimum_length = int(input('Enter minimum length: '))
password = input("Insert password: ")
while len(password) < minimum_length:
    print("Invalid password")
    password = input("Insert password: ")
print("*" * len(password))