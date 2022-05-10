from re import U
from FloraPosude import app
from FloraPosude.data.db_initializer import db_initialize
from FloraPosude.models.user import User


if __name__ == "__main__":
    if User.query.all() == []:
        db_initialize()
    app.run(debug = True)
