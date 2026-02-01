import json
import uuid
import os
from datetime import datetime
from zoneinfo import ZoneInfo

# Set timezone to Indian Standard Time (IST) for display purposes
IST = ZoneInfo("Asia/Kolkata")
DATA_FILE = 'tasks.json'

# Global list to store task dictionaries in memory
tasks=[]

# Define business rules for valid statuses
ALLOWED_STATUSES = {'todo', 'in_progress', 'done'}

# Define strict rules for moving between statuses (State Machine Logic)
ALLOWED_TRANSITIONS = {
    "todo": {"in_progress", "done"},
    "in_progress": {"done"},
    "done": set() # Once done, a task cannot change status
}

def to_ist(dt):
    """
    Converts a datetime object to IST for user-friendly display.
    Handles 'naive' datetimes (no timezone) by assuming they are UTC first.
    """
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=ZoneInfo("UTC"))
    return dt.astimezone(IST)

def save_tasks():
    """
    Persists the current in-memory tasks list to a JSON file.
    Converts datetime objects to strings (ISO format) for storage.
    """
    data_to_save = []
    for t in tasks:
        # Create a shallow copy to avoid modifying the actual runtime objects
        item = t.copy() 
        item['created_at'] = item['created_at'].isoformat()
        item['updated_at'] = item['updated_at'].isoformat()
        data_to_save.append(item)
        
    with open(DATA_FILE, "w") as f:
        json.dump(data_to_save, f, indent=2)

def load_tasks():
    """
    Loads tasks from JSON file into memory on startup.
    Parses ISO strings back into Python datetime objects.
    """
    global tasks
    # If file doesn't exist (first run), start with empty list
    if not os.path.exists(DATA_FILE):
        return 
        
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            
        tasks = []
        for item in data:
            # Parse strings back to datetime
            c_at = datetime.fromisoformat(item['created_at'])
            u_at = datetime.fromisoformat(item['updated_at'])
            
            if c_at.tzinfo is not None:
                c_at = c_at.replace(tzinfo=None)
            if u_at.tzinfo is not None:
                u_at = u_at.replace(tzinfo=None)
                
            item['created_at'] = c_at
            item['updated_at'] = u_at
            tasks.append(item)
        print(f"Loaded {len(tasks)} tasks.")
    except Exception as e:
        print(f"Warning: Could not load file ({e}). Starting empty.")
        tasks = []

def print_task(task):
    """Helper to print a single task in a readable format."""
    print(f"ID        : {task['id']}")
    print(f"Title     : {task['title']}")
    print(f"Description: {task['description']}")
    print(f"Status    : {task['status']}")
    # Display times in IST for the user
    print(f"Created At: {to_ist(task['created_at']).strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Updated At: {to_ist(task['updated_at']).strftime('%Y-%m-%d %H:%M:%S')}")
    print("\n")

def create_task(title, description = None):
    """Validates input and adds a new task to the list."""
    if not title or len(title.strip()) < 3:
        raise ValueError("Task title must be at least 3 characters long.")
    # Use UTC for internal storage to avoid timezone confusion
    now = datetime.utcnow()

    task = {
        "id":str(uuid.uuid4()), # Generate unique ID
        "title":title.strip(),
        "description":description,
        "status":"todo", # Default status
        "created_at":now,
        "updated_at":now
    }

    tasks.append(task)
    save_tasks()
    print("Task created successfully.")
    return task

def get_task_by_id(task_id):
    """Finds a task by its UUID string."""
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None

def update_status(task_id,new_status):
    """
    Updates a task's status, enforcing valid transitions.
    Example: Prevents moving a 'done' task back to 'todo'.
    """
    if new_status not in ALLOWED_STATUSES:
        raise ValueError(f"Invalid status: {new_status}. Choose from {ALLOWED_STATUSES}")

    task = get_task_by_id(task_id)
    if not task:
        raise ValueError("Task not found.")

    current_status = task['status']

    if new_status == current_status:
        return task
    
    if new_status not in ALLOWED_TRANSITIONS[current_status]:
        raise ValueError(f"Invalid transition from '{current_status}' to '{new_status}'.")

    task['status'] = new_status
    task['updated_at'] = datetime.utcnow()
    save_tasks()
    print("Status updated!")
    return task

def list_tasks(status=None, sort_order="desc"):
    result = tasks
    if status:
        result = [t for t in result if t['status'] == status]

    reverse = True if sort_order == "desc" else False
    return sorted(result, key=lambda t: t['created_at'], reverse=reverse)
                

def metrics():
    """Calculates total counts and average completion time."""
    counts = {status: 0 for status in ALLOWED_STATUSES}
    completed_tasks = []

    for task in tasks:
        counts[task['status']] += 1
        if task['status'] == 'done':
            completed_tasks.append(task)

    avg_time = None
    if completed_tasks:
        total_seconds =  sum(
            (t['updated_at'] - t['created_at']).total_seconds()
            for t in completed_tasks)
        avg_time = total_seconds / len(completed_tasks)
    
    return {
        "total_tasks": len(tasks),
        "count_per_status": counts,
        "average_completion_time_seconds": avg_time
    }

def main():
    load_tasks()

    while True:
        print("\nTASK MANAGER")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Status")
        print("4. Show Metrics")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        try:
            if choice == '1':
                t = input("Title: ")
                d = input("Description: ")
                create_task(t, d)
            
            elif choice == '2':
                filter_choice = input("Filter by status? (leave empty for all): ").strip()
                # Validate filter input
                if filter_choice and filter_choice not in ALLOWED_STATUSES:
                    print("Invalid status filter.")
                    continue
                    
                order = input("Sort order (asc/desc, default desc): ").strip() or "desc"
                found_tasks = list_tasks(filter_choice if filter_choice else None, order)

                
                print(f"\nListing {len(found_tasks)} tasks:")
                for t in found_tasks:
                    print_task(t)
                            
            elif choice == '3':
                tid = input("Task ID: ")
                # Show valid options to user
                print("Options: todo / in_progress / done")
                stat = input("New Status: ")
                update_status(tid, stat)
                
            elif choice == '4':
                data = metrics()
                print("\nMETRICS")
                print(data)
                
            elif choice == '5':
                print("Exiting. Bye!")
                break
            else:
                print("Invalid choice, try again.")

        except ValueError as e:
                # Catch validation errors (e.g. short title, invalid status)
                print(f"ERROR: {e}")
        except Exception as e:
                print(f"UNEXPECTED ERROR: {e}")


if __name__ == "__main__":
    main()