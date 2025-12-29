class Task:
    def __init__(self, title: str, completed: bool = False):
        self.title = title
        self.completed = completed

    def toggle_completed(self):
        self.completed = not self.completed

    def __repr__(self):
        status = "✓" if self.completed else "✗"
        return f"{status} {self.title}"


class TaskModel:
    def __init__(self):
        self.tasks = []

    def add_task(self, title: str):
        task = Task(title)
        self.tasks.append(task)

    def get_all_tasks(self):
        return self.tasks

    def toggle_task(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks[index].toggle_completed()
