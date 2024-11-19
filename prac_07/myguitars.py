"""CP1404/CP5632 Practical - Guitar."""
from guitar import Guitar


def main():
    guitars = []
    read_guitars(guitars)
    guitars.sort()
    display_guitars(guitars)
    add_guitars(guitars)
    save_guitars(guitars)


def read_guitars(guitars):
    """Read guitars from csv file."""
    with open('guitars.csv', 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], parts[1], parts[2])
            guitars.append(guitar)


def display_guitars(guitars):
    """Display guitars."""
    for guitar in guitars:
        print(guitar)


def add_guitars(guitars):
    """Generate new guitars."""
    name = input('Name:')
    while name != '':
        year = int(input('Year:'))
        cost = float(input('Cost:'))
        guitar = Guitar(name, year, cost)
        print(guitar)
        guitars.append(guitar)
        name = input('Name:')


def save_guitars(guitars):
    """Save guitars to csv file."""
    with open('guitars.csv', 'w') as out_file:
        for guitar in guitars:
            out_file.write(f'{guitar.name},{guitar.year},{guitar.cost}\n')


main()
