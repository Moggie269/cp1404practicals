"""
CP1404/CP5632 Practical
Wimbledon winners
"""


def main():
    winners = []
    winner_to_nationality = {}
    compile_list(winners)
    compile_dictionary(winner_to_nationality, winners)
    nationalities = compile_set(winner_to_nationality)
    for winner, nationality in winner_to_nationality.items():
        print(f'{winner} {nationality[1]}')
    print(sorted(nationalities))


def compile_list(winners):
    """Compile list of winners."""
    with open('wimbledon.csv', "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            if line[0].isnumeric():
                complete_match_information = line.strip().split(',')
                winners.append(complete_match_information[1:3])


def compile_dictionary(winner_to_nationality, winners):
    """Compile dictionary of winners and their nationalities."""
    for winner in winners:
        try:
            winner_to_nationality[winner[1]][1] += 1
        except KeyError:
            winner_to_nationality[winner[1]] = [winner[0], 1]


def compile_set(winner_to_nationality):
    """Compile set of nationalities."""
    nationalities = {nationality[0] for nationality in winner_to_nationality.values()}
    return nationalities


main()