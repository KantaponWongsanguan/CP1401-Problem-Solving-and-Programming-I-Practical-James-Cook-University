"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
when the argument is correct data type but an inappropriate value ie float, string.
2. When will a ZeroDivisionError occur?
when the value is being divided by 0 which is not possible ie in this case when denominator is inputted as 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    # To avoid the possibility of ZeroDivisionError
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
