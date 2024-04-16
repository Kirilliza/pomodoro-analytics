from fastapi import APIRouter, status, Depends
from typing import Annotated

from schema.task import Task
from database.database import get_db_session
from repository.task_repository import TaskRepository
from repository.task_cache import TaskCache
from dependency import get_task_repository, get_task_service
from service.task_service import TaskService



router = APIRouter(prefix='/task', tags=['task'])

@router.get("/all", response_model=list[Task])
async def get_tasks(task_service: Annotated[TaskService, Depends(get_task_service)]):
    return task_service.get_tasks()
    

@router.post("/", response_model=Task)
async def create_task(task: Task, task_repository: Annotated[TaskRepository, Depends(get_task_repository)]):
    task_id = task_repository.create_task(task=task)
    task.id = task_id
    return task


@router.patch("/{task_id}", response_model=Task)
async def patch_task(task_id: int, name: str, task_repository: Annotated[TaskRepository, Depends(get_task_repository)]):
    return task_repository.update_task_name(task_id=task_id, name=name)
    

@router.delete("/{task_id}",  status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int, task_repository: Annotated[TaskRepository, Depends(get_task_repository)]):
    task_repository.delete_task(task_id=task_id)
    return {"message": "Task deleted successfully"}
