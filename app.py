#importing the necessary tools for the backend to work
from flask import Flask, render_template, request, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
import sqlite3

#setting where to find the database, a secret key for and where to find the static files
app = Flask(__name__, static_url_path='/static')
app.config['SECRET KEY'] = '654392748kl3242dfnkl43235hf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

#database model
class Glassesdb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    counter = db.Column(db.Integer)
    image_file = db.Column(db.String(50))
    prize = db.Column(db.String(4))

#definitions of the bestsellers in the frontend
def first_bestseller():
    conn = sqlite3.connect('site.db')
    c = conn.cursor()
    c.execute('Select * From (Select Row_Number() Over (Order By counter desc) As RowNum, * From Glassesdb) t2 Where RowNum = 1')
    #c.execute('Select * From (SELECT * FROM Glassesdb (ORDER BY counter desc) As RowNum) t2 Where RowNum = 3')
    first_glasses = c.fetchall()
    conn.commit()
    conn.close()
    return first_glasses

def second_bestseller():
    conn = sqlite3.connect('site.db')
    c = conn.cursor()
    c.execute('Select * From (Select Row_Number() Over (Order By counter desc) As RowNum, * From Glassesdb) t2 Where RowNum = 2')
    #c.execute('Select * From (SELECT * FROM Glassesdb (ORDER BY counter desc) As RowNum) t2 Where RowNum = 3')
    first_glasses = c.fetchall()
    conn.commit()
    conn.close()
    return first_glasses

def third_bestseller():
    conn = sqlite3.connect('site.db')
    c = conn.cursor()
    c.execute('Select * From (Select Row_Number() Over (Order By counter desc) As RowNum, * From Glassesdb) t2 Where RowNum = 3')
    #c.execute('Select * From (SELECT * FROM Glassesdb (ORDER BY counter desc) As RowNum) t2 Where RowNum = 3')
    first_glasses = c.fetchall()
    conn.commit()
    conn.close()
    return first_glasses
    
#routes 
@app.route('/')
@app.route('/home')
def index():
    bestseller1 = first_bestseller()
    bestseller2 = second_bestseller()
    bestseller3 = third_bestseller()
    return render_template('index.html', title='Bandoo', bestseller1=bestseller1, bestseller2=bestseller2, bestseller3=bestseller3)

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

#recommendation route
@app.route('/recommendations', methods=["POST", "GET"])
def recommendations():
    if request.method == "POST":
        artist = request.form["artist"]
        color = request.form["color"]
        drink = request.form["drink"]
        bestseller1 = first_bestseller()
        bestseller2 = second_bestseller()
        bestseller3 = third_bestseller()
        gls = int(artist) + int(color) + int(drink)
        conn = sqlite3.connect('site.db') #kann wahrscheinlich rausgenommen werden und nach oben gesetzt werden
        c = conn.cursor()
        if gls <= 5:
            c.execute('UPDATE Glassesdb SET counter = counter +1 WHERE id = 1 ')
            conn.commit()
            conn.close()
            return render_template('i_love_my_gold_chain.html', title='Bandoo', bestseller1=bestseller1, bestseller2=bestseller2, bestseller3=bestseller3)
        elif gls > 5 and gls <=7:
            c.execute('UPDATE Glassesdb SET counter = counter +1 WHERE id = 2 ')
            conn.commit()
            conn.close()
            return render_template('my_life_is_bb.html', title='Bandoo', bestseller1=bestseller1, bestseller2=bestseller2, bestseller3=bestseller3)
        elif gls > 7 and  gls <=9:
            c.execute('UPDATE Glassesdb SET counter = counter +1 WHERE id = 3 ')
            conn.commit()
            conn.close()
            return render_template('i_was_born_with_style.html', title='Bandoo', bestseller1=bestseller1, bestseller2=bestseller2, bestseller3=bestseller3)
        else:
            c.execute('UPDATE Glassesdb SET counter = counter +1 WHERE id = 4 ')
            conn.commit()
            conn.close()
            return render_template('beachvibesbaby.html', title='Bandoo', bestseller1=bestseller1, bestseller2=bestseller2, bestseller3=bestseller3)
    else:
        return render_template('index.html', title='Bandoo')


if __name__=="__main__":
    app.run(debug=True)
