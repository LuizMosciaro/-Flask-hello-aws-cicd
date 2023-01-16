from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is my first deployment with Flask in Python"

if __name__=='__main__':
    app.run(debug=True)