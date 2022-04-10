from flask import Flask, render_template, request,url_for, session,redirect
from flask_session import Session
import sqlite3 as s

connection = s.connect("Crimereport.db", check_same_thread=False)
crime = Flask(__name__)
global result
#
# @crime.route('/index', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         if request.form["admin"]:
#             return redirect(url_for("/admin"))
#         elif request.form["userlogin"]:
#             return redirect(url_for("/userlogin"))
#         else:
#             return redirect(url_for("/register"))
#
#     return render_template("index.html")


@crime.route('/', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        getUsername = request.form["username"]
        getPassword = request.form["password"]
        if getUsername == "admin" and getPassword == "12345":
            return redirect("/viewcrimes")
    return render_template("admin.html")


@crime.route("/viewcrimes")
def view_crimes():
    cursor = connection.cursor()
    count = cursor.execute("select * from user")
    result = cursor.fetchall()

    return render_template("view.html", report=result)



@crime.route("/filtersearch",methods=['GET','POST'])
def filter():

    if request.method == 'POST':
        getdate = request.form["date"]
        cursor = connection.cursor()
        count = cursor.execute("select * from user WHERE date='"+getdate+"'")
        result = cursor.fetchall()
        return render_template("filtersearch.html", filterreport=result)
    return render_template("filtersearch.html")

@crime.route("/logout")
def logout():
    return render_template("admin.html")
if __name__ == "__main__":
    crime.run(debug=True)
