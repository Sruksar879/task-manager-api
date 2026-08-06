from fastapi import APIRouter
from app.models.task import Task
from app.services.task_service import create_task, get_all_tasks

router = APIRouter()

@router.get("/")
def get_tasks():
    return get_all_tasks()

@router.post("/")
def create_new_task(task:Task):
    return create_task(task)


@router.delete("/{task_id}")
def delete_task(task_id:int):
    return{
        "message" : f"Task {task_id} deleted successfully"
    }