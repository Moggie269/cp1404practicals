MENU = "(E)ven numbers\n(O)dd numbers\n(S)quared numbers\n(Q)uit"

first_number = int(input('First number: '))
second_number = int(input('Second number: '))
while first_number >= second_number:
    print('Invalid number.')
    second_number = int(input('Second number: '))
print(MENU)
choice = input('Select option: ').upper()
while choice != 'Q':
    if choice == 'E':
        for i in range(first_number, second_number + 1):
            if i % 2 == 0:
                print(i, end=' ')
        print()
    elif choice == 'O':
        for i in range(first_number, second_number + 1):
            if i % 2 == 1:
                print(i, end=' ')
        print()
    elif choice == 'S':
        for i in range(first_number, second_number + 1):
            print(i ** 2, end=' ')
        print()
    else:
        print('Invalid choice.')
    print(MENU)
    choice = input('Select option: ').upper()
print('Farewell.')
