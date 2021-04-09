from app import app
from flask import render_template, request

@app.route('/')
@app.route('/index')
def hello_world():
    return render_template('index.html')

@app.route('/calculate')
def calculate():
    req = request.args.to_dict()
    start = req['start']
    end = req['end']

    entry = Divvy.query.get_or_404(entry_id)

    print(req)
    return {"A": "TEST", "B": req}