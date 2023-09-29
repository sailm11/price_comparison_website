from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/electronics')
def electronics():
    return render_template('electronics.html')

if __name__ == "__main__":
    app.run(debug=True)