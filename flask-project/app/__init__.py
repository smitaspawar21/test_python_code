from flask import Flask
from app.auth.routes import auth as auth_blueprint
from app.user.routes import user as user_blueprint

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'  # Set your secret key here

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(user_blueprint)

    return app

app = create_app()