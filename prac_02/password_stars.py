"""
CP1404/CP5632 - Practical
Password stars
"""


def main():
    """Get a minimum length and a password."""
    minimum_length = int(input('Enter minimum length: '))
    password = get_valid_password("Insert password: ", minimum_length)
    print_stars(password)


def get_valid_password(prompt, minimum_length):
    """Get a valid password."""
    password = input(prompt)
    while len(password) < minimum_length:
        print("Invalid password")
        password = input(prompt)
    return password


def print_stars(word):
    """Print as many stars as the word is long"""
    print("*" * len(word))


main()
