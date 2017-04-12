# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
from flask import Flask, render_template
from flask_graphql import GraphQLView

from . import public
from .schema import schema
from .settings import ProdConfig


def create_app(config_object=ProdConfig):
    """
    An application factory.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__.split('.')[0],
                static_folder=config_object.STATIC_FOLDER,
                template_folder=config_object.TEMPLATE_FOLDER)
    app.config.from_object(config_object)

    register_blueprints(app)
    register_add_urls(app)
    register_error_handlers(app)
    register_shell_context(app)

    return app


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(public.views.bp)

    return None


def register_add_urls(app):
    gql_view = GraphQLView.as_view('graphql', schema=schema, graphiql=True)
    app.add_url_rule('/graphql', view_func=gql_view)

    return None


def register_error_handlers(app):
    """Register error handlers."""
    def render_error(error):
        """Render error template."""
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        return render_template('{0}.html'.format(error_code)), error_code

    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)

    return None


def register_shell_context(app):
    """Register shell context objects."""
    def shell_context():
        """Shell context objects."""
        return {'schema': schema}

    app.shell_context_processor(shell_context)
