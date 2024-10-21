"""
CP1404/CP5632 Practical
Colours in a dictionary
"""
COLOURS = {'Blanched Almond': '#ffebcd', 'Bright Turquoise': '#08e8de', 'Dodger Blue1': '#1e90ff', 'Falu Red': '#801818',
           'Kombu Green': '#354230', 'Puce': '#cc8899', 'Salmon4': '#8b4c39', 'Timberwolf': '#dbd7d2', 'Windsor Tan': '#a75502'}

choice = input('Select colour: ').title()
while choice != '':
    try:
        print(COLOURS[choice])
    except KeyError:
        print('Invalid choice.')
    choice = input('Select colour: ').title()