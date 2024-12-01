"""
CP1404/CP5632 - Practical
Tasks related to reading and writing files.
"""

# 1.
user_name = input("Enter your name: ")
out_file = open('name.txt', 'w')
print(user_name, file=out_file)
out_file.close()

# 2.
in_file = open('name.txt')
new_name = in_file.read().strip()
print(f"Hi {new_name}!")
in_file.close()

# 3.
with open('numbers.txt') as in_file:
    number_1 = int(in_file.readline())
    number_2 = int(in_file.readline())
    total = number_1 + number_2
    print(total)

# 4.
with open('numbers.txt') as in_file:
    total = 0
    for line in in_file:
        total += int(line)
    print(total)