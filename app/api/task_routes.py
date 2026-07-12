from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_tasks():
    return {
        "message": "List of tasks will be returned here."
    }

