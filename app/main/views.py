from flask import Blueprint, render_template, url_for
from flask_login import current_user
from werkzeug.utils import redirect

from app.extensions import cache

bp_main = Blueprint('main', __name__, template_folder='templates')


# for endpoint without / to redirect for /lang/
def root():
    return redirect(url_for('main.index'))


@bp_main.route('/')
@cache.cached(timeout=180, unless=lambda: current_user.is_authenticated)  # if user changed, cache is deleted
def index():
    return render_template('index.html')
