from flask import Flask
import sqlite3 
import installation

app = Flask(__name__)

try:
    import LocalSettings
except:
    print(' * LocalSettings.py를 찾을 수 없습니다. ')
    installation.start()

dictionary = open('dic.json', 'r', encoding = 'utf-8').read()
webview = open('view/index.html', 'r', encoding = 'utf-8').read()

@app.route('/')
def main():
    publish_unit = '공개 범위 : '
    if LocalSettings.ENTREE_HOST_PUBLISH == 'local':
        publish_unit += '로컬'
    elif LocalSettings.ENTREE_HOST_PUBLISH == 'server':
        publish_unit += '서버'
    else:
        return 0

app.run(LocalSettings.FLASK_HOST, LocalSettings.FLASK_HOST_PORT)