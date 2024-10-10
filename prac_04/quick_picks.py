"""
CP1404/CP5632 Practical
"Quick Pick" Lottery Ticket Generator
"""
import random

def main():
    """"""
    number_of_quick_picks = int(input('How many quick picks do you want? '))
    values = []
    generate_random_values(values)
    print(sorted(values))


def generate_random_values(values):
    """Generate 6 random values."""
    for i in range(6):
        random_value = random.randint(1, 46)
        while random_value in values:
            random_value = random.randint(1, 46)
        values.append(random_value)


main()