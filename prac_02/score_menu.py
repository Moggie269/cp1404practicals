"""
CP1404/CP5632 - Practical
Score menu program
"""

def main():
    print(MENU)
    choice = input(">>>: ").upper()
    while choice != 'Q':
        if choice == 'G':
            pass
        elif choice == 'P':
            pass
        elif choice == 'S':
            pass
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>>: ").upper()
    print("Farewell")
