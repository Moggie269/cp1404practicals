"""
CP1404/CP5632 Practical
Taxi Simulator
Emiliano Mogorovich
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi
MENU = "Let's drive!\nq)uit, c)hoose taxi, d)rive"

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
         SilverServiceTaxi("Hummer", 200, 4)]
print(MENU)
menu_choice = input('>>> ').upper()
while menu_choice != 'Q':
    if menu_choice == 'C':
        pass
    elif menu_choice == 'D':
        pass
    else:
        print('Invalid option')
    print(MENU)
    menu_choice = input('>>> ').upper()