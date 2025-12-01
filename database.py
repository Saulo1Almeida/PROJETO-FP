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

def initialize_db():
    """Inicializa o banco de dados, criando as tabelas se não existirem."""
    conn = create_connection()
    if conn is not None:
        alunos_table = """
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            matricula TEXT UNIQUE NOT NULL,
            turma_id INTEGER,
            FOREIGN KEY (turma_id) REFERENCES turmas (id)
        );
        """
        professores_table = """
        CREATE TABLE IF NOT EXISTS professores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            matricula TEXT UNIQUE NOT NULL,
            disciplina TEXT NOT NULL
        );
        """
        turmas_table = """
        CREATE TABLE IF NOT EXISTS turmas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            professor_id INTEGER,
            FOREIGN KEY (professor_id) REFERENCES professores (id)
        );
        """
        notas_table = """
        CREATE TABLE IF NOT EXISTS notas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            aluno_id INTEGER NOT NULL,
            disciplina TEXT NOT NULL,
            valor REAL NOT NULL,
            UNIQUE(aluno_id, disciplina),
            FOREIGN KEY (aluno_id) REFERENCES alunos (id)
        );
        """
        
        execute_query(conn, alunos_table)
        execute_query(conn, professores_table)
        execute_query(conn, turmas_table)
        execute_query(conn, notas_table)
        conn.close()
        print("Banco de dados inicializado com sucesso.")
    else:
        print("Não foi possível inicializar o banco de dados.")

if __name__ == '__main__':
    initialize_db()
    
