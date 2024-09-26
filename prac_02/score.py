"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    user_score = float(input("Enter score: "))
    user_result = determine_result(user_score)
    print(user_result)
    random_score = random.randint(1,100)
    random_result = determine_result(random_score)
    print(random_score, random_result)


def determine_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    else:
        if score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        else:
            return "Bad"


main()