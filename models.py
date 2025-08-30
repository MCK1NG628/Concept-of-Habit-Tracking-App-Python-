import pytest
from datetime import datetime, timedelta
from habit_tracker.models import Habit

def test_habit_creation():
    h = Habit("Test", "daily")
    assert h.name == "Test"
    assert h.periodicity == "daily"
    assert isinstance(h.created_at, datetime)
    assert h.completions == []

def test_habit_complete_and_streak():
    h = Habit("Test", "daily")
    base = datetime.now() - timedelta(days=3)
    for i in range(4):
        h.complete(base + timedelta(days=i))
    assert h.get_streak() == 4
