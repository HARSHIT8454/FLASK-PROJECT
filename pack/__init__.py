from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
app.config['SECRET_KEY']='ed7faf35bd7d6003bcfc1bc7'

db = SQLAlchemy(app)
bcrypt=Bcrypt(app)

from pack import routes