import sys
from database import get_database
from datetime import datetime

# Initialize connection
db = get_database()
tasks = db["tasks"]

def print_menu():
    print("\n--- 🛠️  MONGODB TASK MANAGER ---")
    print("1. View All Tasks")
    print("2. Add New Task")
    print("3. Mark Task as Completed")
    print("4. Delete a Task")
    print("5. Exit")

def main():
    while True:
        print_menu()
        choice = input("Select an option (1-5): ")

        if choice == "1":
            all_docs = tasks.find()
            print("\nYOUR TASKS:")
            for doc in all_docs:
                status_icon = "✅" if doc.get("status") == "Completed" else "⏳"
                print(f"{status_icon} [{doc.get('priority')}] {doc.get('task_name')}")

        elif choice == "2":
            name = input("Task Name: ")
            pri = input("Priority (Low/High/Critical): ")
            tasks.insert_one({
                "task_name": name, 
                "priority": pri, 
                "status": "Pending",
                "created_at": datetime.now()
            })
            print("Task Saved!")

        elif choice == "3":
            name = input("Which task did you finish? ")
            tasks.update_one({"task_name": name}, {"$set": {"status": "Completed"}})
            print("Updated!")

        elif choice == "4":
            name = input("Task name to delete: ")
            # THE 'D' IN CRUD: DELETE
            result = tasks.delete_one({"task_name": name})
            if result.deleted_count > 0:
                print("Task removed from database.")
            else:
                print("Task not found.")

        elif choice == "5":
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()