from app import app
from flask import render_template
@app.route('/')
def index():
    animal = 'Tiger'
    return render_template('index.html',name=animal)