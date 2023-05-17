from fastapi import FastAPI
from app.todo.controllers import todos_controller
from app.todo.models import create_table
from fastapi.middleware.cors import CORSMiddleware

create_table()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todos_controller.router)
