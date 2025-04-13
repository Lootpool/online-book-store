from flask import *
import sqlite3
import requests

app=Flask(__name__)

AUTH_SERVICE="https://online-book-store-1-sck8.onrender.com"
BOOK_SERVICE="http://localhost:5002"
ORDER_SERVICE="http://localhost:5003"

@app.route("/",methods=["GET"])
def home_page():
    return render_template("index.html")

@app.route("/loginpage",methods=["GET"])
def login_page():
    return render_template("login.html")

@app.route("/login",methods=["POST"])
def login():
    uName=request.form["uName"]
    uPass=request.form["uPass"]
    try:
        response=requests.post(AUTH_SERVICE+"/login",json={"uName":uName,"uPass":uPass})
        if response.status_code==200:
            response=response.json()
            isValid=response["success"]
            if(isValid):
                return viewPage(uName)
            else:
                return render_template("result.html",msg="NO SUCH USER")
        else:
             return render_template("result.html",msg="AUTH_SERIVCE" + response["msg"])
    except Exception as e:
        return render_template("result.html",msg="API-GATEWAY" + str(e))

@app.route("/signuppage",methods=["GET"])
def signup_page():
    return render_template("signup.html")

@app.route("/signup",methods=["POST"])
def signup():
    uName=request.form["uName"]
    uPass=request.form["uPass"]
    uMail=request.form["uMail"]
    try:
        response=requests.post(AUTH_SERVICE+"/signup",json={"uName":uName,"uPass":uPass,"uMail":uMail})
        print("********",response,"********")
        if response.status_code==200:
            response=response.json()
            print("********",response,"********")
            isValid=response["success"]
            if(isValid):
                return viewPage(uName)
            else:
                return render_template("result.html",msg="NO SUCH USER")
        else:
             return render_template("result.html",msg="AUTH_SERIVCE" + response["msg"])
    except Exception as e:
        return render_template("result.html",msg="API-GATEWAY" + str(e))
    
@app.route("/viewusers",methods=["GET"])
def viewUsers():
    try:
        response=requests.get(AUTH_SERVICE+"/viewusers")
        print(response)
        data=response.json()
        print(data)
        return render_template("viewusers.html",rows=data['data'])
    except Exception as e:
        return render_template("result.html",msg="API-GATEWAY" + str(e))

@app.route("/viewbooks",methods=["GET"])
def viewBooks():
    try:
        response=requests.get(BOOK_SERVICE+"/viewbooks")
        print(response)
        data=response.json()
        print(data)
        return render_template("viewbooks.html",rows=data['data'])
    except Exception as e:
        return render_template("result.html",msg="API-GATEWAY" + str(e))


def viewPage(uName):
    return render_template("userPage.html",uName=uName)

@app.route("/orderpage",methods=["GET"])
def orderpage():
    return render_template("order.html")

@app.route("/order",methods=["POST"])
def order():
    id=request.form["id"]
    bId=request.form["bId"]
    bQty=request.form["bQty"]
    try:
        response=requests.post(ORDER_SERVICE+"/order",json={"id":id,"bId":bId,"bQty":bQty})
        print("********",response,"********")
        if response.status_code==200:
            response=response.json()
            print("********",response,"********")
            isValid=response["success"]
            if(isValid):
                return render_template("result.html",msg="ORDER SUCCESSFULLY PLACED")
            else:
                return render_template("result.html",msg="FAILED TO PLACE ORDER")
        else:
             return render_template("result.html",msg="AUTH_SERIVCE" + response["msg"])
    except Exception as e:
        return render_template("result.html",msg="API-GATEWAY" + str(e))

@app.route("/vieworderspage",methods=["GET"])
def viewOrderPage():
    return render_template("vieworderpage.html")

@app.route("/vieworders",methods=["POST"])
def viewOrders():
    uId=request.form['uId']
    try:
        response=requests.get(ORDER_SERVICE+"/vieworders",json={"uId":uId})
        print(response)
        data=response.json()
        print(data)
        return render_template("vieworders.html",rows=data['data'])
    except Exception as e:
        return render_template("result.html",msg="API-GATEWAY" + str(e))

def main():
    app.run(host="0.0.0.0",port=10000,debug=True)

if __name__=='__main__':
    main()
