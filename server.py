from flask import Flask, redirect, url_for, render_template, request, session, flash
import sys, hashlib, uuid, binascii, os, json, random
from datetime import timedelta, datetime
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy



app = Flask(__name__)
app.secret_key = "WziLNrfRES7L+964Q3vDnIhkqWgKxf9PFjBm1iwiiu1ZWH9lScgPdy7oyGZkcx4668sV/lkQd4YFg8JX/Pn9Fg=="
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    pwdsalt = db.Column(db.String(100))
    pwdhash = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, pwdsalt, pwdhash, email):
        self.name = name
        self.pwdsalt = pwdsalt
        self.pwdhash = pwdhash
        self.email = email


port = 8000 if len(sys.argv) == 1 else sys.argv[1]

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/")
def home():
    if "user" in session:
        return redirect(url_for("user"))
    return redirect(url_for("login"))

@app.route("/view")
def view():
    return render_template("view.html", values=users.query.all())
    
@app.route("/test")
def test():
    return render_template("new.html")

@app.route("/register", methods=["POST", "GET"])
def register():
    if "user" in session:
        flash("You are already logged in!")
        return redirect(url_for("user"))

    if request.method == "POST":
        user = request.form.get("nm")
        pwa = request.form.get("pwa")
        pwb = request.form.get("pwb")

        if (user == "") or (pwa == "") or (pwb == ""):
            flash("Please complete all fields.")
            return redirect(url_for("register"))
        
        if pwa != pwb:
            flash("Passwords do not match!")
            return redirect(url_for("register"))

        if users.query.filter_by(name=user).first():
            flash("Username taken!")
            return redirect(url_for("register"))


        
        session["user"] = user
        hashed_pw = hash_password(pwa)
        usr = users(user, hashed_pw["salt"], hashed_pw["pwdhash"], None)
        db.session.add(usr)
        db.session.commit()

        flash("Registration successful")
        return redirect(url_for("user"))


        

    else:
        return render_template("register.html")



@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        
        user = request.form["nm"]
        pwd = request.form.get("pwd")
        remember = request.form.get("rmb")
        
        
        found_user = users.query.filter_by(name=user).first()
        
        if found_user:
            hashed_pw = {
                "salt": found_user.pwdsalt,
                "pwdhash": found_user.pwdhash
            }
            if verify_password(hashed_pw,pwd):
                
                flash("Login Successful!")
                session["user"] = user
                return redirect(url_for("user"))

        flash("Invalid details")
        return redirect(url_for("login"))
            

        
    else:
        if "user" in session:
            flash("You are already logged in!")
            return redirect(url_for("user"))
        
        return render_template("login.html")

    flash("ERROR: You do not have access to this feature!")
    return redirect(url_for("user"))


@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        return render_template("user.html", user=user, email=email, vaqlues=users.query.all())
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if not "user" in session:
        return redirect(url_for("login"))
    session.pop("user", None)
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))


@app.errorhandler(404)
def page_not_found(e):
    flash("Error 404, page does not exist!")
    return redirect(url_for("user"))


    

def hash_password(password):

    salt = binascii.b2a_base64(hashlib.sha256(os.urandom(60)).digest()).strip()
    pwdhash = binascii.b2a_base64(hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 10000)).strip().decode()
    return { 'salt': salt.decode(), 'pwdhash': pwdhash } 

def verify_password(stored_password, provided_password):

    pwdhash = hashlib.pbkdf2_hmac('sha256', 
                                  provided_password.encode('utf-8'), 
                                  stored_password['salt'].encode(), 
                                  10000)
    return pwdhash == binascii.a2b_base64(stored_password['pwdhash']) 



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(
        #ssl_context='adhoc',
        debug=True,
        host='0.0.0.0',
        port=port)