from . import *


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(100), nullable=False)
    creator_id = Column(Integer(), ForeignKey("users.id"))
    operator_id = Column(Integer(), ForeignKey("users.id"))
    date = Column(DateTime(), default=datetime.now)
    status_id = Column(Integer(), ForeignKey("statuses.id"))
