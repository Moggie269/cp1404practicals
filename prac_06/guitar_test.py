"""
CP1404/CP5632 Practical - Guitar Test
"""
from guitar import Guitar

guitar = Guitar("Gibson L-5 CES",1922,16035.40)
another_guitar = Guitar('Another Guitar', 2013)
first_line = input(f'{guitar.name} get_age() - Expected ' )
print(f'Got {guitar.get_age()}')
second_line = input(f'{guitar.name} get_age() - Expected ' )
print(f'Got {another_guitar.get_age()}')
third_line = input(f'{guitar.name} is_vintage() - Expected ' )
print(f'Got {guitar.is_vintage()}')
fourth_line = input(f'{guitar.name} is_vintage() - Expected ' )
print(f'Got {another_guitar.is_vintage()}')