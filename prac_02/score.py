"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

MAX_SCORE = 100
MIN_SCORE = 0
PASS_SCORE = 50
EXCELLENT_SCORE = 90


def main():
    """Program to determine grade with the inout score"""
    score = float(input("Enter score: "))
    print(get_grade(score))


def get_grade(score):
    """Function to determine grade according to score"""
    if score < MIN_SCORE or score > MAX_SCORE:
        return "Invalid score"
    elif MIN_SCORE <= score < PASS_SCORE:
        return "Bad"
    elif PASS_SCORE <= score < EXCELLENT_SCORE:
        return "Passable"
    elif EXCELLENT_SCORE <= score <= MAX_SCORE:
        return "Excellent"


main()
