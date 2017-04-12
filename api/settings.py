from os import environ, pardir
from os.path import abspath, dirname, join


class Config(object):
    """Base configuration."""

    SECRET_KEY = environ.get('API_SECRET', 'secret-key')
    APP_DIR = abspath(dirname(__file__))
    PROJECT_ROOT = abspath(join(APP_DIR, pardir))

    TEMPLATE_FOLDER = abspath(join(PROJECT_ROOT, 'react/build'))
    STATIC_FOLDER = abspath(join(PROJECT_ROOT, 'react/build/static'))


class ProdConfig(Config):
    """Production configuration."""

    ENV = 'prod'
    DEBUG = False


class DevConfig(Config):
    """Development configuration."""

    ENV = 'dev'
    DEBUG = True


class TestConfig(Config):
    """Test configuration."""

    TESTING = True
    DEBUG = True
