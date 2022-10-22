from flask import Flask
from flask import render_template
import main


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/settings')
def settings():
    return "Settings"

@app.route('/command')
def command():
    main.respondToCommand()
    return

if __name__ == '__main__':
    app.run()