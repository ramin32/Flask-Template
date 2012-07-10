from flask import render_template
from project_name import app

@app.route('/')
def root():
    return render_template('home.html')
