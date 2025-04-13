from flask import *
import sqlite3
import requests

app=Flask(__name__)

AUTH_SERVICE="http://localhost:5001"
BOOK_SERVICE="http://localhost:5002"
ORDER_SERVICE="http://localhost:5003"
 
@app.route("/login",methods=["POST"])
def login():
    data=request.json
    uName=data["uName"]
    uPass=data["uPass"]
    try:
        conn=sqlite3.connect("/bookstore")
        conn.row_factory=sqlite3.Row
        cur=conn.cursor()
        cur.execute("SELECT * FROM users WHERE name=? AND pass=?",(uName,uPass))
        row=cur.fetchone()
        conn.commit()
        conn.close()
        if len(row)!=0:
            return jsonify({"success":True}),200
        else:
            return jsonify({"success":False}),200
    except Exception as e:
        return jsonify({"msg":str(e)}),200

@app.route("/signup",methods=["POST"])
def signup():
    data=request.json
    print("********",data,"************")
    uName=data["uName"]
    uPass=data["uPass"]
    uMail=data["uMail"]
    try:
        conn=sqlite3.connect("/bookstore")
        cur=conn.cursor()
        cur.execute("INSERT INTO users(name,email,pass) VALUES(?,?,?)",(uName,uMail,uPass))
        conn.commit()
        conn.close()
        return jsonify({"success":True}),200
    except Exception as e:
        return jsonify({"msg":str(e)}),200

@app.route("/viewusers",methods=["GET"])
def viewUsers():
    try:
        conn=sqlite3.connect("/bookstore")
        conn.row_factory=sqlite3.Row
        cur=conn.cursor()
        cur.execute("SELECT * FROM users")
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
    app.run(host="0.0.0.0",port=10000,debug=True)

if __name__=='__main__':
    main()
