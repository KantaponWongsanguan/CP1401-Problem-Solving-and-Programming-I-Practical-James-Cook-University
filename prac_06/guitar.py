"""
Estimate: 15 min
Actual: 18
"""
PRESENT_YEAR = 2023
VINTAGE_AGE = 50


class Guitar:
    """Representing Guitar Class"""

    def __init__(self, name, year, cost):
        """Set parameters to pass guitar detail to"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Display guitar details"""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """returns guitar age"""
        return PRESENT_YEAR - self.year

    def is_vintage(self):
        """Determine if guitar is vintage(50 years older)"""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Less than, used for sorting Guitars - by year released."""
        return self.year < other.year
