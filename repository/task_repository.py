from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session

from database.models import Tasks, Categories
from schema.task import Task


class TaskRepository:
   
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_tasks(self):
        with self.db_session() as session:
            task = session.execute(select(Tasks)).scalars().all()
        return task

    def get_task(self, task_id: int) -> Tasks:
        with self.db_session() as session:
            task = session.execute(select(Tasks).where(task_id == Tasks.id)).scalar_one()
        return task
    
    def create_task(self, task: Task) -> int:
        task_model = Tasks(name=task.name, pomodoro_count=task.pomodoro_count, category_id=task.category_id)
        with self.db_session() as session:
            session.add(task_model)
            session.commit()
            return task_model.id
        
    def update_task_name(self, task_id: int, name: str) -> Tasks:
        query = update(Tasks).where(task_id == Tasks.id).values(name=name).returning(Tasks.id)
        with self.db_session() as session:
            task_id: int = session.execute(query).scalar_one_or_none()
            session.commit()
        return self.get_task(task_id)

    
    def delete_task(self, task_id: int) -> None:
        query = delete(Tasks).where(Tasks.id == task_id)
        with self.db_session() as session:
            task = session.execute(query)
            session.commit()
            return Tasks

    def get_task_by_category_name(self, category_name: str) -> Tasks | None:
        query = select(Tasks).join(Categories, Tasks.category_id == Categories.id).where(Categories.name == category_name)
        with self.db_session() as session:
            task = session.execute(query)
        return task
    