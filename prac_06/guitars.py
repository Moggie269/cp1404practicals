"""
CP1404/CP5632 Practical
Guitar Test
Estimate: 20 minutes
Actual:   26 minutes
"""
from guitar import Guitar

guitars = []
name = input('Name:')
while name != '':
    year = int(input('Year:'))
    cost = float(input('Cost:'))
    guitar = Guitar(name,year,cost)
    print(guitar)
    guitars.append(guitar)
    name = input('Name:')
# guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
# guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

max_length = 0
for guitar in guitars:
    if len(guitar.name) > max_length:
        max_length = len(guitar.name)
for i, guitar in enumerate(guitars):
    if guitar.is_vintage():
        vintage_string = '(vintage)'
    else:
        vintage_string = ''
    print(f"Guitar {i+1}: {guitar.name:>{max_length}} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")