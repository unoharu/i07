import sqlite3

dbname = 'db.sqlite3'
conn = sqlite3.connect(dbname)

cur = conn.cursor()

def status_reset():
    cur.execute(
        'UPDATE `table` SET status = "o"  WHERE status = "x";'
    )

def id_reset():
    for i in range(13):
        cur.execute(
            f'UPDATE `table` SET id = "{i+1}"  WHERE id = "{i+6}";'
        )

for i in range(2):
    cur.execute(f'INSERT INTO `table`(max_seats, status, id) VALUES (1, "o", {i+11});')
    conn.commit()
rows = cur.fetchall()
for row in rows:
    print(row)
conn.commit()
conn.close()