from fastapi import APIRouter
from pydantic import BaseModel

from database.models.task import Task
from database.models.user import User
from database.models.status import Status
from database.models.role import Role
from database.db import session


router = APIRouter()

class task_model(BaseModel):
    name: str
    description: str
    # files: str     !!!!!!!!!!!!!
    user_id: int


@router.post("/api/task/create")
async def create(task: task_model):
    user = session.query(User).filter_by(id=task.user_id).first()
    if not user:
        return {"error": "user_id not found"}
    
    operator_role = session.query(Role).filter_by(name="Оператор").first()
    operator = session.query(User).filter_by(role_id=operator_role.id).first()

    new_task = Task(
        name=task.name,
        description=task.description,
        creator_id=user.id,
        operator_id=operator.id,
        status_id=session.query(Status).filter_by(name="Открыта").first().id
    )

    session.add(new_task)
    session.flush()
    session.refresh(new_task)

    task_id = new_task.id
    operator_id = operator.id

    session.commit()
    session.close()

    return {"task_id": task_id, "operator_id": operator_id}
