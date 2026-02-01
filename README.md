Below is a **submission-ready `README.md`**.
You can copy-paste this directly into your repo. It is concise, professional, and aligned exactly with your code and the round’s expectations.

---

# Mini Task Manager (CLI)

A simple command-line task management system implemented in Python.
The project supports task creation, status updates with strict transition rules, task listing with filtering and sorting, basic metrics, and optional file-based persistence.

This was built as part of an internship coding round, with a focus on **clean logic, clear decisions, and explainability** rather than frameworks or boilerplate.

---

## Features

* Create tasks with validation (minimum title length)
* Update task status with **strict allowed transitions**
* List tasks with:

  * optional status filtering
  * sorting by creation time (ascending / descending)
* Metrics:

  * total number of tasks
  * count per status
  * average completion time for completed tasks
* In-memory storage with optional **JSON file persistence**
* CLI-based interaction (no external dependencies)

---

## Task Model

Each task contains the following fields:

* `id` – unique identifier (UUID string)
* `title` – required, minimum 3 characters
* `description` – optional
* `status` – one of: `todo`, `in_progress`, `done`
* `created_at` – UTC timestamp
* `updated_at` – UTC timestamp

Timestamps are stored internally in UTC and converted to IST for display.

---

## Status Transition Rules

Only the following transitions are allowed:

* `todo → in_progress`
* `todo → done`
* `in_progress → done`

Any other transition is rejected.

---

## How to Run

### Prerequisites

* Python 3.9 or higher (for `zoneinfo` support)
* No external libraries required

### Run the application

```bash
python task_manager.py
```

You will see an interactive CLI menu to:

* add tasks
* list tasks
* update task status
* view metrics
* exit the program

---

## Data Persistence

* Tasks are stored in memory during runtime.
* Tasks are also saved to a local `tasks.json` file for persistence.
* On startup, existing tasks are automatically loaded from the file.
* `tasks.json` is ignored via `.gitignore` and is not part of source control.

---

## Example Metrics Output

```text
METRICS
{
  'total_tasks': 3,
  'count_per_status': {'todo': 1, 'in_progress': 0, 'done': 2},
  'average_completion_time_seconds': 42.5
}
```

If no tasks are completed, the average completion time is returned as `None`.

---

## Design Decisions & Assumptions

* Used a **dictionary-based data model** instead of classes to keep logic explicit and simple.
* Implemented a clear state-machine (`ALLOWED_TRANSITIONS`) to enforce business rules.
* Chose a CLI interface over an API to minimize boilerplate and focus on core logic.
* Stored timestamps in UTC to avoid timezone issues; converted to IST only for display.
* Prioritized readability and explainability over advanced tooling.

---

## AI Usage Disclosure

AI tools (e.g., ChatGPT) were used in a **supportive role**, including:

* validating design decisions and edge cases
* reviewing logic for state transitions and metrics
* improving code structure and clarity

All core logic, validations, and final implementation were written, reviewed, and understood manually. AI-generated suggestions were modified as needed to align with the problem requirements.

---

## Possible Extensions

* Replace JSON persistence with a database
* Add argparse-based CLI commands
* Separate storage and business logic layers
* Expose functionality via an HTTP API

---

## Author

Harneet Kaur
harneetkaur4464@gmail.com

Internship coding assignment submission
Incredible Visibility
