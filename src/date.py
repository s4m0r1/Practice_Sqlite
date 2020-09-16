# 時刻をSqliteで扱ってみる

import sqlite3
from datetime import datetime

# データーベースの準備
DBNAME = "TEST.db"
conn = sqlite3.connect(DBNAME)
cur = conn.cursor()

# 文字列をdatetime型にしたりしなかったり

time_1 = "2017-12-01 23:06:19"
time_2 = '2020-09-21 23:38:20'
time_3 = '2021-12-31 23:59:59'

# time_1 = datetime.strptime(time_1, '%Y-%m-%d %H:%M:%S')
# time_2 = datetime.strptime(time_2, '%Y-%m-%d %H:%M:%S')
# time_3 = datetime.strptime(time_3, '%Y-%m-%d %H:%M:%S')

# Discordで利用予定なので架空のIDを指定

# time_1_id = "755154899632783370"
# time_2_id = 755154898749283749
# time_3_id = 755342794729234234

# a = [time_1, time_1_id]

# テーブルに書き込み
# cur.executemany('INSERT INTO schedule_time values(null, ?, ?)', (a,))

# 取り出した日付をリストで受け取る
# [(1,"2020-09-17 21:21:00"),(2, "2020-08-29 23:23:23"),]
cur.execute('SELECT * FROM schedule_time')
print(cur.fetchall())

# IDを使って指定のIDを消す


# conn.commit()

cur.close()
conn.close()

print("OK")