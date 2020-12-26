from flask import Flask
from mongoengine import connect

from login_service.routes.access_token import access_token
from login_service.routes.reset_password import reset_pwd
from login_service.routes.sign_in import sign_in
from login_service.routes.sign_up import sign_up
from login_service.routes.token_validator import token_validator
from login_service.util.utility import Util


def create_app():
    app = Flask(__name__)
    app.register_blueprint(sign_up, url_prefix='/api')
    app.register_blueprint(sign_in, url_prefix='/api')
    app.register_blueprint(token_validator, url_prefix='/api')
    app.register_blueprint(reset_pwd, url_prefix='/api')
    app.register_blueprint(access_token, url_prefix='/api')
    return app


if __name__ == '__main__':
    Util.init_config()
    conn = connect(   db='Pollote',
    username='boltathi24',
    password='ZohoTest@24',
    host='mongodb+srv://cluster0.xckok.mongodb.net').Util.config.DATABASE
    app = create_app()
    app.debug = Util.config.DEBUG
    app.run(host=Util.config.APP_HOST, port=Util.config.APP_PORT)
