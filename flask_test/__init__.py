from flask import Flask


def create_app():
    app = Flask(__name__)
    app.debug = True

    # blueprint 등록
    from .views import main_views, imginfo_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(imginfo_views.bp)

    return app
