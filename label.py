from flask import (
        Flask, Blueprint, render_template
)

bp = Blueprint('label', __name__, url_prefix='/label')

@bp.route('/')
def index():
    return render_template('index.html')


