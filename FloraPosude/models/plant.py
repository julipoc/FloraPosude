from FloraPosude import db


class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    image = db.Column(db.String(250), nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    watering = db.Column(db.String(250), nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    place = db.Column(db.String(250), nullable=False)
    substrate_addition = db.Column(db.Boolean, nullable=False)
    description = db.Column(db.Text)
    ph_value = db.Column(db.Float, nullable=False)

    pots = db.relationship("Pot", backref="plant", lazy=True)
