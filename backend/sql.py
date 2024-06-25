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


cur.execute('SELECT * FROM `table`')
rows = cur.fetchall()
for row in rows:
    print(row)
conn.commit()
conn.close()