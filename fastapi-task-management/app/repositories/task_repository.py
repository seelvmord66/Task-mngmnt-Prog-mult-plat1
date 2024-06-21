from sqlalchemy.orm import Session
from app.models.task_model import Task

class TaskRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_task(self, task: Task):
        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)
        return task

    def get_task_by_id(self, task_id: int):
        return self.session.query(Task).filter(Task.id == task_id).first()

    def update_task(self, task_id: int, task_data: dict):
        task = self.get_task_by_id(task_id)
        if not task:
            return None
        for key, value in task_data.items():
            setattr(task, key, value)
        self.session.commit()
        self.session.refresh(task)
        return task

    def delete_task(self, task_id: int):
        task = self.get_task_by_id(task_id)
        if task:
            self.session.delete(task)
            self.session.commit()
        return task

    def list_tasks(self):
        return self.session.query(Task).all()
