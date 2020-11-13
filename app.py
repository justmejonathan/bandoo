from flask import Flask, render_template, request, url_for
#from forms import RegistrationForm
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
        return '''greg{}gre {}terge {}'''.format(artist, color, drink)
        #redirect(url_for("data", ))
    else:
        return render_template('index.html', title='Bandoo')

if __name__=="__main__":
    app.run(debug=True)
