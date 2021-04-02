#!/usr/local/bin/python
import MySQLdb
import MySQLdb.cursors
from flask import Flask, render_template, jsonify,request,session,redirect,url_for



app = Flask(__name__, static_url_path='')
app.secret_key = b''
count=0
books = {}

def get_db():
    db = MySQLdb.connect(host="",
                         user="",
                         password="",
                         db="")
    return db
db = get_db()

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html',data=str(session['username']),logged_in=True)
    elif 'login_failed' in session:
        return render_template('index.html',data='Login Failed, Try Again',logged_in=False)
    else:
        return render_template('index.html',data='Not Logged In',logged_in=False)

@app.route("/login", methods=["POST"])
def login():
    global db
    cur = db.cursor()
    cur.execute('SELECT * FROM Users where username=%s and password = %s;',(request.form["username"],request.form["password"]))
    if cur.rowcount!=0:
        user = cur.fetchall()[0]
        session['username'] = user[1]
    else:
        session['login_failed']='-1'
    return ''

@app.route("/register", methods=["POST"])
def register():
    global db
    cur = db.cursor()
    try:
        cur.execute('INSERT INTO Users (username,password) VALUES (%s,%s);',(request.form["username"],request.form["password"]))
    except:
        return jsonify(False)
    db.commit()
    return jsonify(True)

@app.route("/logout", methods=["POST"])
def logout():
    if 'username' in session:
        session.pop('username')
    return ''