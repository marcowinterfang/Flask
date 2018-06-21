"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template,redirect,Flask,url_for
from flask import request
from MarcoFlask import app
import sys
from mcmysql import loginfo
import pymysql
import hashlib

@app.route('/')
def default():
    return "Test"

@app.route('/home')
def home():
    """Renders the home page."""
    return render_template('index.html',
        title='Home Page',
        year=datetime.now().year,)

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template('contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.')

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template('about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.')
@app.route('/')
@app.route('/signin',methods = ['GET','POST'])
def signin():
    try:
        if request.method == "POST":
            username = request.form["username"]
            password = request.form['password']
            #info = loginfo()
            #password = __md5__(password)
            msg = check(username,password)
            if(msg == 'success'):
                return redirect("home")
            else:
                return render_template('login.html',message = msg)
        return render_template('login.html')
    except Exception:
        return sys.exc_info()[0] + sys.exc_info()[1]

def check(username,password):
    try:
        if(username == "" or password == ""):
            return "AccountId or password is empty,please check"
        if(len(password)<6):
            return "password length must more than 6"
        db = pymysql.connect("localhost","root","Unlock@10","circle")
        cursor = db.cursor()
        sql = "select username,pw from loginfo where username = '" + username + "'"
        nbr = cursor.execute(sql)
        if(nbr == 0):
            return "Your accountId(" + username + ") is NOT EXIST"
        data = cursor.fetchone()
        pw = hashlib.md5(password.encode('utf-8')).hexdigest()
        if(data[1] == pw):
            return "success"
        return "wrong password"
    except Exception:
        return sys.exc_info()[1]


