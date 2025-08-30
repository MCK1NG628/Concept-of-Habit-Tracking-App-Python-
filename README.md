# Habit Tracking App

A simple Python backend for tracking habits using object-oriented and functional programming.

## Features

- Add, complete, and analyze habits (daily/weekly)
- Analytics (longest streak, habits by type, etc.)
- Save/load data (JSON)
- 5 predefined habits and 4 weeks of test data
- Command Line Interface (CLI)
- Unit tests included

## Installation

```bash
git clone https://github.com/MCK1NG628/Concept-of-Habit-Tracking-App-Python-.git
cd Concept-of-Habit-Tracking-App-Python-
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

Follow the prompts to add, complete, and analyze habits.

## Testing

```bash
pytest
```

## Adding Habits

Use the CLI to add new habits. Example:

1. Select "Add habit" from the menu.
2. Enter a name and periodicity ("daily" or "weekly").

## Completing Habits

Select "Complete habit" and enter the habit name.

## Data Persistence

All habit data is saved in `habits.json`.

## Documentation

All code is documented with Python docstrings.

## Abstract

See `abstract.pdf` for a summary and technical report.

## License

MIT
