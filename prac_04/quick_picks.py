"""
CP1404/CP5632 Practical
"Quick Pick" Lottery Ticket Generator
"""
import random


def main():
    """Print lines of values."""
    number_of_quick_picks = int(input('How many quick picks do you want? '))
    for i in range(number_of_quick_picks):
        quick_picks = []
        generate_random_values(quick_picks)
        for value in quick_picks:
            print(f'{value:3}', end='')
        print()


def generate_random_values(values):
    """Generate 6 random values."""
    for i in range(6):
        random_value = random.randint(1, 46)
        while random_value in values:
            random_value = random.randint(1, 46)
        values.append(random_value)


main()