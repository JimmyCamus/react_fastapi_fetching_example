from fastapi import APIRouter
from ..services import TodosService
from ..dto.todo_dto import TodoDto

router = APIRouter()
todos_service = TodosService()


@router.get("/todos")
async def get():
    return todos_service.get_all()


@router.get("/todos/{id}")
async def get_by_id(id: str):
    return todos_service.get_one(id)


@router.post("/todos")
async def create_todo(todo_data: TodoDto):
    return todos_service.create(todo_data)
