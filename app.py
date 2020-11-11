from flask import Flask, render_template
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

if __name__=="__main__":
    app.run(debug=True)