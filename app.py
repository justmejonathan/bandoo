from flask import Flask, render_template, request, url_for
import sqlite3
app = Flask(__name__)

app.config['SECRET KEY'] = '654392748kl3242dfnkl43235hf'
app.static_folder = 'static'


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', title='Bandoo')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

@app.route('/recommendations', methods=["POST", "GET"])
def recommendations():
    if request.method == "POST":
        artist = request.form["artist"]
        color = request.form["color"]
        drink = request.form["drink"]
        gls = int(artist) + int(color) + int(drink)
        conn = sqlite3.connect('glasses.db', check_same_thread=False)
        c = conn.cursor()
        if gls <= 5:
            c.execute('UPDATE glasses SET counter = counter +1 WHERE id = 1 ')
            return "I love my Gold Chain"        
        elif gls > 5 and gls <=7:
            c.execute('UPDATE glasses SET counter = counter +1 WHERE id = 2 ')
            return "My Life is Bling Bling"
        elif gls > 7 and  gls <=9:
            c.execute('UPDATE glasses SET counter = counter +1 WHERE id = 3 ')
            return "I was Born with Style"
        else:
            c.execute('UPDATE glasses SET counter = counter +1 WHERE id = 4 ')
            return render_template('beachvibesbaby.html', title='Bandoo')
            conn.commit()
            conn.close()
    else:
        return render_template('index.html', title='Bandoo')





if __name__=="__main__":
    app.run(debug=True)