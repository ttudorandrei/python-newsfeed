from flask import Flask


def create_app(test_config=None):
    # set up config, configure Flask
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes = False
    app.config.from_mapping(
        SECRET_KEY="super_secret_key"
    )

    @app.route("/hello")
    def hello():
        return "hello world"

    return app
