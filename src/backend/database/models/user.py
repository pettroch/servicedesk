from . import *


class User(Base):
    __tablename__ = "users"
    id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable=False)
    role_id = Column(Integer(), ForeignKey("roles.id"))
