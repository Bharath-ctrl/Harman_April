from flask import Flask, render_template, request, redirect
import sqlite3 as sql

connection=sql.connect("Books.db",check_same_thread=False)
listofBook = connection.execute("select name from sqlite_master where type='table' AND name='book'").fetchall()

if listofBook!=[]:
    print("Table exist already")
else:
    connection.execute('''create table book(
                             ID integer primary key autoincrement,
                             bookname text,
                             author text,
                             category text,
                             price integer,
                             publisher text
                             )''')
    print("Table Created Successfully")

admin=Flask(__name__)

@admin.route("/",methods=["GET","POST"])
def Login():
    if request.method == "POST":
        getusername=request.form["username"]
        getpassword=request.form["password"]
        print(getusername)
        print(getpassword)
        if getusername=="admin" and getpassword=="1234":
            return redirect("/viewall")
    return  render_template("adminlogin.html")

@admin.route("/entry",methods = ["GET","POST"])
def Book_details():
    if request.method == "POST":
        getbookname=request.form["name"]
        getauthor=request.form["author"]
        getcategory=request.form["category"]
        getprice=request.form["price"]
        getpublisher=request.form["publisher"]
        print(getbookname)
        print(getauthor)
        print(getcategory)
        print(getprice)
        print(getpublisher)
        try:
            connection.execute("insert into book(bookname,author,category,price,publisher)\
                               values('"+getbookname+"','"+getauthor+"','"+getcategory+"',"+getprice+",'"+getpublisher+"')")
            connection.commit()
            print("Book Added Successfully.")
        except Exception as e:
            print("Error occurred ", e)

    return render_template("entry.html")

@admin.route("/search",methods=["GET","POST"])
def search_book():
    if request.method == "POST":
        getbookname=request.form["name"]
        print(getbookname)
        cursor = connection.cursor()
        count = cursor.execute("select * from book where bookname='"+getbookname+"'")
        result = cursor.fetchall()
        return render_template("search.html", searchBook=result)

    return render_template("search.html")

@admin.route("/delete",methods=["GET","POST"])
def delete_book():
    if request.method == "POST":
        getbookname = request.form["name"]
        print(getbookname)

        try:
            connection.execute("delete from book where bookname='"+getbookname+"'")
            connection.commit()
            print("Book Deleted Successfully.")
        except Exception as e:
            print("Error occured ", e)

    return render_template("delete.html")

@admin.route("/update",methods = ["GET","POST"])
def update_book():
    if request.method == "POST":
        getbookname = request.form["name"]
        author = request.form["author"]
        category = request.form["category"]
        price = request.form["price"]
        publisher = request.form["publisher"]
        try:
            connection.execute("update book set author='" + author + "',category='" + category + "',price=" + price + ",publisher='" + publisher + "' where bookname='" + getbookname + "'")
            connection.commit()
            print("Updated Successfully")
        except Exception as e:
            print(e)
        cursor = connection.cursor()
        count = cursor.execute("select * from book where bookname='" + getbookname + "'")
        result = cursor.fetchall()
        return render_template("update.html", searchBook=result)

    return render_template("update.html")



@admin.route("/viewall")
def viewall_book():
    cursor = connection.cursor()
    count = cursor.execute("select * from Book")
    result = cursor.fetchall()
    return render_template("viewall.html", Book=result)



if __name__=="__main__":
    admin.run(debug=True)