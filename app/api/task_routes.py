from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_tasks():
    return {
        "message": "List of tasks will be returned here."
    }

@router.post("/")
def create_task():
    return { "message" : "Task created successfully"}


@router.delete("/{task_id}")
def delete_task(task_id:int):
    return{
        "message" : f"Task {task_id} deleted successfully"
    }