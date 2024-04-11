from . import *


class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable=False)



