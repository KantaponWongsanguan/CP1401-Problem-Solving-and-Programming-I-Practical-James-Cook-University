"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""
result = ""
is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))

        # quite the loop when valid integer is accepted.
        is_finished = True

    except ValueError:  # ValueError exception for unwanted type of data
        print("Please enter a valid integer.")
print("Valid result is:", result)
