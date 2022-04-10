from flask import Flask, render_template, request
import sqlite3 as sql

from werkzeug.utils import redirect

connection=sql.connect("Books.db",check_same_thread=False)
listofBookuser = connection.execute("select name from sqlite_master where type='table' AND name='user'").fetchall()

if listofBookuser!=[]:
    print("Table exist already")
else:
    connection.execute('''create table user(
                             ID integer primary key autoincrement,
                             name text,
                             address text,
                             email text,
                             phone integer,
                             password text
                             )''')
    print("Table Created Successfully")

user=Flask(__name__)

@user.route("/",methods=["POST","GET"])
def register():
    global getemail, getpassword
    if request.method == "POST":
        getname=request.form["name"]
        getaddress=request.form["address"]
        getemail=request.form["email"]
        getphone=request.form["phone"]
        getpassword=request.form["password"]
        try:
            connection.execute("insert into user(name,address,email,phone,password)\
                                   values('" + getname + "','" + getaddress + "','" + getemail + "'," + getphone + ",'" + getpassword + "')")
            connection.commit()
            print("User Added Successfully.")
        except Exception as e:
            print("Error occured ", e)
        return redirect("/userlogin")

    return render_template("register.html")

@user.route("/userlogin",methods=["POST","GET"])
def user_login():
    if request.method=="POST":
        getEmail=request.form["email"]
        getPassword=request.form["password"]
        if getemail==getEmail and getpassword==getpassword:
            return redirect("/viewbook")
    return render_template("userlogin.html")


@user.route("/viewbook")
def user_viewbook():
    cursor = connection.cursor()
    count = cursor.execute("select * from Book")
    result = cursor.fetchall()
    return render_template("viewbook.html", Book=result)

@user.route("/searchbook",methods=["POST","GET"])
def user_search_book():
    if request.method == "POST":
        getbookname=request.form["name"]
        print(getbookname)
        cursor = connection.cursor()
        count = cursor.execute("select * from book where bookname='"+getbookname+"'")
        result = cursor.fetchall()
        return render_template("searchbook.html", searchBook=result)

    return render_template("searchbook.html")

if __name__=="__main__":
    user.run(debug=True)