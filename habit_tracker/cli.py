"""
Command Line Interface for Habit Tracker.
"""

from habit_tracker.storage import save_habits, load_habits
from habit_tracker.analytics import *
from habit_tracker.fixtures import make_fixtures
from habit_tracker.models import Habit

def main():
    habits = load_habits()
    if not habits:
        habits = make_fixtures()
        save_habits(habits)
    print("Welcome to the Habit Tracker!")
    while True:
        print("\nMenu:\n1. List habits\n2. Add habit\n3. Complete habit\n4. Analytics\n5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            for h in habits:
                print(f"{h.name} ({h.periodicity})")
        elif choice == "2":
            name = input("Habit name: ")
            period = input("Periodicity (daily/weekly): ")
            habits.append(Habit(name, period))
            save_habits(habits)
        elif choice == "3":
            name = input("Habit to complete: ")
            for h in habits:
                if h.name == name:
                    h.complete()
                    print(f"Completed {name}!")
                    save_habits(habits)
                    break
            else:
                print("Habit not found.")
        elif choice == "4":
            print("Analytics:")
            print("All habits:", get_all_habits(habits))
            print("Daily habits:", habits_by_periodicity(habits, "daily"))
            print("Weekly habits:", habits_by_periodicity(habits, "weekly"))
            print("Longest streak (all):", longest_streak(habits))
            name = input("Habit for streak: ")
            for h in habits:
                if h.name == name:
                    print("Longest streak for", name, longest_streak_for_habit(h))
        elif choice == "5":
            break

if __name__ == "__main__":
    main()
