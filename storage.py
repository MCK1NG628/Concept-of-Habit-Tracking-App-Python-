import os
from habit_tracker.models import Habit
from habit_tracker.storage import save_habits, load_habits
from datetime import datetime

def test_save_and_load(tmp_path):
    habit = Habit("Test", "daily")
    habit.complete(datetime.now())
    file_path = tmp_path / "habits.json"
    save_habits([habit], file_path)
    habits = load_habits(file_path)
    assert len(habits) == 1
    assert habits[0].name == "Test"
    assert len(habits[0].completions) == 1
