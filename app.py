from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("escola.db")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/alunos")
def alunos():
    con = get_db()
    cur = con.cursor()


    cur.execute("""
        SELECT alunos.id, alunos.nome, alunos.idade,
               alunos.id_turma, turmas.nome
        FROM alunos
        LEFT JOIN turmas
        ON turmas.id = alunos.id_turma
    """)
    alunos = cur.fetchall()

 
    notas = cur.execute(
        "SELECT aluno_id, disciplina, valor FROM notas"
    ).fetchall()


    turmas = cur.execute("SELECT id, nome FROM turmas").fetchall()

    con.close()


    notas_por_aluno = {}
    for n in notas:
        aluno_id = n[0]
        if aluno_id not in notas_por_aluno:
            notas_por_aluno[aluno_id] = []
        notas_por_aluno[aluno_id].append(n)

    return render_template(
        "alunos.html",
        alunos=alunos,
        notas_por_aluno=notas_por_aluno,
        aluno_editar=None,
        notas_editar=None,
        turmas=turmas
    )


@app.route("/alunos/editar/<int:id>")
def alunos_editar(id):
    con = get_db()
    cur = con.cursor()

    cur.execute("""
        SELECT id, nome, idade, id_turma
        FROM alunos
        WHERE id=?
    """, (id,))
    aluno_editar = cur.fetchone()


    notas_editar = cur.execute("""
        SELECT * FROM notas WHERE aluno_id=?
    """, (id,)).fetchone()


    alunos = cur.execute("""
        SELECT alunos.id, alunos.nome, alunos.idade,
               alunos.id_turma, turmas.nome
        FROM alunos
        LEFT JOIN turmas
        ON turmas.id = alunos.id_turma
    """).fetchall()


    turmas = cur.execute("SELECT id, nome FROM turmas").fetchall()

    con.close()

    return render_template(
        "alunos.html",
        alunos=alunos,
        aluno_editar=aluno_editar,
        notas_editar=notas_editar,
        turmas=turmas
    )


@app.route("/alunos/update/<int:id>", methods=["POST"])
def alunos_update(id):
    nome = request.form["nome"]
    idade = request.form["idade"]
    id_turma = request.form["id_turma"]

    con = get_db()
    cur = con.cursor()

    cur.execute("""
        UPDATE alunos 
        SET nome=?, idade=?, id_turma=?
        WHERE id=?
    """, (nome, idade, id_turma, id))

    con.commit()
    con.close()

    return redirect("/alunos")


@app.route("/alunos/update_notas/<int:id>", methods=["POST"])
def alunos_update_notas(id):
    disciplina = request.form["disciplina"]
    valor = request.form["valor"]

    con = get_db()
    cur = con.cursor()


    count = cur.execute("""
        SELECT COUNT(*) FROM notas WHERE aluno_id=?
    """, (id,)).fetchone()[0]

    if count >= 3:
        con.close()
        return "❌ Este aluno já possui o limite de 3 matérias!", 400

    existing = cur.execute("""
        SELECT id FROM notas 
        WHERE aluno_id=? AND disciplina=?
    """, (id, disciplina)).fetchone()

    if existing:
        cur.execute("UPDATE notas SET valor=? WHERE id=?", (valor, existing[0]))
    else:
        cur.execute("""
            INSERT INTO notas (aluno_id, disciplina, valor)
            VALUES (?, ?, ?)
        """, (id, disciplina, valor))

    con.commit()
    con.close()

    return redirect("/alunos")


@app.route("/alunos/add", methods=["POST"])
def alunos_add():
    nome = request.form["nome"]
    idade = request.form["idade"]
    id_turma = request.form["id_turma"]

    con = get_db()
    cur = con.cursor()

    cur.execute("""
        INSERT INTO alunos (nome, idade, id_turma)
        VALUES (?, ?, ?)
    """, (nome, idade, id_turma))

    con.commit()
    con.close()

    return redirect("/alunos")


@app.route("/alunos/delete/<int:id>")
def alunos_delete(id):
    con = get_db()
    cur = con.cursor()

    cur.execute("DELETE FROM alunos WHERE id=?", (id,))
    cur.execute("DELETE FROM notas WHERE aluno_id=?", (id,))

    con.commit()
    con.close()

    return redirect("/alunos")



@app.route("/professores")
def professores_listar():
    con = get_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM professores")
    professores = cur.fetchall()
    con.close()
    return render_template("professores.html", professores=professores)

@app.route("/professores/editar/<int:id>")
def professores_editar(id):
    con = get_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM professores WHERE id = ?", (id,))
    prof = cur.fetchone()
    con.close()
    return render_template("professores.html",
                           prof_editar=prof,
                           professores=get_todos_professores())

def get_todos_professores():
    con = get_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM professores")
    dados = cur.fetchall()
    con.close()
    return dados

@app.route("/professores/update/<int:id>", methods=["POST"])
def professores_update(id):
    nome = request.form["nome"]
    matricula = request.form["matricula"]
    disciplina = request.form["disciplina"]

    con = get_db()
    cur = con.cursor()
    cur.execute(
        "UPDATE professores SET nome=?, matricula=?, disciplina=? WHERE id=?",
        (nome, matricula, disciplina, id))
    con.commit()
    con.close()

    return redirect("/professores")

@app.route("/professores/add", methods=["POST"])
def professores_add():
    nome = request.form["nome"]
    matricula = request.form["matricula"]
    disciplina = request.form["disciplina"]

    con = get_db()
    cur = con.cursor()
    try:
        cur.execute(
            "INSERT INTO professores (nome, matricula, disciplina) VALUES (?, ?, ?)",
            (nome, matricula, disciplina)
        )
        con.commit()
    except sqlite3.IntegrityError:
        con.close()
        return "❌ Matrícula já cadastrada!", 400

    con.close()
    return redirect("/professores")

@app.route("/professores/delete/<int:id>")
def professores_delete(id):
    con = get_db()
    cur = con.cursor()
    cur.execute("DELETE FROM professores WHERE id=?", (id,))
    con.commit()
    con.close()

    return redirect("/professores")


@app.route("/turmas")
def turmas():
    con = get_db()
    cur = con.cursor()

    cur.execute("""
        SELECT turmas.id, turmas.nome,
               professores.nome
        FROM turmas
        LEFT JOIN professores
        ON turmas.professor_id = professores.id
    """)
    turmas = cur.fetchall()

    cur.execute("SELECT id, nome FROM professores")
    professores = cur.fetchall()

    return render_template(
        "turmas.html",
        turmas=turmas,
        professores=professores,
        turma_editar=None
    )

@app.route("/turmas/editar/<int:id>")
def turmas_editar(id):
    con = get_db()
    cur = con.cursor()

    cur.execute("SELECT * FROM turmas WHERE id=?", (id,))
    turma = cur.fetchone()

    cur.execute("""
        SELECT turmas.id, turmas.nome,
               professores.nome
        FROM turmas
        LEFT JOIN professores
        ON turmas.professor_id = professores.id
    """)
    turmas = cur.fetchall()

    cur.execute("SELECT id, nome FROM professores")
    professores = cur.fetchall()

    return render_template(
        "turmas.html",
        turmas=turmas,
        professores=professores,
        turma_editar=turma
    )

@app.route("/turmas/add", methods=["POST"])
def turmas_add():
    nome = request.form["nome"]
    professor_id = request.form["professor_id"]

    con = get_db()
    cur = con.cursor()
    cur.execute("""
        INSERT INTO turmas (nome, professor_id)
        VALUES (?, ?)
    """, (nome, professor_id))

    con.commit()
    return redirect("/turmas")

@app.route("/turmas/update/<int:id>", methods=["POST"])
def turmas_update(id):
    nome = request.form["nome"]
    professor_id = request.form["professor_id"]

    con = get_db()
    cur = con.cursor()
    cur.execute("""
        UPDATE turmas 
        SET nome=?, professor_id=?
        WHERE id=?
    """, (nome, professor_id, id))

    con.commit()
    return redirect("/turmas")

@app.route("/turmas/delete/<int:id>")
def turmas_delete(id):
    con = get_db()
    cur = con.cursor()
    cur.execute("DELETE FROM turmas WHERE id=?", (id,))
    con.commit()
    return redirect("/turmas")


if __name__ == "__main__":
    app.run(debug=True)
