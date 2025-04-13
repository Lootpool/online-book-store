import sqlite3

conn=sqlite3.connect("/bookstore")
cur=conn.cursor()
# cur.execute("CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT,name VARCHAR(25) NOT NULL,email VARCHAR(25) NOT NULL,pass VARCHAR(25) NOT NULL)")
# cur.execute("CREATE TABLE books(bid INTEGER PRIMARY KEY AUTOINCREMENT,title VARCHAR(25) NOT NULL,author VARCHAR(25) NOT NULL,price FLOAT NOT NULL,STOCK INTEGER NOT NULL)")
# cur.execute("CREATE TABLE orders(oid INTEGER PRIMARY KEY AUTOINCREMENT,id INTEGER NOT NULL,bid INTEGER NOT NULL,qty INTEGER NOT NULL,FOREIGN KEY (id) REFERENCES users(id) ON DELETE CASCADE,FOREIGN KEY (bid) REFERENCES books(bid) ON DELETE CASCADE)")

# cur.execute("DROP TABLE users")
# cur.execute("DROP TABLE books")
# cur.execute("DROP TABLE orders")

cur.execute("INSERT INTO books(title,author,price,STOCK) VALUES('Whimpy kid','Jeff Kinney',100,10)")
cur.execute("INSERT INTO books(title,author,price,STOCK) VALUES('Percy Jackson','James',200,3)")
cur.execute("INSERT INTO books(title,author,price,STOCK) VALUES('Wings of Fire','APJ Kalaam',150,5)")

conn.commit()
conn.close()

