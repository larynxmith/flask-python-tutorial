from flask import Blueprint, render_template
from models.index import db


loops_blueprint = Blueprint(
    'loops', __name__, url_prefix='/loops'
)


@loops_blueprint.route('/')
def index():
    loops = list(db.loops.find())

    return render_template('loops/index.html', loops=loops)
