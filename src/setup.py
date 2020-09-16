import sqlite3

DBNAME = "TEST.db"
conn = sqlite3.connect(DBNAME)
cur = conn.cursor()

cur.execute(
    'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')

cur.execute(
    'CREATE TABLE schedule_time(id INTEGER PRIMARY KEY AUTOINCREMENT, time STRING, message_id STRING)')

conn.commit()

cur.close()
conn.close()

print("OK")