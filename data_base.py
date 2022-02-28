import sqlite3

bd = sqlite3.connect("2048.sqlite")

cur = bd.cursor()
cur.execute("""
create table RECORDS(
    name text,
    score integer
)""")


cur.close