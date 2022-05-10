from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired

from FloraPosude.helpers.validation import *


class LoginForm(FlaskForm):
    username = StringField(
        "Korisničko ime", 
        validators=[DataRequired(message="Polje je obvezno."), validate_username]
        )
    password = PasswordField(
        "Lozinka", 
        validators=[DataRequired(message="Polje je obvezno."), validate_password]
        )
    remember_me = BooleanField("Zapamti me?")
    submit = SubmitField("Prijava")


class ProfileForm(FlaskForm):
    first_name = StringField("Ime", validators=[DataRequired(message="Polje je obvezno.")])
    last_name = StringField("Prezime", validators=[DataRequired(message="Polje je obvezno.")])
    username = StringField("Korisničko ime", validators=[DataRequired(message="Polje je obvezno.")])
    password = PasswordField("Lozinka", validators=[DataRequired(message="Polje je obvezno.")])
    submit = SubmitField("Spremi promjene")