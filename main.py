from flask import Flask, render_template
import dash

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contat():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run("0.0.0.0", port=8080)

