from habit_tracker.models import Habit
from habit_tracker.analytics import get_all_habits, habits_by_periodicity, longest_streak, longest_streak_for_habit
from datetime import datetime, timedelta

def test_analytics_functions():
    base = datetime.now() - timedelta(days=3)
    habits = [
        Habit("A", "daily", base),
        Habit("B", "weekly", base)
    ]
    for i in range(4):
        habits[0].complete(base + timedelta(days=i))
    for i in range(2):
        habits[1].complete(base + timedelta(weeks=i))
    assert get_all_habits(habits) == ["A", "B"]
    assert habits_by_periodicity(habits, "daily") == ["A"]
    assert habits_by_periodicity(habits, "weekly") == ["B"]
    assert longest_streak(habits) == 4
    assert longest_streak_for_habit(habits[1]) == 2
