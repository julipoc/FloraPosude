from datetime import datetime 

from FloraPosude import db


class Pot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.String(250), nullable=False)
    status = db.Column(db.String(250), nullable=False)
    watering_date = db.Column(db.DateTime, default=datetime.utcnow)

    plant_id = db.Column(db.Integer, db.ForeignKey("plant.id"))
