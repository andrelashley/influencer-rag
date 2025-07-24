from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Andre'}
    pdfs = [
        {
            'owner': {'username': 'John'},
            'title': 'info.pdf'
        },
        {
            'owner': {'username': 'James'},
            'title': 'sample.pdf'
        }
    ]
    return render_template('index.html', title='Home', user=user, pdfs=pdfs)