import sqlite3

DBNAME = "TEST.db"
conn = sqlite3.connect(DBNAME)
cur = conn.cursor()

cur.execute('INSERT INTO persons(name) values("s4m0r1")')
cur.execute('INSERT INTO persons(name) values("smicle")')
cur.execute('INSERT INTO persons(name) values("kgky_9")')

conn.commit()

cur.close()
conn.close()

print("OK")