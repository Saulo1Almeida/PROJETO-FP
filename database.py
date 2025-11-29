import sqlite3
from sqlite3 import Error

DATABASE_NAME = "escola.db"

def create_connection():
    """Cria uma conexão com o banco de dados SQLite."""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        conn.row_factory = sqlite3.Row
        return conn
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        if conn:
            conn.close()
        return None
