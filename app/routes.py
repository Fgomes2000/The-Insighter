from flask import render_template
from app import app, db
from app.models import User

@app.route('/')
def home():
    users = User.query.all()
    return render_template('index.html', users=users)
