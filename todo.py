# Created for Finals Assignment

tasks = []

while True:
    print("\n--- My To-Do List ---")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        new_task = input("Enter the task: ")
        tasks.append(new_task)
        print(f"Added: '{new_task}'")
    elif choice == '2':
        if not tasks:
            print("Your to-do list is empty!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
    elif choice == '3':
        print("Goodbye!!! Your task have been saved for this session brother.")
        break
    else:
        print("Invalid choice. Please try again.")
