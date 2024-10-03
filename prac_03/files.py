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