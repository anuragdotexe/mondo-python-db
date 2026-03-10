from database import get_database

db = get_database()
tasks_collection = db["tasks"]

def show_all_tasks():
    # .find({}) with an empty dictionary means "Give me everything"
    all_tasks = tasks_collection.find()
    
    print("\n--- CURRENT TASK LIST ---")
    for task in all_tasks:
        name = task.get("task_name")
        priority = task.get("priority")
        status = task.get("status")
        print(f"[{priority}] {name} - Status: {status}")

def find_high_priority():
    # This acts like a filter: SELECT * WHERE priority = 'High'
    query = {"priority": "High"}
    high_tasks = tasks_collection.find(query)
    
    print("\n--- HIGH PRIORITY ONLY ---")
    for task in high_tasks:
        print(f"!! {task.get('task_name')}")

# Run the functions
show_all_tasks()
find_high_priority()