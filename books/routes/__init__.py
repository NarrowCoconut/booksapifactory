from flask import Blueprint

def init_app(app):
    from . import frontpage, admin
    app.register_blueprint(frontpage.bp)
    app.register_blueprint(admin.bp)
