"""
Persistence layer for Habit Tracker.
"""

import json
import os
from datetime import datetime
from typing import List
from habit_tracker.models import Habit

DATA_FILE = "habits.json"

def save_habits(habits: List[Habit], filename: str = DATA_FILE):
    """
    Save habits to JSON file.
    """
    data = []
    for h in habits:
        data.append({
            "name": h.name,
            "periodicity": h.periodicity,
            "created_at": h.created_at.isoformat(),
            "completions": [dt.isoformat() for dt in h.completions]
        })
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

def load_habits(filename: str = DATA_FILE) -> List[Habit]:
    """
    Load habits from JSON file.
    """
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as f:
        data = json.load(f)
    habits = []
    for h in data:
        habit = Habit(h["name"], h["periodicity"], datetime.fromisoformat(h["created_at"]))
        habit.completions = [datetime.fromisoformat(dt) for dt in h["completions"]]
        habits.append(habit)
    return habits
