from flask import Flask
from flask_babel import Babel, lazy_gettext as _l
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
babel = Babel()
login_manager = LoginManager()


def create_app(config_env=''):  # factory function
    app = Flask(__name__)

    if not config_env:
        config_env = app.env

    app.config.from_object(f'config.{config_env.capitalize()}Config')  # from route source

    db.init_app(app)
    babel.init_app(app)
    login_manager.init_app(app)

    login_manager.session_protection = 'strong'
    login_manager.login_view = 'auth.login'
    login_manager.login_message = _l('You need to be logged in to access this page.')  # lazy
    login_manager.login_message_category = 'danger'

    from app.main.views import bp_main
    from app.auth.views import bp_auth

    app.register_blueprint(bp_main)
    app.register_blueprint(bp_auth, url_prefix='/auth')

    Migrate(app, db)

    return app
