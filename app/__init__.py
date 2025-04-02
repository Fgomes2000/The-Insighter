import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
database_path = os.path.join(basedir, '..', 'instance', 'database.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

print(f"Database URI set to: {app.config['SQLALCHEMY_DATABASE_URI']}")  # <-- ADD THIS LINE

db = SQLAlchemy(app)

from app import routes, models