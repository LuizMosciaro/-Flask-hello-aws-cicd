from flask import Flask

application = Flask(__name__)

@application.route('/')
def home():
    return "Hello, this is my first deployment with Flask in Python\n \
    Ola, essa é a minha primeira implementação com Flask em Python"

if __name__=='__main__':
    application.run(debug=True)