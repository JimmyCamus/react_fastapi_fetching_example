from ..dto.todo_dto import TodoDto
from ..models import Todo


class TodoRepository:
    def get_one(self, id: str):
        try:
            todo = Todo.get_by_id(id)
            res = {
                "id": todo.id,
                "title": todo.title,
                "description": todo.description,
                "is_active": todo.is_active,
            }
            return res
        except Exception:
            return {"error": {"code": 404, "message": "todo not found"}}

    def get_all(self):
        raw_todos = Todo.select()
        todos = []
        for todo in raw_todos:
            todos.append(
                {
                    "id": todo.id,
                    "title": todo.title,
                    "description": todo.description,
                    "is_active": todo.is_active,
                }
            )
        return todos

    def create_one(self, todo_data: TodoDto):
        todo = Todo.create(
            title=todo_data.title,
            description=todo_data.description,
            is_active=todo_data.is_active,
        )
        res = {
            "id": todo.id,
            "title": todo.title,
            "description": todo.description,
            "is_active": todo.is_active,
        }
        return res
