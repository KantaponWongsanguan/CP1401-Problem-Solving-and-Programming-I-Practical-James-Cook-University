MENU = """C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"""


def main():
    """Temperature conversion with functions"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = get_fahrenheit_from_celsius(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = get_celsius_fahrenheit(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def get_fahrenheit_from_celsius(celsius):
    """Convert Fahrenheit from Celsius"""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def get_celsius_fahrenheit(fahrenheit):
    """Convert Celsius from Fahrenheit"""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()
