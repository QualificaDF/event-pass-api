from database import get_connection

def create_event(nome, data, capacidade, local):
    c = get_connection()
    cur = c.cursor()
    cur.execute(
        "INSERT INTO eventos (nome,data,capacidade,local) VALUES (?,?,?,?)",
        (nome, data, capacidade, local)
    )
    c.commit()
    c.close()

def get_events():
    c = get_connection()
    cur = c.cursor()
    cur.execute("SELECT * FROM eventos")
    rows = cur.fetchall()
    c.close()
    return [dict(r) for r in rows]

def get_event(evento_id):
    c = get_connection()
    cur = c.cursor()
    cur.execute("SELECT * FROM eventos WHERE id=?", (evento_id,))
    r = cur.fetchone()
    c.close()
    return dict(r) if r else None

def delete_event(evento_id):
    c = get_connection()
    cur = c.cursor()
    cur.execute("DELETE FROM eventos WHERE id=?", (evento_id,))
    c.commit()
    c.close()

def get_event_capacity(evento_id):
    c = get_connection()
    cur = c.cursor()
    cur.execute("SELECT capacidade FROM eventos WHERE id=?", (evento_id,))
    r = cur.fetchone()
    c.close()
    return r["capacidade"] if r else None

def count_participants(evento_id):
    c = get_connection()
    cur = c.cursor()
    cur.execute(
        "SELECT COUNT(*) as total FROM participantes WHERE evento_id=?",
        (evento_id,)
    )
    r = cur.fetchone()
    c.close()
    return r["total"]

def add_participant(nome, email, evento_id):
    c = get_connection()
    cur = c.cursor()
    cur.execute(
        "INSERT INTO participantes (nome,email,evento_id) VALUES (?,?,?)",
        (nome, email, evento_id)
    )
    c.commit()
    c.close()
