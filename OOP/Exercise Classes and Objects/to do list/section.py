
from task import Task
class Section:

    def __init__(self,name):
        self.name =name
        self.tasks = []

    def add_task(self,new_task: Task):
        if new_task in self.tasks:
            return f'Task is already in the section {self.name}'

        self.tasks.append(new_task)
        return f'Task {new_task.details()} is added to the section'

    def complete_task(self,task_name: str):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        removed = [x for x in self.tasks if x.completed]
        self.tasks = [x for x in self.tasks if not x.completed]
        return f"Cleared {len(removed)} tasks."

    def view_section(self):
        tasks_details = "\n".join(task.details() for task in self.tasks)
        return f"Section {self.name}:\n{tasks_details}"
