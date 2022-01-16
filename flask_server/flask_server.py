from flask import Flask
app = Flask(__name__)

@app.route('/')
def hellow_world():
    return 'Hello! I am Flask application'

if __name__ == '__main__':
    app.run(host='0.0.0.0')

