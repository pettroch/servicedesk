from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base
from .models.file import File
from .models.role import Role
from .models.status import Status
from .models.task import Task
from .models.user import User


engine = create_engine('sqlite:///database/servicedesk.db')
Session = sessionmaker(bind=engine)
session = Session()


def create_db():
    Base.metadata.create_all(engine)

    if not session.query(Role).filter_by(name="Пользователь").first():
        session.add(Role(name="Пользователь"))

    if not session.query(Role).filter_by(name="Оператор").first(): 
        session.add(Role(name="Оператор"))

    if not session.query(Role).filter_by(name="Администратор").first(): 
        session.add(Role(name="Администратор"))

    if not session.query(Status).filter_by(name="Открыта").first(): 
        session.add(Status(name="Открыта"))

    if not session.query(Status).filter_by(name="В процессе").first(): 
        session.add(Status(name="В процессе"))

    if not session.query(Status).filter_by(name="Ожидание ответа").first(): 
        session.add(Status(name="Ожидание ответа"))

    if not session.query(Status).filter_by(name="Оценивание").first(): 
        session.add(Status(name="Оценивание"))

    if not session.query(Status).filter_by(name="Завершена").first(): 
        session.add(Status(name="Завершена"))





    user_role = session.query(Role).filter_by(name="Пользователь").first()
    operator_role = session.query(Role).filter_by(name="Оператор").first()

    if user_role:
        session.add(User(name="User User", role_id=user_role.id))
        session.commit()

    if operator_role:
        session.add(User(name="Op op", role_id=operator_role.id))
        session.commit()

    session.close()
