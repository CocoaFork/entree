import random
from flask import Flask, redirect, url_for, request

app = Flask(__name__)

webview = open('view/installation.html', 'r', encoding = 'utf-8').read()
verifiation_code = ''

@app.route('/')
def main():
    return webview

@app.route('/', methods=['POST'])
def install():
    post_verify = request.form['verifiation-code']
    SQLITE3_FILENAME = request.form['database-filename']
    FLASK_HOST_PORT = request.form['flask-host-port']
    CRYPT_SECRET_KEY = request.form['crypt-secret-key']
    if post_verify == verifiation_code:
        #아래 작동 안함
        LocalSettingsValue = open('LocalSettings-example.py').read()
        LocalSettingsValue.replace("SQLITE3_FILENAME = 'db.db'", "SQLITE3_FILENAME = '"+SQLITE3_FILENAME+"'")
        LocalSettingsValue.replace("FLASK_HOST_PORT = 5000", "FLASK_HOST_PORT = "+FLASK_HOST_PORT)
        LocalSettingsValue.replace("CRYPT_SECRET_KEY = 'This is a secret key.'", "CRYPT_SECRET_KEY = '"+CRYPT_SECRET_KEY+"'")
        with open('LocalSettings.py', 'w') as f:
            f.write(LocalSettingsValue)
        return LocalSettingsValue
    else:
        return 'false'


def start():
    global verifiation_code
    verifiation_code = str(random.random())[2:8]
    flask_port_tmp = str(random.random())[2:6]
    print(' * http://localhost:' + str(flask_port_tmp) + ' 에 접속하여 설정을 진행해 주십시오.')
    print(' * 소유자 증명 코드는  ' + verifiation_code + '  입니다.')
    app.run('localhost', int(flask_port_tmp))