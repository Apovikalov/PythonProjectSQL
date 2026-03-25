import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    database = "test",
    user = "postgres",
    password = "12345"
)

# cursor
# cur = conn.cursor()

# execute query
# cur.executemany("INSERT INTO user_account VALUES (%s, %s), [(3, 'Jon'), (5, 'Jake')]")
# cur.execute("SELECT * FROM user_account")
# conn.commit()

# rows = cur.fetchall()
# for row in rows:
#     print(row)

# close cursor
# cur.close()
conn.close()
