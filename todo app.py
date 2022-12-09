import tkinter as tk
from datetime import datetime

class Task:
    def __init__(self, description, date):
        self.description = description
        self.date = date
        self.is_completed = False

# Create the main window
root = tk.Tk()
root.geometry("500x500")
root.title("To-Do App")

# Create a list to store the tasks
tasks = []

# Function to add a task to the list
def add_task():
    # Get the task from the input field
    description = task_entry.get()

    # Get the date from the input field
    date_string = date_entry.get()
    date = datetime.strptime(date_string, "%Y-%m-%d").date()

    # Create a new task
    task = Task(description, date)

    # Add the task to the list
    tasks.append(task)

    # Clear the input fields
    task_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)

# Function to mark a task as complete
def complete_task():
    # Get the selected task from the list
    index = task_listbox.curselection()[0]
    task = tasks[index]

    # Mark the task as complete
    task.is_completed = True

# Function to view all tasks
def view_tasks():
    # Clear the listbox
    task_listbox.delete(0, tk.END)

    # Loop through the tasks and add them to the listbox
    for task in tasks:
        task_listbox.insert(tk.END, task.description)

# Create a frame to hold the input fields
input_frame = tk.Frame(root)
input_frame.pack()

# Create a label for the task input field
task_label = tk.Label(input_frame, text="Task:")
task_label.pack(side=tk.LEFT)

# Create an input field for adding tasks
task_entry = tk.Entry(input_frame)
task_entry.pack(side=tk.LEFT)

# Create a label for the date input field
date_label = tk.Label(input_frame, text="Date (YYYY-MM-DD):")
date_label.pack(side=tk.LEFT)

# Create an input field for adding dates
date_entry = tk.Entry(input_frame)
date_entry.pack(side=tk.LEFT)

# Create a frame to hold the buttons
button_frame = tk.Frame(root)
button_frame.pack()

# Create a button for adding tasks
add_task_button = tk.Button(button_frame, text="Add Task", command=add_task)
add_task_button.pack(side=tk.LEFT)

# Create a button for marking

complete_task_button = tk.Button(button_frame, text="Complete Task", command=complete_task)
complete_task_button.pack(side=tk.LEFT)


view_tasks_button = tk.Button(button_frame, text="View Tasks", command=view_tasks)
view_tasks_button.pack(side=tk.LEFT)


task_listbox = tk.Listbox(root)
task_listbox.pack()


root.mainloop()