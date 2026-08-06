from fastapi import FastAPI
from app.api.task_routes import router as task_router
from app.core.config import settings

# Create the FastAPI application
app = FastAPI(
    title = settings.APP_NAME,
    version = settings.VERSION,
    debug = settings.DEBUG

)
app.include_router(task_router, prefix="/tasks", tags=["Tasks"])

# Root endpoint
@app.get("/")
def root():
    return {
        "message" : f"Welcome back to {settings.APP_NAME}!"
    }

# Health check endpoint
@app.get("/health")
def health():
    return{
        "status": "UP",
        "version" : settings.VERSION,
        "service" : settings.APP_NAME
    }

@app.get("/about")
def about():
    return{
        "message" : "This is an about page"
    }
