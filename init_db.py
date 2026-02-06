import sqlite3

conn = sqlite3.connect("eventpass.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS eventos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    data TEXT,
    capacidade INTEGER,
    local TEXT
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS participantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT,
    evento_id INTEGER
)
""")

conn.commit()
conn.close()
print("Banco criado com sucesso")
