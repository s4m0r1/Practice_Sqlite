import sqlite3

DBNAME = "TEST.db"
conn = sqlite3.connect(DBNAME)
cur = conn.cursor()

cur.execute('DROP TABLE "persons"')
cur.execute('DROP TABLE "schedule_time')


conn.commit()

cur.close()
conn.close()

print("OK")