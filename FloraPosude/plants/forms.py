from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, FileField, TextAreaField, SelectField, FloatField, BooleanField
from wtforms.validators import DataRequired, Optional

from FloraPosude.helpers.validation import *


class MyFloatField(FloatField):
    def process_formdata(self, valuelist):
        if valuelist:
            try:
                self.data = float(valuelist[0].replace(',', '.'))
            except ValueError:
                self.data = None
                raise ValueError(self.gettext('Polje je obezno. Unesite vrijednost u decimalnom obliku.'))


class CreateUpdatePlantForm(FlaskForm):
    name = StringField("Ime biljke", validators=[DataRequired(message="Polje je obvezno.")])
    image = FileField("Slika")
    watering = SelectField(
        "Potrebno zalijevanje", 
        validators=[DataRequired(message="Polje je obvezno.")],
        choices=["Dnevno", "Tjedno", "Mjesečno"]
        )
    place = SelectField(
        "Mjesto boravka", 
        validators=[DataRequired(message="Polje je obvezno.")],
        choices=["Svjetlije", "Tamnije"]
        )
    substrate_addition = BooleanField("Preporučeno dodavanje supstrata")
    description = TextAreaField("Opis", validators=[Optional()])
    temperature = MyFloatField("Idealna temperatura")
    humidity = MyFloatField("Idealna vlažnost zemlje")
    ph_value = MyFloatField("Idealna ph vrijednost tla")
    submit = SubmitField("Spremi")