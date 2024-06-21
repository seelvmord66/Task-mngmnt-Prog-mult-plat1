from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm import Session
from app.services.task_service import TaskService
from app.repositories.task_repository import TaskRepository
from app.models.task_model import Task
from app.database import get_db

router = APIRouter(prefix="/task", tags=["task"])

class TaskCreate(BaseModel):
    title: str
    description: str = None
    status: str

class TaskUpdate(BaseModel):
    title: str = None
    description: str = None
    status: str = None

@router.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    task_repo = TaskRepository(db)
    task_service = TaskService(task_repo)
    return task_service.create_task(task.title, task.description, task.status)

@router.get("/tasks/", response_model=List[Task])
def list_tasks(db: Session = Depends(get_db)):
    task_repo = TaskRepository(db)
    task_service = TaskService(task_repo)
    return task_service.list_tasks()

@router.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task_repo = TaskRepository(db)
    task_service = TaskService(task_repo)
    task = task_service.get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    task_repo = TaskRepository(db)
    task_service = TaskService(task_repo)
    updated_task = task_service.update_task(task_id, task.title, task.description, task.status)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@router.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task_repo = TaskRepository(db)
    task_service = TaskService(task_repo)
    deleted_task = task_service.delete_task(task_id)
    if not deleted_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return deleted_task
