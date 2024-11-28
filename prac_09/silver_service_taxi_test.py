"""
CP1404/CP5632 Practical
Silver Service Taxi class test
"""
from skimage.color.rgb_colors import silver

from silver_service_taxi import SilverServiceTaxi

silver_taxi = SilverServiceTaxi('Fancy taxi', 100, 2)
driven_distance = silver_taxi.drive(18)
print(f'Driving {silver_taxi.name} for {driven_distance}km will cost you {silver_taxi.get_fare()}')

