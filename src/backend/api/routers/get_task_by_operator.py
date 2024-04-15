from fastapi import APIRouter
from pydantic import BaseModel

from database.models.task import Task
from database.db import session


router = APIRouter()

class task_model(BaseModel):
    operator_id: int


@router.get("/api/task/by_operator")
async def get_by_operator(task: task_model):
    task_q = session.query(Task.id).filter_by(operator_id=task.operator_id).all()

    ids_list = [task_id[0] for task_id in task_q]

    return {"task_ids": ids_list}
