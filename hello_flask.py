from flask import Flask,render_template,redirect
import datetime
app = Flask(__name__)


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
    
    return render_template("dashboard.html",name_temp=name,notification_temp=notification,mail_temp=mail)
if __name__ == "__main__":
    app.run(host="0.0.0.0")