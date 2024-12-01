"""CP1404/CP5632 Practical - Programming Languages."""


class ProgrammingLanguage:
    def __init__(self, name='', typing='', reflection='', year=0):
        """Initialise a programming language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if programming language is dynamic."""
        if self.typing == 'Dynamic':
            return True

    def __str__(self):
        """Return a string representation of the programming language."""
        return f'{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}'

    def __repr__(self):
        return str(self)