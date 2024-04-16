from dataclasses import dataclass
from repository import TaskRepository, TaskCache
from schema.task import Task

@dataclass
class TaskService:
    task_repository: TaskRepository
    task_cache: TaskCache
    
    def get_tasks(self):
        if tasks := self.task_cache.redis_get_tasks():
            return tasks
        else:
            tasks = self.task_repository.get_tasks()
            task_schema = [Task.model_validate(task) for task in tasks]
            self.task_cache.redis_set_tasks(task_schema)
            return tasks