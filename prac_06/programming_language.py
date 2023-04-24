"""
Estimated: 20 min
Actual: 14 min
"""


class ProgrammingLanguage:
    """Representing programming language class"""

    def __init__(self, name, typing, reflection, year):
        """Set parameters to pass in for programming language"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Display languages detail"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Check if language typing is dynamic or not"""
        return self.typing == "Dynamic"
    