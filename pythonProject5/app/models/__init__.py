from app.models.user import User
from app.models.task import Task


from sqlalchemy.schema import CreateTable
print(CreateTable(Task.__table__))

from sqlalchemy.schema import CreateTable
print(CreateTable(User.__table__))
