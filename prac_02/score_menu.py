"""
CP1404/CP5632 - Practical
Score menu program
"""
MENU = "(G)et score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    score = 0
    print(MENU)
    choice = input(">>>: ").upper()
    while choice != 'Q':
        if choice == 'G':
            score = get_valid_score("Score: ", 0, 100)
        elif choice == 'P':
            result = determine_result(score)
            print(result)
        elif choice == 'S':
            pass
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>>: ").upper()
    print("Farewell")


def get_valid_score(prompt, low, high):
    score = int(input(prompt))
    while score < low or score > high:
        print("Invalid score")
        score = int(input(prompt))
    return score


def determine_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()