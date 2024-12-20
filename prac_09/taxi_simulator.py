"""
CP1404/CP5632 Practical
Taxi Simulator
Emiliano Mogorovich
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi
MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    """Display menu and get menu choice."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    bill = 0
    current_taxi = None
    print("Let's drive!")
    print(MENU)
    choice = input('>>> ').upper()
    while choice != 'Q':
        if choice == 'C':
            print('Taxis available: ')
            display_available_taxi(taxis)
            current_taxi = get_valid_taxi_choice(taxis)
        elif choice == 'D':
            if current_taxi is None:
                print('You need to choose a taxi before you can drive')
            else:
                distance = int(input('Drive how far? '))
                current_taxi.start_fare()
                current_taxi.drive(distance)
                fare = current_taxi.get_fare()
                bill += fare
                print(f'Your {current_taxi.name} trip will cost you ${fare:.2f}')
        else:
            print('Invalid option')
        print(f'Bill to date: ${bill:.2f}')
        print(MENU)
        choice = input('>>> ').upper()
    print(f'Taxis are now:')
    display_available_taxi(taxis)


def display_available_taxi(taxis):
    """Display available taxi."""
    for i, taxi in enumerate(taxis):
        print(f'{i} - {taxi}')


def get_valid_taxi_choice(taxis):
    """Get a valid taxi choice."""
    taxi_choice = int(input('Choose taxi: '))
    try:
        current_taxi = taxis[taxi_choice]
        return current_taxi
    except IndexError:
        print('Invalid taxi choice')



if __name__ == '__main__':
    main()