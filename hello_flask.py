from flask import Flask,render_template,redirect,request
import datetime
import sqlite3
app = Flask(__name__)

Insertquery='INSERT INTO DATA(name,age) VALUES("%s","%s")';
Fetchquery='SELECT * from data'

dbfilename = "flaskExpDB.db"

@app.route("/")
def index():
    return "Flask Working fine -- Ruban"
@app.route("/login")


def template():
    return render_template("index.html")
@app.route("/pageone")


def pageone():
    return render_template("firstpage.html")
@app.route("/pagetwo")


def pagetwo():
    return render_template("secondpage.html")
@app.route("/frontpage")


def frontpage():
    return render_template("frontpage.html")
@app.route("/resultpage")


def resultpage():
    return render_template("resultpage.html")
@app.route("/printtime")


def printtime():
    print()
    print(datetime.datetime.now())
    print()
    return redirect("/resultpage")
    
@app.route("/dashboard")
def dashboard():
    name="Ruban"
    notification=5
    mail=8

@app.route("/inputpage")
def inputpage():
    return render_template("inputpage.html")
    
    
@app.route("/statuspage",methods=["post"])
def statuspage():
    status=request.form.get("textinput")
    return render_template("statuspage.html",status=status)
    
@app.route("/templateworks")
def templateworks():
    d=['srinithin','anand','prasnth']
    return render_template("templateworks.html",data=d)

@app.route("/createpost")
def createpost():
    return render_template("createpost.html")
    
@app.route("/page_2",methods=["post"])
def page_2():
    name=request.form.get("name1")
    age=request.form.get("number1")
    conn=sqlite3.connect(dbfilename)
    cursor=conn.cursor()
    cursor.execute(Insertquery%(name,age))
    conn.commit()
    conn.close()
    return render_template("page_2.html",name=name,age=age)
    
def Createtable():
    Createtablequery="""CREATE TABLE IF NOT EXISTS "data" (
                "name" TEXT NOT NULL,
                "age" TEXT NOT NULL,
                "_id" INTEGER NOT NULL, PRIMARY KEY("_id" AUTOINCREMENT)
                );
                """
   
    conn=sqlite3.connect(dbfilename)
    cursor=conn.cursor()
    cursor.execute(Createtablequery)
    conn.commit()
    conn.close()
    
@app.route("/view")
def fetchall():
    conn=sqlite3.connect(dbfilename)
    cursor=conn.cursor()
    cursor.execute(Fetchquery)
    receivedData=cursor.fetchall()
    return render_template("view.html",Result=receivedData)
    
    
if __name__ == "__main__":
    
    Createtable()
    app.run(host="0.0.0.0",port=5050,debug=True)