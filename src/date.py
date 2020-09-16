# 時刻をSqliteで扱ってみる

import sqlite3
from datetime import datetime

# datetime型を文字列に変換してDBに書き込み

# 取り出した日付をリストで受け取る
# [(1,"2020-09-17 21:21:00"),(2, "2020-08-29 23:23:23"),]

# IDを使って指定のIDを消す

# DBNAME = "TEST.db"
# conn = sqlite3.connect(DBNAME)
# cur = conn.cursor()

# cur.execute('INSERT INTO persons(name) values("s4m0r1")')
# cur.execute('INSERT INTO persons(name) values("smicle")')
# cur.execute('INSERT INTO persons(name) values("kgky_9")')

# conn.commit()

# cur.close()
# conn.close()

# print("OK")