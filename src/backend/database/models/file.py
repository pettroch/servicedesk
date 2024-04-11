from . import *


class File(Base):
    __tablename__ = "files"
    id = Column(Integer(), primary_key=True)
    task_id = Column(Integer(), ForeignKey("tasks.id"))
    path = Column(String(2048), nullable=False)
