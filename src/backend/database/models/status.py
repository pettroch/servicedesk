from . import *


class Status(Base):
    __tablename__ = "statuses"
    id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable=False)
