from typing import List, Optional
from app.models.task_model import Task
from app.repositories.task_repository import TaskRepository

class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def create_task(self, title: str, description: Optional[str], status: str):
        new_task = Task(title=title, description=description, status=status)
        return self.repository.create_task(new_task)

    def get_task_by_id(self, task_id: int):
        return self.repository.get_task_by_id(task_id)

    def update_task(self, task_id: int, title: Optional[str], description: Optional[str], status: Optional[str]):
        task_data = {}
        if title:
            task_data['title'] = title
        if description:
            task_data['description'] = description
        if status:
            task_data['status'] = status
        return self.repository.update_task(task_id, task_data)

    def delete_task(self, task_id: int):
        return self.repository.delete_task(task_id)

    def list_tasks(self) -> List[Task]:
        return self.repository.list_tasks()
