"""CP1404/CP5632 Practical - Guitar."""

class Guitar:
    def __init__(self, name='', year=0, cost=0):
        """Initialise a guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string form of guitar instance."""
        return f'{self.name} ({self.year}) : ${self.cost:,}'

    def __repr__(self):
        return str(self)

    def get_age(self):
        """Calculate age of guitar."""
        return 2024-self.year

    def is_vintage(self):
        """Determine if guitar is vintage."""
        if self.get_age() >= 50:
            return True
        else:
            return False