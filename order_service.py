from flask import *
import sqlite3
import requests

app=Flask(__name__)

AUTH_SERVICE="http://localhost:5001"
BOOK_SERVICE="http://localhost:5002"
ORDER_SERVICE="http://localhost:5003"


@app.route("/order",methods=["POST"])
def order():
    data=request.json
    print("********",data,"************")
    id=data["id"]
    bId=data["bId"]
    bQty=data["bQty"]
    try:
        conn=sqlite3.connect("/bookstore")
        cur=conn.cursor()
        cur.execute("INSERT INTO orders(id,bid,qty) VALUES(?,?,?)",(id,bId,bQty))
        conn.commit()
        conn.close()
        return jsonify({"success":True}),200
    except Exception as e:
        return jsonify({"msg":str(e)}),200

@app.route("/vieworders",methods=["GET"])
def viewOrders():
    data=request.json
    id=data["uId"]
    try:
        conn=sqlite3.connect("/bookstore")
        conn.row_factory=sqlite3.Row
        cur=conn.cursor()
        cur.execute("SELECT * FROM orders WHERE id=?",(id,))
        rows=cur.fetchall()
        userList=[]
        for row in rows:
            userList.append(dict(row))
        print(userList)
        return jsonify({"data":userList}),200
    except Exception as e:
        print("((()))",str(e))
        return jsonify({"data":str(e)}),200
    
def main():
    app.run(host="0.0.0.0",port=5003,debug=True)

if __name__=='__main__':
    main()