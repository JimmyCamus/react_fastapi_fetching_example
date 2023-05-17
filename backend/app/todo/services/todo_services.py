from ..dto.todo_dto import TodoDto
from ..repository.todo_repository import TodoRepository


class TodosService:
    def __init__(self) -> None:
        self.repository = TodoRepository()

    def get_one(self, id: str):
        return self.repository.get_one(id)

    def get_all(self):
        return self.repository.get_all()

    def create(self, todo_data: TodoDto):
        return self.repository.create_one(todo_data)
