from flask import Blueprint

books = Blueprint('books', __name__)

from . import views, errors

def init_app(app):
    app.register_blueprint(books)
