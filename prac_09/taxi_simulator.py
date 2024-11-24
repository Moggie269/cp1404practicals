"""
CP1404/CP5632 Practical
Taxi Simulator
Emiliano Mogorovich
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi
MENU = "Let's drive!\nq)uit, c)hoose taxi, d)rive"

def main():
    """Display menu and get menu choice."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    bill_to_date = 0
    current_taxi = None
    print(MENU)
    choice = input('>>> ').upper()
    while choice != 'Q':
        if choice == 'C':
            print('Taxis available: ')
            for i, taxi in enumerate(taxis):
                print(f'{i} - {taxi}')
            current_taxi = get_valid_taxi_choice(taxis)
        elif choice == 'D':
            pass
        else:
            print('Invalid option')
        print(f'Bill to date: ${bill_to_date:.2f}')
        print(current_taxi)
        print(MENU)
        choice = input('>>> ').upper()


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