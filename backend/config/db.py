from peewee import SqliteDatabase

sqlite_db = SqliteDatabase(
    "db.sqlite3", pragmas={"journal_mode": "wal", "cache_size": -1024 * 64}
)
