"""
CP1404/CP5632 - Practical
Password stars
"""


def main():
    minimum_length = int(input('Enter minimum length: '))
    password = get_valid_password("Insert password: ", minimum_length)
    print_stars(password)


def get_valid_password(prompt, minimum_length):
    password = input(prompt)
    while len(password) < minimum_length:
        print("Invalid password")
        password = input(prompt)
    return password


def print_stars(password):
    print("*" * len(password))


main()
