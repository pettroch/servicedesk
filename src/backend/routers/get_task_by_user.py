from fastapi import APIRouter
from pydantic import BaseModel

from database.models.task import Task
from database.db import session


router = APIRouter()

class task_model(BaseModel):
    creator_id: int


@router.get("/api/task/by_user")
async def get_by_user(task: task_model):
    task_q = session.query(Task.id).filter_by(creator_id=task.creator_id).all()

    ids_list = [task_id[0] for task_id in task_q]

    return {"task_ids": ids_list}
