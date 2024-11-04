"""
CP1404/CP5632 Practical
Emails
Estimate: 10 minutes
Actual:   11 minutes
"""
email_to_name = {}
email = input("Email: ")
while email != '':
    name_length = email.find('@')
    predicted_name = email[:name_length].title()
    choice = input(f'Is your name {predicted_name}? (y/n): ').lower()
    if choice == 'y' or choice == '':
        real_name = predicted_name
    else:
        real_name = input('Name: ').title()
    email_to_name[email] = real_name
    email = input("Email: ")
print()
for email, name in email_to_name.items():
    print(f'{name} ({email})')