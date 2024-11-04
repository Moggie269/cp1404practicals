"""
CP1404/CP5632 - Practical
Electricity bill estimator
"""
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print('Electricity bill estimator 2.0')
choice = input('Which tariff? 11 or 31: ')
while choice != '11' and choice != '31':
    print('Please enter either 11 or 31.')
    choice = input('Which tariff? 11 or 31: ')
daily_use_in_kwh = float(input('Enter daily use in kWh: '))
number_of_days = int(input('Enter number of billing days: '))
if choice == '11':
    estimated_bill = TARIFF_11 * daily_use_in_kwh * number_of_days
else:
    estimated_bill = TARIFF_31 * daily_use_in_kwh * number_of_days
print(f'Estimated bill: ${estimated_bill:.2f}')
