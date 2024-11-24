"""Band class for CP1404"""


class Band:
    """Band class"""

    def __init__(self, name=""):
        """Construct a Musician with a name and empty musician collection."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({self.musicians})"

    def add(self, musician_to_instrument):
        """Add a musician to band's collection."""
        self.musicians.append(musician_to_instrument)

    def play(self):
        """Return a string showing the musicians playing their first (or no) instrument."""
        return '\n'.join(musician.play() for musician in self.musicians)
