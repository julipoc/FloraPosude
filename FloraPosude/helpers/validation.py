from wtforms.validators import ValidationError

from FloraPosude.models.user import User


def validate_username(form, field):
    user = User.query.filter_by(username=form.username.data).first()
    if user is None:
        raise ValidationError("Netočno korisničko ime.")


def validate_password(form, field):
    user = User.query.filter_by(password=form.password.data).first()
    if user is None:
        raise ValidationError("Netočna lozinka.")