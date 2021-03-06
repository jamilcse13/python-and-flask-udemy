from math import pi
from flask import Flask, app, render_template, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/table')
def table():
    con = sql.connect("database.db")
    cur = con.cursor()
    print("Opened database successfully")
    cur.execute('CREATE TABLE students (name text, addr text, city text, pin text)')
    con.close()
    return "Table created successfully"

@app.route('/enternew')
def new_student():
    return render_template('student.html')

@app.route('/addrec', methods = ['GET', 'POST'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['addr']
            city = request.form['city']
            pin = request.form['pin']
            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students (name, addr, city, pin) VALUES (?,?,?,?)", (nm, addr, city, pin))
                con.commit()
                msg = "Record successfully added"
        except:
            msg = "error in insert operation"
            con.rollback()
        finally:
            return render_template('result.html', msg = msg)
            con.close()

@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from students")
    rows = cur.fetchall();
    return render_template('list.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)