import random
from flask import Flask
app = Flask(__name__)

content = ''

def start():
    flask_port_tmp = ''
    for i in range(5):
        flask_port_tmp += str(random.randrange(0, 9))
    app.run('localhost', int(flask_port_tmp))

@app.route('/')
def installation():
    return content