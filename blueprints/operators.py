
from flask import Blueprint, redirect, render_template, request
from bson.objectid import ObjectId
from models.index import db

operators_blueprint = Blueprint(
    'operators', __name__, url_prefix='/operators')


@operators_blueprint.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'GET':
        operators = list(db.operators.find())
        print(operators, len(operators))
        return render_template('operators/index.html', operators=operators)
    elif request.method == 'POST':
        db.operators.insert_one({
            'name': request.form['name'],
            'description': request.form['description'],
            'symbol': request.form['symbol'],
            'example': request.form['example'],
            'uses': request.form['uses']
        })
        return redirect('/operators')


@operators_blueprint.route('/<char_id>')
def show(char_id):
    print(char_id)
    operator = db.operators.find_one({'_id': ObjectId(char_id)})
    return render_template('operators/show.html', operator=operator)
