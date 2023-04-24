
def main():
    """This program will ask user for 5 numbers and store them in a list and output info about these numbers"""
    print("Please enter 5 numbers")
    numbers = []
    for num in range(1, 6):
        number_input = int(input("Number: "))
        numbers.append(number_input)

    """Display list information"""
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the number is {sum(numbers)/ len(numbers)}")


main()


"""Part 2"""
"""Woefully inadequate security checker"""
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username_to_check = str(input("Your username is >>"))
if username_to_check in usernames:
    print("Access granted")
else:
    print("Access denied")
