import sqlite3

conn = sqlite3.connect('ages.sqlite')
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Ages")
cur.execute("CREATE TABLE Ages(name VARCHAR, age INTEGER)")

cur.execute("INSERT INTO Ages(name, age) VALUES(?,?)",("Lenny", 17))