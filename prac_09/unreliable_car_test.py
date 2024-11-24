"""
CP1404/CP5632 Practical
Unreliable Car test
"""
from unreliable_car import UnreliableCar

unreliable_car = UnreliableCar('Some car', 100, 0)
driven_km = unreliable_car.drive(100)
print(f'{unreliable_car.name} has fuel {unreliable_car.fuel}. It has driven {driven_km}km')

unreliable_car_2 = UnreliableCar('Another car', 100, 69.9)
driven_km_2 = unreliable_car_2.drive(100)
print(f'{unreliable_car_2.name} has fuel {unreliable_car_2.fuel}. It has driven {driven_km_2}km')

unreliable_car_3 = UnreliableCar('A third car', 100, 100)
driven_km_3 = unreliable_car_3.drive(100)
print(f'{unreliable_car_3.name} has fuel {unreliable_car_3.fuel}. It has driven {driven_km_3}km')

