from flask import Flask
from .extentions import db
from .controllers.user_controller import users

def create_app():
    app = Flask(__name__)

    #configure application
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    # initailize db
    db.init_app(app)

    # Initailize Routees
    app.register_blueprint(users)
    
    # run migrations
    with app.app_context():
        db.create_all()
        
    return app