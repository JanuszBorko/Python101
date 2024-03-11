from flask import Flask
app = Flask (__name__)

@app.route('/')
def homepage():
    return 'Home Page AQUI. <a href="/agur"> pincha aqui </a> para volver'

@app.route('/agur')
def agur():
    return "<h1>agur</h1>"
if __name__ == '__main__':
    app.run()