"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

MAX_SCORE = 100
MIN_SCORE = 0
PASS_SCORE = 50
EXCELLENT_SCORE = 90
score = float(input("Enter score: "))
if score < MIN_SCORE or score > MAX_SCORE:
    print("Invalid score")
elif MIN_SCORE <= score < PASS_SCORE:
    print("Bad")
elif PASS_SCORE <= score < EXCELLENT_SCORE:
    print("Passable")
elif EXCELLENT_SCORE <= score <= MAX_SCORE:
    print("Excellent")
