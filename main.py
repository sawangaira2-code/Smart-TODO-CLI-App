class TodoApp:
    def __init__(self):
        self.tasks = []
        self.load_tasks()
        self.menu()

    def menu(self):
        while True:
            user_input = input("""
--- TO-DO APP ---
1. Add Task
2. Show Tasks
3. Delete Task
4. Exit
Choose: """)

            if user_input == "1":
                self.add_task()
            elif user_input == "2":
                self.show_tasks()
            elif user_input == "3":
                self.delete_task()
            elif user_input == "4":
                self.save_tasks()
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")

    def add_task(self):
        task = input("Enter task: ")
        self.tasks.append(task)
        print("Task added!")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def delete_task(self):
        self.show_tasks()
        try:
            task_no = int(input("Enter task number to delete: "))
            if 1 <= task_no <= len(self.tasks):
                removed = self.tasks.pop(task_no - 1)
                print(f"Deleted: {removed}")
            else:
                print("Invalid number")
        except:
            print("Enter valid number")

    def save_tasks(self):
        with open("tasks.txt", "w") as f:
            for task in self.tasks:
                f.write(task + "\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                self.tasks = [line.strip() for line in f]
        except:
            self.tasks = []


# Run App
app = TodoApp()
