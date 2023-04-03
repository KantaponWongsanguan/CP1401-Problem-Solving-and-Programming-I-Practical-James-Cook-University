import random
MAXIMUM = 45
MINIMUM = 1
NUM_PER_LINE = 6


def main():
    line_wanted = int(input("How many quick picks? "))
    while line_wanted <= 0:
        print("Invalid number of line")
        line_wanted = int(input("How many quick picks? "))

    for i in range(line_wanted):
        quick_picks = []
        while len(quick_picks) < NUM_PER_LINE:
            quick_picks.append(random.randint(MINIMUM, MAXIMUM))
        quick_picks.sort()
        print(" ".join(f"{quick_pick:2}" for quick_pick in quick_picks))


main()
