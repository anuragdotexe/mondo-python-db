from database import get_database
from datetime import datetime

db = get_database()
tasks_collection = db["tasks"]

def add_task(name, priority):
    new_task = {
        "task_name": name,
        "priority": priority,
        "status": "Pending",
        "created_at": datetime.now()
    }
    result = tasks_collection.insert_one(new_task)
    print(f"Task created with ID: {result.inserted_id}")

# Let's test it!
add_task("Finish Python Setup", "High")
add_task("Build MongoDB Project", "Critical")