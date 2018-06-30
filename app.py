from flask import Flask
import sqlite3 
import installation

app = Flask(__name__)

try:
    import LocalSettings
except:
    installation.start()