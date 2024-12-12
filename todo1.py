tasks = []

# Define a function to add a task
def add_task():
    task_name = input("Enter the task: ")
    task_description = input("Enter the description for the task: ")
    task_id = len(tasks) + 1 
    tasks.append({
        'task_id': task_id,
        'task': task_name,
        'description': task_description,
        'completed': False
    })
    print(f"Task '{task_name}' with description '{task_description}' added.")
    
# Function to view a specific task by Index
def view_task_index():
    show_tasks()
    
    # Find the task with the given task Index
    task_found = False
    for index, task in enumerate(tasks):
            status = "Completed" if task['completed'] else "Not Completed"
            print(f"Description: {task['description']}, Status: {status} ")
            task_found = True
            delete_task()
            break
    
    if not task_found:
        print(f"No task found.")
    
# Define a function to show the tasks
def show_tasks():
    if not tasks:
        print("No tasks to show. ")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks,1):
            print(f"{i}. {task['task']} - {'Completed' if task['completed'] else 'pending'}")
            
# Define a function to update task
def update_task():
    show_tasks()
    try:
        task_index = int(input("Enter the task number to update: ")) - 1
        if task_index < 0 or task_index >= len(tasks):
            print("Invalid task number. ")
            return
        new_task = input("Enter the updated task: ")
        tasks[task_index]['task'] = new_task
        print("Task updated successfully.")
    except ValueError:
        print("Please enter a valid task number.")
        
# Define a function to mark a task as complete
def complete_task():
    show_tasks()
    try:
         task_index = int(input("Enter the task number to mark as completed: ")) - 1
         if task_index < 0 or task_index >= len(tasks):
             print("Invalid task number. ")
             return
         tasks[task_index]['completed'] = True
         print("Task marked as completed.")
    except ValueError:
         print("Please enter a valid task number.")
         
# Define a function to delete a task
def delete_task():
    show_tasks()
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        if task_index < 0 or task_index >= len(tasks):
            print("Invalid task number.")
            return
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task['task']}' deleted.")
    except ValueError:
        print("Please enter a valid task number.")
        
    

# Main function to interact with the user
def main():
    while True:
        print("\nTO-DO List App")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Complete Task")
        print("5. Delete Task")
        print("6. View Task")
        print("7. Exit")
        
        
        
        choice = input("Choose an option 1-6: ")
        
        if choice == "1":
           show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            complete_task()
        elif choice == '5':
            delete_task()
        elif choice == '6':
            view_task_index()
        elif choice == '7':
            print("Exiting the To-Do List app. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 6.")
            break
        
        
main()
        
        

            