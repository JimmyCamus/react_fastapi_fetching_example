from peewee import Model, CharField, BooleanField
from config.db import sqlite_db


class Todo(Model):
    title = CharField()
    description = CharField()
    is_active = BooleanField(default=True)

    class Meta:
        database = sqlite_db


def create_table():
    if sqlite_db.table_exists("todo"):
        return
    Todo.create_table()
