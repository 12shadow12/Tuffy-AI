from flask import Flask, request
from flask import render_template


app = Flask(__name__)
loop = False

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

@app.route('/textCommand/<query>')
def textCommand(query):
    data = {}
    data['response'] = main.respondToCommand(loop=False, c=query)
    return data

@app.route('/profile')
def profile():
    return render_template("profile.html")

if __name__ == '__main__':
    import main
    app.run()