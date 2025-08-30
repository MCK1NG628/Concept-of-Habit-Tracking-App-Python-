"""
Analytics module using functional programming.
"""

from typing import List
from habit_tracker.models import Habit

def get_all_habits(habits: List[Habit]) -> List[str]:
    """
    Return names of all habits.
    """
    return list(map(lambda h: h.name, habits))

def habits_by_periodicity(habits: List[Habit], periodicity: str) -> List[str]:
    """
    Return names of habits with given periodicity.
    """
    return list(map(lambda h: h.name, filter(lambda h: h.periodicity == periodicity, habits)))

def longest_streak(habits: List[Habit]) -> int:
    """
    Return the longest streak across all habits.
    """
    return max(map(lambda h: h.get_streak(), habits), default=0)

def longest_streak_for_habit(habit: Habit) -> int:
    """
    Return the longest streak for a single habit.
    """
    return habit.get_streak()
