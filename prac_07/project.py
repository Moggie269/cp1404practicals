from datetime import datetime


class Project:
    """Create Project instance."""

    def __init__(self, name='', start_date='', priority=0, cost_estimate=0, completion_percentage=0):
        """Initialize Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"{self.name}  {self.start_date}  {self.priority}  {self.cost_estimate}  {self.completion_percentage}"

    def __repr__(self):
        return str(self)

    def __gt__(self, other):
        return self.priority > other.priority

    def is_complete(self):
        return self.completion_percentage >= 100

    def has_started_after_date(self, other):
        if self.start_date > other:
            return True
        else:
            return False