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
def execute_query(conn, query, params=()):
    """Executa uma query SQL (INSERT, UPDATE, DELETE)."""
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"Erro ao executar query: {e}")
        return None

def execute_read_query(conn, query, params=()):
    """Executa uma query SQL de leitura (SELECT)."""
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        return [dict(row) for row in result]
    except Error as e:
        print(f"Erro ao executar query de leitura: {e}")
        return []


