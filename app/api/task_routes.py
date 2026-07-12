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
