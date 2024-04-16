from redis import Redis
import json

from schema.task import Task


class TaskCache:
    def __init__(self, redis: Redis):
        self.redis = redis

    def redis_get_tasks(self) -> list[Task]:
        with self.redis as redis:
            tasks_json = redis.lrange('tasks', 0, -1)
            return [Task.model_validate(json.loads(task)) for task in tasks_json]

    def redis_set_tasks(self, tasks: list[Task]):
        tasks_json = [task.json() for task in tasks]
        with self.redis as redis:
            redis.lpush('tasks', *tasks_json)