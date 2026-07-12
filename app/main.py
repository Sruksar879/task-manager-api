from fastapi import FastAPI
from app.api.task_routes import router as task_router

# Create the FastAPI application
app = FastAPI()
app.include_router(task_router, prefix="/tasks", tags=["Tasks"])

# Root endpoint
@app.get("/")
def root():
    return {
        "message" : "Welcome to Task Manager API!"
    }

# Health check endpoint
@app.get("/health")
def health():
    return{
        "status": "Healthy"
    }

@app.get("/about")
def about():
    return{
        "message" : "This is an about page"
    }
