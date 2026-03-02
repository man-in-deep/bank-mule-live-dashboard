import sqlite3

DB_PATH = "db/mule.db"

def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS alerts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        account TEXT,
        score REAL,
        scenarios TEXT,
        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()