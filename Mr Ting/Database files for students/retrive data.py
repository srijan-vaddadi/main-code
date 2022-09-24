import sqlite3

conn = sqlite3.connect('MyFilms.db')
cursor = conn.cursor()

for row in cursor.execute \
            ('select * from tblFilms'):
    print(row)
conn.close()
