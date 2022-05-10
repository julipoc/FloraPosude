from flask_login import UserMixin

from FloraPosude import db
from FloraPosude import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False) 
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)


