from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField


class FilterForm(FlaskForm):
    filter_value = StringField("Pretraži")
    submit = SubmitField("Pretraži")
