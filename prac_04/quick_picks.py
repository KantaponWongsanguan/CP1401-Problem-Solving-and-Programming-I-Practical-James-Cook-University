import random
MAXIMUM = 45
MINIMUM = 1
NUM_PER_LINE = 6


def main():
    """Function to ask user how many "quick picks" then generate that many line with 6 random numbers each"""
    line_wanted = int(input("How many quick picks? "))

    while line_wanted <= 0:    # line input validating
        print("Invalid number of line")
        line_wanted = int(input("How many quick picks? "))

    for i in range(line_wanted):
        quick_picks = []
        while len(quick_picks) < NUM_PER_LINE:
            random_number = random.randint(MINIMUM, MAXIMUM)

            while random_number in quick_picks:          # checking if the random num exists in the list
                random_number = random.randint(MINIMUM, MAXIMUM)
            quick_picks.append(random_number)

        quick_picks.sort()
        print(" ".join(f"{quick_pick:2}" for quick_pick in quick_picks))


main()
