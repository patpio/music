import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY') or 'top_secret'
    ALLOWED_IMAGE_EXTENSIONS = ['jpg', 'jpeg', 'png']
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LANGUAGES = ['en', 'hr']
    ADMIN_VIEWS = []


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('FLASK_DB_URI') or f"sqlite:///{os.path.join(basedir, 'music.db')}"
    IMAGE_UPLOADS = os.environ.get('FLASK_UPLOADS_FOLDER_URI') or os.path.join(basedir, 'uploads')


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'music.db')}"
    IMAGE_UPLOADS = os.path.join(basedir, 'uploads')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'test_music.db')}"
    IMAGE_UPLOADS = os.path.join(basedir, 'uploads')
