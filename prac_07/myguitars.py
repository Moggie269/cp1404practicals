"""CP1404/CP5632 Practical - Guitar."""
from guitar import Guitar


def main():
    guitars = []
    read_guitars(guitars)
    guitars.sort()
    display_guitars(guitars)


def read_guitars(guitars):
    with open('guitars.csv', 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], parts[1], parts[2])
            guitars.append(guitar)


def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)


main()
