# To-Do List App

class Task:
    def __init__(self, description):
        self.description = description
        self.done = False

    def mark_done(self):
        self.done = True

    def __str__(self):
        status = "Done" if self.done else "Pending"
        return f"{self.description} - {status}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_tasks(self):
        for task in self.tasks:
            print(task)


# Example usage:
todo = ToDoList()
task1 = Task("Study Python")
task2 = Task("Go to gym")

todo.add_task(task1)
todo.add_task(task2)
todo.show_tasks()

task1.mark_done()
todo.show_tasks()
