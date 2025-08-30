"""
Predefined habits and example data for 4 weeks.
"""

from datetime import datetime, timedelta
from habit_tracker.models import Habit

def make_fixtures():
    base = datetime.now() - timedelta(weeks=4)
    habits = [
        Habit("Brush Teeth", "daily", base),
        Habit("Read Book", "daily", base),
        Habit("Workout", "daily", base),
        Habit("Go for a walk", "weekly", base),
        Habit("Visit grandparents", "weekly", base),
    ]
    # Add example completions
    for habit in habits:
        if habit.periodicity == "daily":
            for i in range(28):  # 4 weeks
                habit.complete(base + timedelta(days=i))
        else:
            for i in range(4):
                habit.complete(base + timedelta(weeks=i))
    return habits
