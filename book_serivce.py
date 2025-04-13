from flask import *
import sqlite3
import requests

app=Flask(__name__)

AUTH_SERVICE="http://localhost:5001"
BOOK_SERVICE="http://localhost:5002"
ORDER_SERVICE="http://localhost:5003"

@app.route("/viewbooks",methods=["GET"])
def viewBooks():
    try:
        conn=sqlite3.connect("/bookstore")
        conn.row_factory=sqlite3.Row
        cur=conn.cursor()
        cur.execute("SELECT * FROM books")
        rows=cur.fetchall()
        bookList=[]
        for row in rows:
            bookList.append(dict(row))
        print(bookList)
        return jsonify({"data":bookList}),200
    except Exception as e:
        print("((()))",str(e))
        return jsonify({"data":str(e)}),200

def main():
    app.run(host="0.0.0.0",port=5002,debug=True)

if __name__=='__main__':
    main()