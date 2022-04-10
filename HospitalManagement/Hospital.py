from os import abort

from flask import Flask, render_template, request, redirect
import sqlite3 as sql

# from werkzeug.utils import

connection = sql.connect("Hospital_Management.db", check_same_thread=False)
Patientlist = connection.execute("select name from sqlite_master where type='table' AND name='patient'").fetchall()

if Patientlist != []:
    print("Table already exists ")
else:
    connection.execute('''create table patient(
                                ID integer primary key autoincrement,
                                name text,
                                mobile integer,
                                age integer,
                                address text,
                                dob text,
                                place text,
                                pincode integer                                                         
                                )''')
    print("Table Created Successfully")

hospital = Flask(__name__)


@hospital.route("/", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        getusername = request.form["username"]
        getpassword = request.form["password"]
        print(getusername)
        print(getpassword)
        if getusername == "admin" and getpassword == "12345":
            return redirect("/dashboard")
    return render_template("admin.html")


@hospital.route("/dashboard", methods=["GET", "POST"])
def patient_registration():
    if request.method == "POST":
        getname = request.form["name"]
        getmobnumber = request.form["mobile"]
        getage = request.form["age"]
        getaddress = request.form["address"]
        getdob = request.form["dob"]
        getplace = request.form["place"]
        getpincode = request.form["pincode"]
        print(getname)
        print(getmobnumber)
        print(getage)
        print(getaddress)
        print(getdob)
        print(getplace)
        print(getpincode)

        try:
            connection.execute("insert into patient(name,mobile,age,address,dob,place,pincode)\
                               values('" + getname + "'," + getmobnumber + "," + getage + ",'" + getaddress + "','" + getdob + "','" + getplace + "'," + getpincode + ")")
            connection.commit()
            print("Data Added Successfully.")
        except Exception as e:
            print("Error occurred ", e)

    return render_template("dashboard.html")


@hospital.route("/viewall")
def view_patient():
    cursor = connection.cursor()
    count = cursor.execute("select * from patient")
    result = cursor.fetchall()
    return render_template("viewall.html", patient=result)


@hospital.route("/search", methods=["GET", "POST"])
def search_patient():
    if request.method == "POST":
        getmobno = request.form["mobile"]
        print(getmobno)
        cursor = connection.cursor()
        count = cursor.execute("select * from patient where mobile=" + getmobno)
        result = cursor.fetchall()
        return render_template("search.html", searchpatient=result)

    return render_template("search.html")


@hospital.route("/delete", methods=["GET", "POST"])
def delete_patient():
    if request.method == "POST":
        getmobno = request.form["mobile"]
        try:
            connection.execute("delete from patient where mobile=" + getmobno)
            connection.commit()
            print("Patient data Deleted Successfully.")
        except Exception as e:
            print("Error", e)

    return render_template("delete.html")


@hospital.route("/update", methods=["GET", "POST"])
def updatepatient():
    if request.method == "POST":

        getMobno = request.form["mobile"]
        getname = request.form["name"]
        getAge = request.form["age"]
        getAddress = request.form["address"]
        getDob = request.form["dob"]
        getPlace = request.form["place"]
        getPincode = request.form["pincode"]

        try:
            connection.execute(
            "UPDATE patient SET name='" + getname + "', age=" + getAge + ",address='" + getAddress + "',dob='" + getDob + "',place='" + getPlace + "',pincode=" + getPincode + " WHERE mobile=" + getMobno)
            connection.commit()
            print("Updated Successfully")
        except Exception as e:
            print(e)
    return render_template("update.html")

@hospital.route("/updatesearch",methods = ["GET","POST"])
def update_search_patient():
    if request.method == "POST":
        getmobnumber=request.form["mobile"]
        cursor = connection.cursor()
        count = cursor.execute("select * from patient where mobile="+getmobnumber)
        result = cursor.fetchall()

        return render_template("update.html", searchpatient=result)

    return render_template("update.html")

if __name__ == "__main__":
    hospital.run(debug=True)
