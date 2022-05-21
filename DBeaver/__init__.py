import sqlite3 as sq

info_users = [
    (1, 'Алексей', 1, 22, 1000),
    (2, 'Миша', 1, 19, 800),
    (3, 'Сергей', 1, 19, 900),
    (4, 'Мария', 2, 18, 1500),
    (5, 'Александр', 1, 20, 1100)
]
with sq.connect('saper.db') as con:
    cur = con.cursor()
    # cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    sex INTEGER NOT NULL DEFAULT 1,
    old INTEGER,
    score INTEGER   
    )""")

    # cur.executemany("INSERT INTO users VALUES (?, ?, ?, ?, ?)", info_users)
    cur.execute("SELECT * FROM users")
    result = cur.fetchall()
    print(result)
    cur.execute("SELECT * FROM users WHERE sex = 2")
    result = cur.fetchall()
    print(result)
    cur.execute("SELECT * FROM users WHERE score < 1000")
    result = cur.fetchall()
    print(result)
    cur.execute("SELECT * FROM users WHERE score > 1400")
    result = cur.fetchall()
    print(result)
    cur.execute("SELECT * FROM users WHERE old BETWEEN 18 AND 20")
    result = cur.fetchall()
    print(result)
