import sqlite3

DATABASE = "database/flashcard.db"


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn
def init_db():
    conn = get_db()

    with open("database/schema.sql", "r") as f:
        conn.executescript(f.read())

    conn.commit()
    conn.close()
def query_db(query, args=(), one=False):
    conn = get_db()
    cur = conn.execute(query, args)
    rows = cur.fetchall()
    conn.close()

    return (rows[0] if rows else None) if one else rows
def execute_db(query, args=()):
    conn = get_db()
    conn.execute(query, args)
    conn.commit()
    conn.close()