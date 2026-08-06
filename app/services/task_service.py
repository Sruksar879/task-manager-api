from app.models.task import Task
from app.core.logger import logger

tasks = []

def create_task(task:Task):
    tasks.append(task)
    logger.info(f"Task '{task.title}'created successfully.")
    return task

def get_all_tasks():
    return tasks
