from flask  import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


db=SQLAlchemy()
DB_NAMe="database.db"


# Create a flask application
def create_app():
    app=Flask(__name__)#name of the file
    app.config['SECRET_KEY']='SXXK,,JHMVBJH;KU.H'
    app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{DB_NAMe}'
    db.init_app(app)


    from .views import views
    from .auth import auth

    # Register the blueprint in there
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    from .models import User,Note

    create_database(app)
    
    login_manager=LoginManager()
    login_manager.login_view='auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('Website/'+DB_NAMe):
         with app.app_context():
            db.create_all()
            print('Created Database!')


    