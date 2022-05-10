import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config["SECRET_KEY"] = "secretkey"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "data.sqlite")


db = SQLAlchemy(app)
migrate = Migrate(app, db)

db.create_all()


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "user.login"


from FloraPosude.users.views import user
app.register_blueprint(user)

from FloraPosude.home.views import home
app.register_blueprint(home)

from FloraPosude.plants.views import plant
app.register_blueprint(plant)

from FloraPosude.pots.views import pot
app.register_blueprint(pot)