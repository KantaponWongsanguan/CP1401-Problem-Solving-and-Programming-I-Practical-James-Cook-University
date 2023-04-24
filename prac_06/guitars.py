"""
Estimate: 30min
Actual: 35 min
"""
from prac_06.guitar import Guitar


def main():
    """Store Guitar info inputs and display them in a list"""
    print("My guitars!")
    guitars = []

    name = input("Name: ")
    while name != "":
        new_guitar = add_guitar(name, guitars)
        guitars.append(new_guitar)
        print(new_guitar, "added.")
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        guitars.sort()
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print("No guitars :( Quick, go and buy one!")


def add_guitar(name, guitars):
    """add new guitar info"""
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar_to_add = Guitar(name, year, cost)
    return guitar_to_add


main()
