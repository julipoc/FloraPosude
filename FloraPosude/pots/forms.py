from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Optional

from FloraPosude.helpers.validation import *


class CreateUpdatePotForm(FlaskForm):
    location_name = StringField("Lokacija", validators=[DataRequired(message="Polje je obvezno.")])
    planted_plant = SelectField("Posađena biljka", validators=[Optional()])
    status = SelectField(
        "Status", 
        validators=[DataRequired(message="Polje je obvezno.")],
        choices=["PRAZNA", "POKVARENA", "U REDU"]
        )
    watering = BooleanField("Zaliti biljku?")
    submit = SubmitField("Spremi")