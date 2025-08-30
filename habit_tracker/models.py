"""
Models for Habit Tracker.
"""

from datetime import datetime, timedelta
from typing import List, Optional

class Habit:
    """
    Represents a habit tracked by the user.
    """
    def __init__(self, name: str, periodicity: str, created_at: Optional[datetime] = None):
        """
        Initialize a new Habit.

        Args:
            name (str): Habit name/task specification.
            periodicity (str): 'daily' or 'weekly'.
            created_at (datetime, optional): Creation time. Defaults to now.
        """
        self.name = name
        self.periodicity = periodicity  # 'daily' or 'weekly'
        self.created_at = created_at or datetime.now()
        self.completions: List[datetime] = []

    def complete(self, timestamp: Optional[datetime] = None):
        """
        Mark habit as completed at given timestamp.

        Args:
            timestamp (datetime, optional): Completion time. Defaults to now.
        """
        self.completions.append(timestamp or datetime.now())

    def get_streak(self) -> int:
        """
        Calculate current streak length.

        Returns:
            int: Number of consecutive periods completed.
        """
        if not self.completions:
            return 0

        sorted_completions = sorted(self.completions)
        streak = 1
        last = sorted_completions[-1]

        period = timedelta(days=1) if self.periodicity == "daily" else timedelta(weeks=1)
        for prev in reversed(sorted_completions[:-1]):
            if (last - prev) <= period:
                streak += 1
                last = prev
            else:
                break
        return streak
