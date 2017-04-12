# -*- coding: utf-8 -*-
"""Public section."""
from flask import Blueprint, render_template

bp = Blueprint('public', __name__)


@bp.route('/', methods=['GET'])
def index():
    """Rendering the React template."""
    return render_template('index.html')


@bp.route('/<path:path>', methods=['GET'])
def any_root_path(path):
    """Rendering the React template."""
    return render_template('index.html')
