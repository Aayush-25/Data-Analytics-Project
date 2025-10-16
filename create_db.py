# create_db.py
from sqlalchemy import create_engine, text
import os
from pathlib import Path
import sys

SQL_FILE = Path("init_db.sql")
if not SQL_FILE.exists():
    print("init_db.sql not found in project root. Aborting.")
    sys.exit(1)

# default to sqlite file in project folder
default_sqlite = f"sqlite:///{Path.cwd() / 'etl_demo.db'}"
DB_URL = os.environ.get("DATABASE_URL", default_sqlite)
print("Using DB URL:", DB_URL)

engine = create_engine(DB_URL, future=True)

sql = SQL_FILE.read_text()

with engine.begin() as conn:
    # split by semicolon and execute non-empty statements
    for stmt in [s.strip() for s in sql.split(";") if s.strip()]:
        try:
            conn.execute(text(stmt))
        except Exception as e:
            print("Failed executing statement (preview):")
            print(stmt[:200])
            raise

print("Schema applied successfully.")