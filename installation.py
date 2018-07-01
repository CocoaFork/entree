import random
from flask import Flask

app = Flask(__name__)

webview = open('view/installation.html', 'r', encoding = 'utf-8').read()

@app.route('/')
def main():
    webview

@app.route('/', methods=['POST'])
def install():
    webview

def start():
    flask_port_tmp = ''
    for i in range(5):
        flask_port_tmp += str(random.randrange(0, 9))
    app.run('localhost', int(flask_port_tmp))