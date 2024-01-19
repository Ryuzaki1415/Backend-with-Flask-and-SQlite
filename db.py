import pymysql

# conn=sqlite3.connect("books.sqlite")
conn=pymysql.connect(
    host='sql12.freesqldatabase.com',
    database='sql12678155',
    user='sql12678155',
    password='c9v5p8zpcW',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor   
 )

cursor= conn.cursor()
sql_query=""" CREATE TABLE book(
    id integer PRIMARY KEY,
    author text NOT NULL,
    language text NOT NULL,
    title text NOT NULL
    )"""
cursor.execute(sql_query)
conn.close()