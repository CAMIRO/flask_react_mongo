from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS


app = Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost/pyhtonreactdb'
PyMongo(app)